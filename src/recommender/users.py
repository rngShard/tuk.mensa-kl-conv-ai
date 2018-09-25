import os
import sys

import numpy as np
import pandas as pd
from google.api_core.exceptions import NotFound

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from util.cloud_connection.firestore_connection import FirestoreConnector


class Users:

    def __init__(self, meal_ids):
        self.meal_ids = meal_ids
        self.firebase = FirestoreConnector()
        self.db_user_path = "users"
        self.users = {}
        self.user_ids = []
        self.ratings = {}
        self.additives = {}
        self.get_all_users()
        self.prepare_user_ratings()
        self.prepare_user_additives()

    def user_exists(self, user_id):
        try:
            user = self.firebase.get_document(self.db_user_path + "/" + user_id)
            return True
        except NotFound:
            return False

    def create_user(self, user_id=None):
        if user_id is None:
            user_id = self.get_new_user_id()
        data = {"user_id": user_id, "ratings": {}, "additives": []}
        self.firebase.create_document(self.db_user_path + "/" + user_id, data)
        return user_id

    def get_all_users(self):
        doc_ref = self.firebase.db.collection(self.db_user_path)
        users = doc_ref.get()
        for user in users:
            self.users[user.id] = user.to_dict()
            self.user_ids.append(user.id)

    def prepare_user_ratings(self):
        for user in self.user_ids:
            user_ratings = self.users[user]["ratings"]
            ratings_row = np.zeros(len(self.meal_ids))
            ratings_series = pd.Series(ratings_row, self.meal_ids, name=user)
            for k, v in user_ratings.items():
                ratings_series.loc[int(k)] = v
            self.ratings[user] = ratings_series

    def prepare_new_user_ratings(self, user_id):
        ratings_row = np.zeros(len(self.meal_ids))
        ratings_series = pd.Series(ratings_row, self.meal_ids, name=user_id)
        self.ratings[user_id] = ratings_series

    def prepare_user_additives(self):
        for user in self.user_ids:
            user_additives = set(self.users[user]["additives"])
            self.additives[user] = user_additives

    def update_rating(self, user_id, m_id, rating):
        self.firebase.update_rating(user_id, m_id, rating)
        self.ratings[user_id].loc[m_id] = rating

    def get_user_ratings(self, user_id):
        return self.ratings[user_id]

    def get_user_additives(self, user_id):
        return self.additives[user_id]

    def get_new_user_id(self):
        return max(self.user_ids) + 1


if __name__ == "__main__":
    users = Users(
        [57, 115, 135, 160, 166, 167, 174, 192, 204, 210, 212, 219, 224, 236, 241, 242, 249, 263, 289, 302, 303, 315,
         316, 323, 342, 344, 352, 353, 358, 359, 360, 364, 370, 372, 375, 376, 379, 380, 390, 395, 401, 403, 404, 410,
         417, 420, 423, 431, 432, 444, 447, 449, 450, 453, 456, 457, 458, 459, 462, 464, 466, 469, 471, 474, 475, 476,
         483, 485, 489, 492, 493, 494, 495, 498, 499, 504, 507, 510, 515, 520, 521, 523, 524, 527, 530, 532, 533, 534,
         535, 536, 538, 539, 543, 545, 546, 548, 549, 550, 551, 554, 555, 556, 558, 563, 566, 567, 568, 570, 571, 573,
         579, 580, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600,
         601])
    print(users.get_new_user_id())
    print(users.get_user_additives(56))

# doc_ref = self.db.db.collection(self.db_user_path)
# user = doc_ref.where("fid", "==", "1324").get()
# user = [(i.id, i.to_dict()) for i in user]
# print(user)
