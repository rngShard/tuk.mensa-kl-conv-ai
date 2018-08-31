import csv
import datetime
import os
import sys

import pandas as pd
import requests
from bs4 import BeautifulSoup

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(parent_path)
from firestore_connection import connection

URL_MENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/mensa/"
URL_ATRIUM = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/cafeteria-atrium/"
URL_ABENDMENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/abendmensa/"

DB = connection.FirestoreConnector()

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
                price_tag = alternative.next_sibling.next_sibling
                if price_tag.string is None:
                    alternative_price = price_tag.next_sibling.string
                else:
                    alternative_price = alternative.next_sibling.next_sibling.string
                if i == 0:
                    week_data.append([date, location_name, alternative_name, alternative_price])
                elif i == 1:
                    week_data.append([date, location_name + "veg",
                                      alternative_name, alternative_price])
    return week_data


def save_as_csv(mensa_plan, name):
    header = ["date", "loc", "title", "price"]
    mensa_data = pd.DataFrame(mensa_plan, dtype='str')
    mensa_data.columns = header
    calener_week = datetime.datetime.today().isocalendar()
    if name == "mensa":
        mensa_data.to_csv("./mensa/" + str(calener_week[0]) + "_"
                          + str(calener_week[1]) + ".csv", index=False, quoting=csv.QUOTE_ALL)
    elif name == "atrium":
        mensa_data.to_csv("./atrium/" + str(calener_week[0]) + "_" + str(calener_week[1])
                          + "_" + str(calener_week[2]) + ".csv", index=False)


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
                price_tag = alternative.next_sibling.next_sibling
                if price_tag.string is None:
                    alternative_price = price_tag.next_sibling.string
                else:
                    alternative_price = alternative.next_sibling.next_sibling.string
                if i == 0:
                    loc[location_name] = {
                        "loc": location_name,
                        "date_string": date,
                        "date": year + month + day,
                        "meal": alternative_name,
                        "price": alternative_price
                    }
                elif i == 1 and not "atrium" in location_name:
                    loc[location_name + "veg"] = {
                        "loc": location_name + "veg",
                        "date_string": date,
                        "date": year + month + day,
                        "meal": alternative_name,
                        "price": alternative_price
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


def main():
    raw_data_mensa = get_data(URL_MENSA)
    raw_data_atrium = get_data(URL_ATRIUM)
    # Parsing Mensa Data
    plan = parse_mensa_firestore(raw_data_mensa, "mensa")
    save_mensa_firestore(plan)
    plan = parse_mensa_plan_csv(raw_data_mensa, "mensa")
    save_as_csv(plan, "mensa")

    # Parsing Atrium Data
    plan = parse_mensa_firestore(raw_data_atrium, "atrium")
    save_mensa_firestore(plan)
    plan = parse_mensa_plan_csv(raw_data_atrium, "atrium")
    save_as_csv(plan, "atrium")


if __name__ == "__main__":
    main()
