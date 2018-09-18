import numpy as np
import pandas as pd

import os, sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from util.cloud_connection import bucket_connection

class Menu:

    def __init__(self, year=2018, week=38):
        self._year = year
        self._month = week
        self.df_menus = bucket_connection.get_menus(year, week)

    def get_food_per_day(self, substring):
        g = self.df_menus.groupby('date')
        for group_name in g.groups:
            if group_name.find(substring) > -1:
                return g.get_group(group_name)

if __name__ == "__main__":
    m = Menu()
    print(m.get_food_per_day('Montag'))