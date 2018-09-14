import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

from definitions import ROOT_DIR
from util.cloud_connection import bucket_connection

RATING_CSV = ROOT_DIR + '/data/rating_normalized.csv'


class Recommender:

    def __init__(self, simi_threshhold=0):
        self.df_ratings = pd.read_csv(RATING_CSV)
        self.df_meals = bucket_connection.get_meals()
        self.df_ratings = self.df_ratings.assign(
            title_prim=[self.df_meals.loc[(self.df_meals['m_id'] == m_id),
                                          'uTitle'].to_string(index=False)
                        for m_id in self.df_ratings.loc[:, 'm_id']])
        
        self.df_user_item = self._create_user_item()
        self.user_similarity = {}
        for metric in ['correlation', 'cosine', 'dice', 'jaccard']:
            self.user_similarity[metric] = self._create_user_user_sim(self.df_user_item.index, metric=metric)
        self.simi_threshhold = simi_threshhold

    def _create_user_item(self):
        df_user_item = self.df_ratings.pivot_table(index="user",
                                                   columns="m_id",
                                                   values="rating",
                                                   aggfunc=np.mean).fillna(0)
        return df_user_item

    def _create_user_user_sim(self, user_index, metric):
        user_similarity = pd.DataFrame(1 - pairwise_distances(self.df_user_item, metric=metric))
        user_similarity.index = user_index
        user_similarity.columns = user_index
        return user_similarity

    def get_all_similar_users(self, current_user, metric="cosine"):
        df_sim_mat = self.user_similarity[metric]
        similar_users = list(df_sim_mat[df_sim_mat.loc[current_user] > self.simi_threshhold].index)
        similar_users.remove(current_user)
        return similar_users

    def predict_rating(self, current_user, m_id=None, metric='cosine', explain=False):
        similar_users = self.get_all_similar_users(current_user, metric)

        if explain:
            print("Similar users: {}".format(similar_users))
            if m_id is None:
                print("Predicting ratings for user {} with `{}`".format(current_user, metric))
            else:
                print("Predicting rating for user {} & meal {} ({}) with `{}`".format(current_user, m_id, self.df_meals[self.df_meals['m_id'] == m_id].loc[:,'uTitle'].to_string(), metric))
                print("... with sim. user ratings of {} for meal {}".format([self.df_user_item.loc[u,m_id] for u in similar_users], m_id))

        if m_id is None:
            return self.bulk_predict(current_user, similar_users, metric)
        else:
            return self.predict(current_user, similar_users, m_id, metric)

    def predict(self, current_user, similar_users, m_id, metric):
        real_rating = self.df_user_item.loc[current_user].loc[m_id]
        if real_rating != 0:
            return real_rating
        else:
            sum_ratings, sum_sim = 0, 0
            for sim_user in similar_users:
                similarity = self.user_similarity[metric].loc[current_user].loc[sim_user]
                rating = self.df_user_item.loc[sim_user].loc[m_id]
                if rating == 0:
                    continue
                sum_ratings += rating * similarity
                sum_sim += similarity
            if sum_sim == 0:
                return 0
            else:
                prediction = sum_ratings / sum_sim
                return prediction
    def bulk_predict(self, current_user, similar_users, metric):
        """Note that now m_id not explicitely given, but rather compute all ratings of 0-rating."""
        preserved_current_rating = self.df_user_item.loc[current_user].replace(0, np.nan)

        aggregated_similar_user_ratings = self.df_user_item.loc[similar_users].replace(0, np.nan)
        # print(aggregated_similar_user_ratings.head())
        aggregated_similar_user_ratings['user'] = [current_user for _ in range(len(aggregated_similar_user_ratings.index))]
        # print(aggregated_similar_user_ratings.head())
        aggregated_similar_user_ratings = aggregated_similar_user_ratings.groupby('user').mean().fillna(0)
        # print(aggregated_similar_user_ratings)

        for idx, preserved_rating in preserved_current_rating.iteritems():
            if preserved_rating > 0:
                aggregated_similar_user_ratings.loc[:,idx] = preserved_rating
        return aggregated_similar_user_ratings




if __name__ == "__main__":
    recommender = Recommender(simi_threshhold=0)
    
    for u in recommender.df_user_item.index:
        print(recommender.predict_rating(u, metric='cosine', explain=True))
