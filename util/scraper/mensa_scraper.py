import argparse
import csv
import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL_MENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/mensa/"
URL_ATRIUM = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/cafeteria-atrium/"
URL_ABENDMENSA = "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/tu-kaiserslautern/abendmensa/"


def get_data(url):
    html_mensa = requests.get(url)
    soup = BeautifulSoup(html_mensa.content, 'html.parser')
    dailyplan = soup.find_all("div", "dailyplan_content")
    return dailyplan


def parse_mensa_plan(dailyplans, name):
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


def main(url, name):
    raw_data = get_data(url)
    plan = parse_mensa_plan(raw_data, name)
    save_as_csv(plan, name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mensa", help="Please specify if you want to scrape 'mensa' or 'atrium'")
    args = parser.parse_args()

    if args.mensa == "mensa":
        main(URL_MENSA, "mensa")
    elif args.mensa == "atrium":
        main(URL_ATRIUM, "atrium")
    else:
        print("Please use 'mensa' or 'atrium' as attribute")
