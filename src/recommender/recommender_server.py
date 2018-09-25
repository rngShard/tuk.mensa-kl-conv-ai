import datetime
import os
import sys

import flask
from flask import request, jsonify

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from src.recommender.recommender import Recommender
from src.recommender.data import clean_title_additives

WEEKDAYS = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag"
}

STR_WEEKDAYS_DE = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']

app = flask.Flask(__name__)
r = Recommender()


@app.route('/')
def index():
    pass


@app.route("/userexists", methods=['POST'])
def user_exists():
    data = request.get_json()
    print(data)
    user_id = data["user_id"]
    if r.users.user_exists(user_id):
        exists = 1
    else:
        exists = 0
    return jsonify({"user_exists": exists})


@app.route("/prediction", methods=['POST'])
def predict():
    data = request.get_json()
    user_id = data["user_id"]
    try:
        day = data["day"]
    except KeyError:
        day = r.day
    recommendation = r.predict(str(user_id), day=day)
    menu = r.menu.get_food_per_day(WEEKDAYS[day])
    recommendation = [(menu.title.values[i], recommendation[i][1]) for i in range(len(recommendation))]
    recommendation = sorted(recommendation, key=lambda x: x[1], reverse=True)
    predictions = []
    for prediction in recommendation:
        predictions.append(clean_title_additives(prediction[0]))
    answer = {}
    answer["prediction"] = predictions
    return jsonify(answer)


@app.route("/getmeals", methods=['POST'])
def get_meals():
    data = request.get_json()
    time = data["time"]
    if time == 'heute':
        today_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()]
        return jsonify({'msg': str(r.menu.get_food_per_day(today_weekday).loc[:,'title'].tolist()) })
    elif time == 'morgen':
        tomorrow_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()+1]
        return jsonify({'msg': str(r.menu.get_food_per_day(tomorrow_weekday).loc[:,'title'].tolist()) })
    elif time == 'woche':
        return jsonify({'msg': str(r.menu.df_menus.loc[:,'title'].tolist()) })
    else:
        return jsonify({'error':"Invalid value for attribute <time>."})


@app.route("/createuser", methods=['POST'])
def create_user():
    data = request.get_json()





if __name__ == "__main__":
    # with open('config.json', 'r') as f:
    #    config = json.load(f)
    app.run()
