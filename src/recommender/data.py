import os
import sys

import numpy as np
import pandas as pd

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
from definitions import ROOT_DIR
from util.cloud_connection import bucket_connection

RATING_CSV = ROOT_DIR + '/data/rating_normalized.csv'


class Data:

    def __init__(self):
        self._df_meals = bucket_connection.get_meals()
        self._df_ratings = self._assign_ratings(RATING_CSV)
        self.df_initial_user_item = self._create_initial_user_item()
        self.df_user_item = {}

    def _assign_ratings(self, path_to_csv):
        df_ratings = pd.read_csv(path_to_csv)
        df_ratings = df_ratings.assign(
            title_prim=[self._df_meals.loc[(self._df_meals['m_id'] == m_id),
                                           'uTitle'].to_string(index=False)
                        for m_id in df_ratings.loc[:, 'm_id']])
        return df_ratings

    def _create_initial_user_item(self):
        df_user_item = self._df_ratings.pivot_table(index="user",
                                                    columns="m_id",
                                                    values="rating",
                                                    aggfunc=np.mean).fillna(0)
        return df_user_item

    def _create_user_item(self, rating):
        self.df_user_item[rating.name] = self.df_initial_user_item.append(rating)

    def get_meal_ids(self):
        return self.df_initial_user_item.columns

    def get_user_item(self, user):
        return self.df_user_item[user]
