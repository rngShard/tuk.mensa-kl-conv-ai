import csv
import datetime
import os
import sys

import pandas as pd
import requests
from bs4 import BeautifulSoup

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_path)
from cloud_connection import firestore_connection, bucket_connection
from normalizer.food_title_normalizer import FoodNormalizer
from normalizer.id_matcher import IdMatcher

URL_MENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/mensa/"
URL_ATRIUM = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/cafeteria-atrium/"
URL_ABENDMENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/abendmensa/"

DB = firestore_connection.FirestoreConnector()


def get_data(url):
    html_mensa = requests.get(url)
    soup = BeautifulSoup(html_mensa.content, 'html.parser')
    dailyplan = soup.find_all("div", "dailyplan_content")
    return dailyplan


def parse_mensa_plan_csv(dailyplans, name):
    week_data = []
    for day in dailyplans:
        date = day.h5.string
        for location in day.find_all("div", "subcolumns"):
            if name == "mensa":
                location_name = location.find("div", "counter-name").strong.string
            elif name == "atrium":
                location_name = "atrium"
            for i, alternative in enumerate(location.find("div", "counter-meal").find_all("strong")):
                alternative_name = alternative.string
                # title_norm = FoodNormalizer.separate_food_title(alternative_name, True)
                # title_prim = title_norm[0][0]
                price_tag = alternative.next_sibling.next_sibling
                if price_tag.string is None:
                    alternative_price = price_tag.next_sibling.string
                else:
                    alternative_price = alternative.next_sibling.next_sibling.string
                if i == 1 and "atrium" not in location_name:
                    location_name = location_name + "veg"
                week_data.append([date, location_name, alternative_name, alternative_price])

    return week_data


