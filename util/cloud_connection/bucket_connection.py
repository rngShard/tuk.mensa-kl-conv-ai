import os
import sys

import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
from definitions import ROOT_DIR

current_file = os.path.abspath(os.path.dirname(__file__))

CRED = service_account.Credentials.from_service_account_file(
    (os.path.join(current_file, "tuk-mensa-kl-conv-ai-storage-buckets.json")))


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client(credentials=CRED, project="tuk-mensa-kl-conv-ai")
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client(credentials=CRED, project="tuk-mensa-kl-conv-ai")
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def get_meals():
    """

    :return: Returns a Pandas Dataframe with the current meal data
    """
    tmp_path = ROOT_DIR + "/meal_tmp.csv"
    download_blob("mensa_data", "meal.csv", tmp_path)
    df_meal = pd.read_csv(tmp_path)
    os.remove(tmp_path)
    return df_meal


def get_menus(year, week):
    tmp_path = ROOT_DIR + "/menues_tmp.csv"
    source_blob_name = "mensa/{}_{}.csv".format(year, week)
    download_blob("mensa_data", source_blob_name, tmp_path)
    df_meal = pd.read_csv(tmp_path)
    os.remove(tmp_path)
    return df_meal
