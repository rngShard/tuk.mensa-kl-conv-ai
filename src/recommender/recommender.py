import os
import sys

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from src.recommender.cluster import Cluster
from src.recommender.data import Data
from src.recommender.menu import Menu
from src.recommender.users import Users
from src.recommender.similarities import Similarities
from src.recommender.prediction import predict_rating, predict_cluster

WEEKDAYS = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag"
}


class Recommender:

    def __init__(self):
        cluster = self.cluster = Cluster()
        self.data = Data()
        self.similarities = Similarities(self.data.df_initial_user_item)
        self.users = Users(self.data.df_initial_user_item.columns)

        self.build_user_data_startup()

        self.year, self.week, self.day = self._get_year_week_day()
        self.menu = Menu(self.year, self.week)

    def build_user_data_startup(self):
        for user_id in self.users.user_ids:
            self.data._create_user_item(self.users.get_user_ratings(user_id))
            self.similarities.create_usr_usr_sim(self.data.get_user_item(user_id), user_id)

    def _get_year_week_day(self):
        import datetime
        now = datetime.datetime.now()
        week = datetime.datetime(int(now.year), int(now.month), int(now.day)).isocalendar()[1]
        day = datetime.datetime(int(now.year), int(now.month), int(now.day)).isocalendar()[2]
        return now.year, week, day

    def predict(self, current_user, metric="cosine", m_id=None, day=0, cluster=False):

        if cluster:
            user_cluster = self.cluster.predict_cluster(self.users.get_user_ratings(current_user))
            print(user_cluster)
            cluster_neighbors = self.cluster.get_neighbbors(user_cluster)
            predictions = {}
            if day is 0:
                if self.day is 6 or self.day is 7:
                    day = WEEKDAYS[1]
            else:
                day = WEEKDAYS[self.day]
            df_user_item = self.data.get_user_item(current_user)
            if m_id is None:
                m_ids = self.menu.get_meal_ids_per_day(day)
                for meal in m_ids:
                    predictions[meal] = predict_cluster(current_user, df_user_item, cluster_neighbors, meal)
            else:
                predictions[m_id] = predict_cluster(current_user, df_user_item, cluster_neighbors, m_id)

            return predictions

        else:
            predictions = {}
            if day is None:
                if self.day is 6 or self.day is 7:
                    day = WEEKDAYS[1]
            else:
                day = WEEKDAYS[self.day]
            df_similarity = self.similarities.get_user_similarity(current_user, metric)
            sim_users = self.similarities.get_similar_users(current_user, metric)
            df_user_item = self.data.get_user_item(current_user)
            df_meals = self.data.get_meals()
            if m_id is None:
                m_ids = self.menu.get_meal_ids_per_day(day)
                for meal in m_ids:
                    predictions[meal] = predict_rating(current_user, df_similarity, df_user_item, df_meals, sim_users,
                                                       meal)
            else:
                predictions[m_id] = predict_rating(current_user, df_similarity, df_user_item, df_meals, sim_users, m_id)

            return predictions


if __name__ == "__main__":
    r = Recommender()
    print(r.predict(54))
    print(r.predict(54, m_id=115))
    print(r.predict(55, m_id=493))

    # r = Recommender(cluster=True)
    # print(r.predict(55, m_id=601))
    # print(r.predict(56))

    # print(str(r.menu.get_food_per_day('Freitag').loc[:, 'title'].tolist()))
    # print(r.users.ratings)
