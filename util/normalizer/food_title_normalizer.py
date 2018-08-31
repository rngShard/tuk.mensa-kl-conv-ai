#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import pandas as pd
import os
import re

DEFAULT_MEAL_CSV_PATH = '../../data/meal_manually_cleaned.csv'

class FoodNormalizer:
    """Normalizing the provided meal-csv-data into consise, usable format."""

    def __init__(self, csv_path):
        current_file = os.path.abspath(os.path.dirname(__file__))
        csv_os_file_path = os.path.join(current_file, csv_path)
        self.meal_csv_path = csv_os_file_path
        self.meal_df_original = pd.read_csv(csv_os_file_path)
        self.meal_df = pd.read_csv(csv_os_file_path)

    @staticmethod
    def separate_food_title(title):
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
            return [component, additives] if additives else [component]
        title_split_components = [separate_additives(component) for component in title_split]
            
        return title_split_components

    def assign_norm_titles(self):
        titles = self.meal_df.title
        titels_norm = [FoodNormalizer.separate_food_title(title) for title in titles]
        titels_prim = [title[0][0] for title in titels_norm]
        self.meal_df = self.meal_df.assign(title_prim=titels_prim)
        self.meal_df = self.meal_df.assign(title_norm=titels_norm)

    def export_to_csv(self, path):
        current_file = os.path.abspath(os.path.dirname(__file__))
        os_file_path =  os.path.join(current_file, path)
        self.meal_df.to_csv(os_file_path, encoding='utf-8', index=False)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=DEFAULT_MEAL_CSV_PATH)
    parser.add_argument('--csv', nargs='?', type=str, help="Please specify the path to the CSV-file containing the meal data.")
    args = parser.parse_args()

    normalizer = FoodNormalizer(args.csv)
    normalizer.assign_norm_titles()
    normalizer.export_to_csv('test_norm_meal.csv')

    # print normalizer.meal_df.head()
    