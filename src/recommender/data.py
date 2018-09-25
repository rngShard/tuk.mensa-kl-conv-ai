import os
import re
import sys

import numpy as np
import pandas as pd

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
from definitions import ROOT_DIR
from util.cloud_connection import bucket_connection

RATING_CSV = ROOT_DIR + '/data/rating_normalized.csv'


def clean_title_additives(title):
    regex = "\([A|Bio|Ei|En|Fi|Gl|Gt|G|Kr|K|La|Lu|L|Nu|R|Se|Sf|Sl|So|Sw|S|V+|V|Wt|W|1|2|3|4|5|6|7|8|9|10].*?\)"
    reg = re.compile(regex)
    pos = reg.findall(title)
    for i in pos:
        title = title.replace(i, "")
    return title

class Data:

    def __init__(self):
        self._df_meals = bucket_connection.get_meals()
        self._df_ratings = self._assign_ratings(RATING_CSV)
        self.df_initial_user_item = self._create_initial_user_item()
        self.df_user_item = {}
        self.df_additives = bucket_connection.get_additives()

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

        df_user_item_mids = set(df_user_item.columns)
        df_meals_mids = set(self._df_meals.m_id)
        missing_columns = set.difference(df_meals_mids, df_user_item_mids)
        values = np.zeros(len(df_user_item.index))
        for i in missing_columns:
            df_user_item[i] = values
        df_user_item = df_user_item.reindex(sorted(df_user_item.columns), axis=1)
        return df_user_item

    def _create_user_item(self, rating):
        self.df_user_item[rating.name] = self.df_initial_user_item.append(rating)

    def get_meal_ids(self):
        return self.df_initial_user_item.columns

    def get_meals(self):
        return self._df_meals

    def get_meal_title(self, m_id):
        return self._df_meals[self._df_meals.m_id == m_id].title.values[0]

    def get_meal_title_without_additives(self, m_id):
        title = self.get_meal_title(m_id)
        regex = "\([A|Bio|Ei|En|Fi|Gl|Gt|G|Kr|K|La|Lu|L|Nu|R|Se|Sf|Sl|So|Sw|S|V+|V|Wt|W|1|2|3|4|5|6|7|8|9|10].+?\)"
        reg = re.compile(regex)
        pos = reg.findall(title)
        for i in pos:
            title = title.replace(i, "")
        return title

    def get_additives_table(self):
        return self.df_additives

    def get_user_item(self, user):
        return self.df_user_item[user]

    def get_meal_additives(self, m_id):
        regex = "(A|Bio|Ei|En|Fi|Gl|Gt|G|Kr|K|La|Lu|L|Nu|R|Se|Sf|Sl|So|Sw|S|V+|V|Wt|W|1|2|3|4|5|6|7|8|9|10)(,|\))"
        reg = re.compile(regex)
        pos = reg.findall(self.get_meal_title(m_id))
        additive_set = set()
        for po in pos:
            additive_set.add(po[0])
        return additive_set


if __name__ == "__main__":
    data = Data()
    print(data.get_meal_title(57))
    print(data.get_meal_title_without_additives(57))
    print(data.get_meal_additives(115))

    # for t in [75, 112, 121, 113, 118]:
    #     print(data.get_meal_title(t))
    # print(data.get_meal_additives(115))