def normalize_titles(current_meals_path, meals_path):
    current_meals = pd.read_csv(current_meals_path).values.tolist()
    meals = pd.read_csv(meals_path)
    last_index = meals.shape[0]
    next_id = meals.m_id.max() + 1
    with open(meals_path, 'a', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow("")
        for row in current_meals:
            row1 = row
            row1.insert(0, next_id)
            row1 = row1 + ["nan", "nan", "nan", "nan", "nan"]
            # row1 = str(next_id) + "," + ",".join(row) + ", nan, nan, nan, nan, nan" + "\n"
            writer.writerow(row1)
            next_id += 1
    # current_meals = pd.read_csv(meals_path)
    # current_meals = current_meals.iloc[last_index:]
    food_normalizer = FoodNormalizer(meals_path, True)
    food_normalizer.assign_norm_titles()
    export_to_csv(food_normalizer.meal_df.iloc[last_index:].drop("m_id", axis=1), current_meals_path, True)
    meals = pd.read_csv(meals_path)
    meals = meals.iloc[:last_index]
    export_to_csv(meals, meals_path, True)

    # food_normalizer.export_to_csv(meals_path, True)


def normalize_m_ids(csv_path, meal_path):
    id_matcher = IdMatcher(csv_path, meal_path)
    if "m_id" not in id_matcher.df_current.columns:
        id_matcher.match_ids()
    id_matcher.export_current_to_csv(absolute_path=True)
    id_matcher.export_meal_to_csv(absolute_path=True)


def save_as_csv(mensa_plan, name):
    bucket_connection.download_blob("mensa_data", "meal.csv", "./meal.csv")

    header = ["date", "loc", "title", "price"]
    mensa_data = pd.DataFrame(mensa_plan, dtype='str')
    if mensa_data.shape == (0, 0):
        print("No data available")
        return
    mensa_data.columns = header
    date = mensa_data.date[0].split(",")[1].split(".")
    calendar_week = datetime.datetime(int(date[2]), int(date[1]), int(date[0])).isocalendar()

    current_file = os.path.abspath(os.path.dirname(__file__))
    # csv_os_file_path = os.path.join(current_file, csv_path)
    meal_path = (os.path.join(current_file, "meal.csv"))
    if name == "mensa":
        file_name = str(calendar_week[0]) + "_" + str(calendar_week[1]) + ".csv"
        current_path = (os.path.join(current_file, "mensa/"))
        mensa_data.to_csv(current_path + file_name, index=False, quoting=csv.QUOTE_ALL)
        normalize_titles(current_path + file_name, meal_path)
        normalize_m_ids(current_path + file_name, meal_path)
        bucket_connection.upload_blob("mensa_data", current_path + file_name,
                                      "mensa/" + file_name)
    elif name == "atrium":
        file_name = str(calendar_week[0]) + "_" + str(calendar_week[1]) + "_" + str(calendar_week[2]) + ".csv"
        current_path = (os.path.join(current_file, "atrium/"))
        mensa_data.to_csv(current_path + file_name, index=False)
        # normalize_titles(current_path + file_name, meal_path)
        bucket_connection.upload_blob("mensa_data", current_path + file_name, "atrium/" + file_name)
    bucket_connection.upload_blob("mensa_data", meal_path, "meal.csv")

def title_norm2dict(title_list):
    title_norm = {}
    index = 0
    for i in title_list:
        if len(i) == 1:
            title_norm["title_norm" + str(index)] = {
                "title": i[0]
            }
        else:
            title_norm["title_norm" + str(index)] = {
                "title": i[0],
                "additives": i[1]
            }
        index += 1
    return title_norm


def parse_mensa_firestore(dailyplans, name):
    week_plan = []
    for dailyplan in dailyplans:
        date = dailyplan.h5.string
        date_list = date.split(", ")[1].split(".")
        year = date_list[2]
        month = date_list[1]
        day = date_list[0]
        day_plan = {}
        loc = {}
        counter_atrium = 1
        for location in dailyplan.find_all("div", "subcolumns"):
            if name == "mensa":
                location_name = location.find("div", "counter-name").strong.string
            elif name == "atrium":
                location_name = "atrium" + str(counter_atrium)
            for i, alternative in enumerate(location.find("div", "counter-meal").find_all("strong")):
                alternative_name = alternative.string
                titels_norm = FoodNormalizer.separate_food_title(alternative_name, True)
                titels_prim = titels_norm[0][0]
                titels_norm_dict = title_norm2dict(titels_norm)
                price_tag = alternative.next_sibling.next_sibling
                if price_tag.string is None:
                    alternative_price = price_tag.next_sibling.string
                else:
                    alternative_price = alternative.next_sibling.next_sibling.string
                if i == 1 and "atrium" not in location_name:
                    location_name = location_name + "veg"
                loc[location_name] = {
                    "loc": location_name,
                    "date_string": date,
                    "date": year + month + day,
                    "title": alternative_name,
                    "price": alternative_price,
                    "title_prim": titels_prim,
                    "title_norm": titels_norm_dict
                }
                counter_atrium += 1
            day_plan[year + month + day] = loc
        week_plan.append(day_plan)

    return week_plan


def save_mensa_firestore(mensa_plan, db=DB):
    for day in mensa_plan:
        for date, locations in day.items():
            year = date[:4]
            month = date[4:6]
            day = date[6:]
            week = str(datetime.datetime(int(year), int(month), int(day)).isocalendar()[1])
            for location, meal in locations.items():
                db.create_document("mensa/" + year + "/" + month + "/" + week + "/" + day + "/" + location, meal)


def export_to_csv(dataframe, path, absolute_path=None):
    if absolute_path is None:
        current_file = os.path.abspath(os.path.dirname(__file__))
        os_file_path = os.path.join(current_file, path)
        dataframe.to_csv(os_file_path, encoding='utf-8', index=False)
    else:
        dataframe.to_csv(path, encoding='utf-8', index=False)

def main():
    raw_data_mensa = get_data(URL_MENSA)
    raw_data_atrium = get_data(URL_ATRIUM)

    # Parsing Mensa Data

    # plan = parse_mensa_firestore(raw_data_mensa, "mensa")
    # save_mensa_firestore(plan)
    plan = parse_mensa_plan_csv(raw_data_mensa, "mensa")
    save_as_csv(plan, "mensa")

    # Parsing Atrium Data

    # plan = parse_mensa_firestore(raw_data_atrium, "atrium")
    # save_mensa_firestore(plan)
    # plan = parse_mensa_plan_csv(raw_data_atrium, "atrium")
    # save_as_csv(plan, "atrium")


if __name__ == "__main__":
    main()
