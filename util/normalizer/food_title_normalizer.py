#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import pandas as pd
import os
import re

DEFAULT_MEAL_CSV_PATH = '../../data/meal.csv'

class FoodNormalizer:
    """Normalizing the provided meal-csv-data into consise, usable format."""

    def __init__(self, csv_path):
        current_file = os.path.abspath(os.path.dirname(__file__))
        csv_os_file_path =  os.path.join(current_file, csv_path)
        self.meal_csv_path = csv_os_file_path
        self.meal_df_original = pd.read_csv(csv_os_file_path)
        self.meal_df = pd.read_csv(csv_os_file_path)

    def separate_food_title(self, title):
        """Separate single string (food-title) into its food components."""

        re_title_delimiters = ', | mit | und |, dazu'
        title_split = re.split(re_title_delimiters, title)
        
        def separate_additives(component):
            """Given a component from the food-title-string, this returns a tuple of (component_str, additives_str)."""
            additives = re.search('\(\w{1,2}(,\w{1,2})*\)', component)
            additives = additives.group(0) if additives else ''
            ad_escaped = additives.replace('(', '\(').replace(')','\)')
            component = re.sub(ad_escaped, '', component) if additives else component 
            return (component.strip(), additives)
        title_split_components = [separate_additives(component) for component in title_split]
            
        return title_split_components

    def assign_norm_titles(self):
        titles = self.meal_df.title
        titels_norm = [self.separate_food_title(title) for title in titles]
        self.meal_df = self.meal_df.assign(title_norm=titels_norm)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=DEFAULT_MEAL_CSV_PATH)
    parser.add_argument('--csv', nargs='?', type=str, help="Please specify the path to the CSV-file containing the meal data.")
    args = parser.parse_args()

    normalizer = FoodNormalizer(args.csv)
    normalizer.assign_norm_titles()
    
    print normalizer.meal_df.head()
    