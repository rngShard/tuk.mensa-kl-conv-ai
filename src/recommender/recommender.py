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
        self.df_user_item = self.create_user_item()
        ind = self.df_user_item.index
        self.user_similarity = self.compute_user_sim()
        self.user_similarity.columns = ind
        self.user_similarity.index = ind
    def create_user_item(self):
        df_user_item = self.df_ratings.pivot_table(index="user",
                                                   columns="m_id",
                                                   values="rating",
                                                   aggfunc=np.mean).fillna(0)
        return df_user_item

    def compute_user_sim(self, metric="cosine"):
        user_similarity = pd.DataFrame(1 - pairwise_distances(self.df_user_item, metric=metric))
        return user_similarity

    def get_all_similar_users(self, current_user):
        similar_users = list(self.user_similarity[self.user_similarity.loc[current_user] > 0].index)
        # similar_users = [i + 1 for i in similar_users]
        return similar_users

    def predict_rating(self, current_user, m_id):
        similar_users = self.get_all_similar_users(current_user)
        real_rating = self.df_user_item.loc[current_user].loc[m_id]
        if real_rating != 0:
            return m_id, real_rating
        else:
            sum_ratings = 0
            sum_sim = 0
            for sim_user in similar_users:
                if sim_user == current_user:
                    continue
                else:
                    similarity = self.user_similarity.loc[current_user].loc[sim_user]
                    rating = self.df_user_item.loc[sim_user].loc[m_id]
                    if rating == 0:
                        continue
                    sum_ratings += rating * similarity
                    sum_sim += similarity
            if sum_sim == 0:
                return m_id, 0
            else:
                prediction = sum_ratings / sum_sim
                return m_id, prediction


if __name__ == "__main__":
    recommender = Recommender()
    print(recommender.predict_rating(1, 115))
