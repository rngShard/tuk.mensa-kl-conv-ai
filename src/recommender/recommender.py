import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

from definitions import ROOT_DIR
from util.cloud_connection import bucket_connection

RATING_CSV = ROOT_DIR + '/data/rating_normalized.csv'


class Recommender:

    def __init__(self):
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
        similar_users = list(df_sim_mat[df_sim_mat.loc[current_user] > 0].index)
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
            return [self.predict(current_user, similar_users, m_id, metric) for m_id in self.df_user_item.columns]
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


if __name__ == "__main__":
    recommender = Recommender()
    print(recommender.predict_rating(1, metric='cosine', explain=True))
