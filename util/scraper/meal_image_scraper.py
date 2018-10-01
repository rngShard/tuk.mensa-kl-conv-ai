import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys, os

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
from util.cloud_connection import bucket_connection

PAGE_URL = "http://www.mensa-kl.de"

def scrape_images():
    res = requests.get(PAGE_URL)
    soup = BeautifulSoup(res.content, 'html.parser')

    futter_paragraphs = soup.find_all('div', attrs={'class': 'futter'})

    def write_to_file(img_src):
        res = requests.get(img_src, stream=True)
        path = 'data/imgs/'+title+'.jpg'
        with open(path, 'wb') as f:
            for chunk in res:
                f.write(chunk)
        return path
    
    def persist_to_bucket(file_path, bucket_dir):
        bucket_dir = bucket_dir.replace(' ', '')
        bucket_connection.upload_blob('mensa_data', file_path, bucket_dir)
        pass

    for div in futter_paragraphs:
        all_p = div.find_all('p')

        location = all_p[0].string.strip()
        if location not in ['Ausgabe 1', 'Ausgabe 1 (veg.)', 'Ausgabe 2', 'Ausgabe 2 (veg.)', 'Wok', 'Grill']:
            continue

        title = all_p[1].contents[0].strip()
        
        img_src = PAGE_URL + div.img['src'][1:]

        if div.img['src'] != "./img/qm.png":    
            path = write_to_file(img_src)

            print("Wrote <{}> to <{}>".format(img_src, path))

            now = datetime.now()
            calendar_week = datetime(int(now.year), int(now.month), int(now.day)).isocalendar()[1]
            bucket_dir = 'mensa/{}_{}/{}'.format(now.year, calendar_week, title)

            persist_to_bucket(path, bucket_dir)



if __name__ == '__main__':
    scrape_images()