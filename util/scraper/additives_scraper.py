import json
import os
import sys

import requests
from bs4 import BeautifulSoup

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
from util.cloud_connection import bucket_connection


def scrape_additives():
    zusatzstoffe = requests.get(
        "https://www.studierendenwerk-kaiserslautern.de/kaiserslautern/essen-und-trinken/zusatzstoffe-und-hauptallergene/")
    soup = BeautifulSoup(zusatzstoffe.content, 'html.parser')

    add_data = {}
    table = soup.find('table', attrs={'class': 'full'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        cols = [ele.text.strip() for ele in cols]
        if len(cols) == 2:
            add_data[cols[0]] = cols[1]

    return add_data


def upload_additives(additives):
    with open('additives.json', 'w') as outfile:
        json.dump(additives, outfile)

    bucket_connection.get_meals()
    bucket_connection.upload_blob("mensa_data", "additives.json", "additives.json")


if __name__ == "__main__":
    data = scrape_additives()
    upload_additives(data)
