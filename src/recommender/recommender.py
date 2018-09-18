import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

import os, sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from src.recommender.cluster import Cluster
from src.recommender.data import Data
from src.recommender.menu import Menu


class Recommender:

    def __init__(self, cluster=False):
        if cluster:
            self.cluster = Cluster()
        self.data = Data()
        year, week = self._get_year_week()
        self.menu = Menu(year, week)
        self.user_similarities = self._set_total_usr_usr_simis()

    def _get_year_week(self):
        import datetime
        now = datetime.datetime.now()
        week =datetime.datetime(int(now.year), int(now.month), int(now.day)).isocalendar()[1]
        return now.year, week

    def _set_total_usr_usr_simis(self):
        """Compute initial user-user-similarities (for all metrics) across all users in the provided ratings-data.
        
        These can later be substituted with in-cluster similarities where needed.
        """
        user_similarities = {}
        for metric in ['correlation', 'cosine', 'dice', 'jaccard']:
            user_similarities[metric] = self._create_user_user_sim(metric=metric)
        return user_similarities

    def _create_user_user_sim(self, users=None, metric='cosine'):
        """Users can be provided to compute similarities only across the specified users."""
        if users != None:
            df_user_item_updated = self.df_user_item.loc[users,:]
            user_similarity = pd.DataFrame(1 - pairwise_distances(df_user_item_updated, metric=metric),
                                           index = df_user_item_updated.index,
                                           columns = df_user_item_updated.index)
            return user_similarity
        else:
            user_similarity = pd.DataFrame(1 - pairwise_distances(self.data.df_user_item, metric=metric),
                                           index = self.data.df_user_item.index,
                                           columns = self.data.df_user_item.index)
            return user_similarity
    
    # not tested yet /!\
    def update_user_user_sim(self, users, metric):
        """Update user_similarities[metric] to the user-simis only accounting for subset of users."""
        self.user_similarities[metric] = self._create_user_user_sim(users, metric=metric)


    def get_similar_users(self, current_user, metric="cosine", simi_threshhold=0):
        df_sim_mat = self.user_similarities[metric]
        similar_users = list(df_sim_mat[df_sim_mat.loc[current_user] > simi_threshhold].index)
        similar_users.remove(current_user)
        return similar_users

    def predict_rating(self, current_user, m_id=None, similar_users=[], metric='cosine', explain=False):
        # if no list of similar_user provided, compute it first
        if len(similar_users) == 0:
            similar_users = self.get_similar_users(current_user, metric)

        if explain:
            print("Similar users: {}".format(similar_users))
            if m_id is None:
                print("Predicting ratings for user {} with `{}`".format(current_user, metric))
            else:
                print("Predicting rating for user {} & meal {} ({}) with `{}`".format(current_user, m_id, self.data._df_meals[self.data._df_meals['m_id'] == m_id].loc[:,'uTitle'].to_string(), metric))
                print("... with sim. user ratings of {} for meal {}".format([self.data.df_user_item.loc[u,m_id] for u in similar_users], m_id))

        # if no meal_id provided, predict ratings for all known meals (probably only for debugging) ...
        if m_id is None:
            return self._bulk_predict(current_user, similar_users, metric)
        else:
            # ... otherwise predict for user X rating of meal Y
            return self._predict(current_user, similar_users, m_id, metric)

    def _predict(self, current_user, similar_users, m_id, metric):
        real_rating = self.data.df_user_item.loc[current_user].loc[m_id]
        if real_rating != 0:
            return real_rating
        else:
            sum_ratings, sum_sim = 0, 0
            for sim_user in similar_users:
                similarity = self.user_similarities[metric].loc[current_user].loc[sim_user]
                rating = self.data.df_user_item.loc[sim_user].loc[m_id]
                if rating == 0:
                    continue
                sum_ratings += rating * similarity
                sum_sim += similarity
            if sum_sim == 0:
                return 0
            else:
                prediction = sum_ratings / sum_sim
                return prediction

    def _bulk_predict(self, current_user, similar_users, metric):
        """Note that now m_id not explicitely given, but rather compute all ratings of 0-rating (Debugging only?) ."""
        preserved_current_rating = self.data.df_user_item.loc[current_user].replace(0, np.nan)

        aggregated_similar_user_ratings = self.data.df_user_item.loc[similar_users].replace(0, np.nan)
        # print(aggregated_similar_user_ratings.head())
        aggregated_similar_user_ratings['user'] = [current_user for _ in range(len(aggregated_similar_user_ratings.index))]
        # print(aggregated_similar_user_ratings.head())
        aggregated_similar_user_ratings = aggregated_similar_user_ratings.groupby('user').mean().fillna(0)
        # print(aggregated_similar_user_ratings)

        for idx, preserved_rating in preserved_current_rating.iteritems():
            if preserved_rating > 0:
                aggregated_similar_user_ratings.loc[:,idx] = preserved_rating
        return aggregated_similar_user_ratings

    def predict_cluster(self, current_user, m_id=None):
        real_ratings = self.data.df_user_item.loc[current_user]
        user_cluster = self.cluster.predict_cluster(real_ratings)
        neighbors = self.cluster.get_neighbbors(user_cluster[0])

        if m_id is None:
            return self._bulk_predict_average(current_user, neighbors)
        else:
            return self._predict_average(current_user, neighbors, m_id)

    def _predict_average(self, current_user, neighbors, m_id):
        real_rating = self.data.df_user_item.loc[current_user].loc[m_id]
        if real_rating != 0:
            return real_rating
        ratings = self.data.df_user_item[self.data.df_user_item.index.isin(neighbors)].loc[:, m_id]
        average_prediction = ratings.where(ratings > 0).mean()
        if np.isnan(average_prediction):
            return 0
        else:
            return average_prediction

    def _bulk_predict_average(self, current_user, neighbors):
        preserved_current_rating = self.data.df_user_item.loc[current_user]
        ratings = self.data.df_user_item[self.data.df_user_item.index.isin(neighbors)]
        average_prediction = ratings.where(ratings > 0).mean()
        for idx, preserved_rating in preserved_current_rating.iteritems():
            if preserved_rating > 0:
                average_prediction[idx] = preserved_rating
        return average_prediction


if __name__ == "__main__":
    r = Recommender()
    # # print(r.user_similarities['cosine'].head())
    # # print(r.get_similar_users(1,'cosine'))
    # print(r.data.df_user_item.loc[1])
    # print(r.predict_rating(1, 115, explain=True))
    # print(r.predict_rating(1, explain=True))

    # r = Recommender(cluster=True)
    # print(r.predict_cluster(1, 601))

    print(r.menu.df_menus)

