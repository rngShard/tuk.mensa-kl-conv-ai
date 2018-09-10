import os
import sys

import pandas as pd

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_path)
from cloud_connection import bucket_connection


class IndexNormalizer:

    def __init__(self, source_path_ratings="rating.csv"):
        self.source_path_ratings = source_path_ratings
        self.df_ratings = pd.read_csv(source_path_ratings)

        bucket_connection.download_blob("mensa_data", "meal_norm_2.csv", "./meal.csv")
        self.df_meals = pd.read_csv("meal.csv")

    def update_index(self):
        # Based on the normalized title values without additives
        new_index = 0
        index_tracker = set()
        for i in self.df_meals.iterrows():
            # for i in df_meals[df_meals.title_norm.duplicated()].iterrows():

            if i[1].m_id in index_tracker:
                print(i[1].m_id, index_tracker)
                continue
            else:
                ident_meal_id = self.df_meals[self.df_meals["uTitle"] == i[1].uTitle].m_id
                self.df_meals.m_id = self.df_meals.m_id.replace(list(ident_meal_id), new_index)
                self.df_ratings.m_id = self.df_ratings.m_id.replace(list(ident_meal_id), new_index)
                self.df_meals.drop_duplicates(subset="m_id", inplace=True)
            index_tracker.add(new_index)
            new_index += 1

    def export_to_csv(self, path_meal="meal.csv", path_rating="rating.csv"):
        current_file = os.path.abspath(os.path.dirname(__file__))
        os_file_path = os.path.join(current_file, path_meal)
        self.df_meals.to_csv(os_file_path, encoding='utf-8', index=False)
        current_file = os.path.abspath(os.path.dirname(__file__))
        os_file_path = os.path.join(current_file, path_rating)
        self.df_ratings.to_csv(os_file_path, encoding='utf-8', index=False)

    def export_to_bucket(self):
        bucket_connection.upload_blob("mensa_data", "meal.csv", "meal.csv")

    def normalize_index(self):
        self.update_index()
        self.export_to_csv()
        self.export_to_bucket()


if __name__ == "__main__":
    normalizer = IndexNormalizer()
    normalizer.normalize_index()
