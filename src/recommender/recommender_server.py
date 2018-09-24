import datetime
import operator
import os
import sys

import flask
from flask import request, jsonify

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

from src.recommender.recommender import Recommender

STR_WEEKDAYS_DE = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']

app = flask.Flask(__name__)
r = Recommender()


@app.route('/')
def index():
    pass


@app.route("/userexists", methods=['GET', 'POST'])
def user_exists():
    data = request.get_json()
    print(data)
    user_id = data["user_id"]
    if r.users.user_exists(user_id):
        exists = 1
    else:
        exists = 0
    return jsonify({"user_exists": exists})


@app.route("/prediction", methods=['GET', 'POST'])
def predict():
    data = request.get_json()
    user_id = data["user_id"]
    try:
        day = data["day"]
    except KeyError:
        day = 0

    predictions = r.predict(user_id, day=day)
    recommendation = []
    sorted_predictions = sorted(predictions.items(), key=operator.itemgetter(1), reverse=True)
    for prediction in sorted_predictions:
        recommendation.append(r.data.get_meal_title_without_additives(prediction[0]))
    answer = {}
    answer["prediction"] = recommendation
    return jsonify(answer)

@app.route("/getmeals", methods=['GET','POST'])
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




if __name__ == "__main__":
    # with open('config.json', 'r') as f:
    #    config = json.load(f)
    app.run()
