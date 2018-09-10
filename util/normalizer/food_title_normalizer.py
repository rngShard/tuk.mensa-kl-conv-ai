#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import os
import re

import pandas as pd

DEFAULT_MEAL_CSV_PATH = '../../data/meal_manually_cleaned.csv'

class FoodNormalizer:
    """Normalizing the provided meal-csv-data into consise, usable format."""

    def __init__(self, csv_path, absolute_csv_path=None):
        if absolute_csv_path is None:
            current_file = os.path.abspath(os.path.dirname(__file__))
            csv_os_file_path = os.path.join(current_file, csv_path)
            self.meal_csv_path = csv_os_file_path
            self.meal_df_original = pd.read_csv(csv_os_file_path)
            self.meal_df = pd.read_csv(csv_os_file_path)
        else:
            self.meal_csv_path = csv_path
            self.meal_df_original = pd.read_csv(csv_path)
            self.meal_df = pd.read_csv(csv_path)
        self.meal_index_tracker = set()
    @staticmethod
    def separate_food_title(title, ignore_additives):
        """Separate single string (food-title) into its food components."""

        re_title_delimiters = ', | mit | und |, dazu|:| in '
        title_split = re.split(re_title_delimiters, title)
        
        def separate_additives(component):
            """Given a component from the food-title-string, this returns a tuple of (component_str, additives_str)."""
            additives = re.search('\([\w\+]{1,2}(,[\w\+]{1,2})*\)', component)
            additives = additives.group(0) if additives else ''
            ad_escaped = additives.replace('(', '\(').replace(')','\)').replace('+','\+')
            component = re.sub(ad_escaped, '', component) if additives else component

            addit_in_name_component = re.search('\([\w\+]{1,2}(,[\w\+]{1,2})*\)', component)    # in case of nested additives
            addit_in_name_component = addit_in_name_component.group(0) if addit_in_name_component else ''
            if addit_in_name_component:
                escaped = addit_in_name_component.replace('(', '\(').replace(')','\)').replace('+','\+')
                component = re.sub(escaped, '', component)
                additives = additives[0:-1]+','+addit_in_name_component[1:]
            
            component = component.strip()
            return [component, additives] if (additives and ignore_additives) else [component]
        title_split_components = [separate_additives(component) for component in title_split]
            
        return title_split_components

    def get_prim_title(self, titles_norm_comps):
        """Takes components of title and generates a primary title of the meal.
        
        E.g. "[['Chinesisches Gemüse'], ['Hähnchenbruststreifen süß-sauer'], ['Reis']]" --> "chinesisches gemüse"
        This takes into account the first meal component without additives and
        - takes all lowercase
        """
        title_prim = titles_norm_comps[0][0]
        title_prim = title_prim.lower()

        return title_prim

    def get_unique_meal_ids(self, titles_prim):
        """Assign unique food IDs
        
        Based additionally on
        - Levenshtein distance
        - same-title dictionary
        to filter for same food entries.
        """
        unique_titles = []
        for title in titles_prim:
            if title not in unique_titles:
                unique_titles.append(title)
        unique_meal_ids = [unique_titles.index(title) for title in titles_prim]
        return unique_meal_ids


    def assign_norm_titles(self):
        titles = self.meal_df.title

        titles_norm_additives = [FoodNormalizer.separate_food_title(title, True) for title in titles]
        titles_norm = [FoodNormalizer.separate_food_title(title, False) for title in titles]

        titles_prim = [self.get_prim_title(title) for title in titles_norm]
        titles_uID = self.get_unique_meal_ids(titles_prim)
        
        self.meal_df = self.meal_df.assign(title_prim=titles_prim)
        self.meal_df = self.meal_df.assign(title_norm=titles_norm)
        self.meal_df = self.meal_df.assign(title_norm_additives=titles_norm_additives)
        self.meal_df = self.meal_df.assign(uID=titles_uID)

    def export_to_csv(self, path, absolute_path=None):
        if absolute_path is None:
            current_file = os.path.abspath(os.path.dirname(__file__))
            os_file_path = os.path.join(current_file, path)
            self.meal_df.to_csv(os_file_path, encoding='utf-8', index=False)
        else:
            self.meal_df.to_csv(path, encoding='utf-8', index=False)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=DEFAULT_MEAL_CSV_PATH)
    parser.add_argument('--csv', nargs='?', type=str, help="Please specify the path to the CSV-file containing the meal data.")
    args = parser.parse_args()

    normalizer = FoodNormalizer(args.csv)
    normalizer.assign_norm_titles()

    normalizer.export_to_csv('meal_norm_1.csv')

    # print(normalizer.meal_df.loc[0,'title_norm'])


    # titles = normalizer.meal_df.loc[:,'title']
    # titles_norm = normalizer.meal_df.loc[:,'title_norm']
    # lens = [len(title_comps) for title_comps in titles_norm]
    # for i, l in enumerate(lens):
    #     if l > 6:
    #         print(titles_norm[i])
    #         # print(titles[i])
    