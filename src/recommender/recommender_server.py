import os
import sys

import flask
from flask import request, jsonify

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)
sys.path.append("~/tuk.mensa-kl-conv-ai/src/recommender.recommender")
from src.recommender.recommender import Recommender
from src.recommender.data import clean_title_additives, get_meal_title_additives

WEEKDAYS = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag",
    6: "Samstag",
    7: "Sonntag"
}

STR_WEEKDAYS_DE = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

app = flask.Flask(__name__)
r = Recommender()


@app.route('/')
def index():
    pass


@app.route("/userexists", methods=['POST'])
def user_exists():
    data = request.get_json()
    user_id = data["user_id"]
    if r.users.user_exists(user_id):
        exists = 1
    else:
        exists = 0
    print("User exists: " + str(exists))
    return jsonify({"user_exists": exists})


@app.route("/usernoprofile", methods=["POST"])
def user_wants_no_profile():
    data = request.get_json()
    user_id = data["user_id"]
    if r.users.wants_no_profile(user_id):
        no_profile = 1
    else:
        no_profile = 0
    print("User wants no profile: " + str(no_profile))
    return jsonify({"no_profile": no_profile})


@app.route("/setuserprofile", methods=["POST"])
def set_user_profile():
    data = request.get_json()
    user_id = data["user_id"]
    r.users.set_wants_profile(user_id)
    return "Set user wants profile"


@app.route("/setusernoprofile", methods=["POST"])
def set_user_no_profile():
    data = request.get_json()
    user_id = data["user_id"]
    r.users.set_wants_no_profile(user_id)
    return "Set user wants no profile"


@app.route("/prediction", methods=['POST'])
def predict():
    week = False
    data = request.get_json()
    user_id = data["user_id"]
    try:
        day = data["day"]
        if day == 8:
            day = [1, 2, 3, 4, 5]
            week = True
    except KeyError:
        day = r.day
    if not week:
        predictions = []
        locations = []
        recommendation = r.predict(str(user_id), day=day)
        menu = r.menu.get_food_per_day(WEEKDAYS[day])
        if menu is None:
            predictions = []
        else:
            recommendation = [(menu.title.values[i], recommendation[i][1], menu["loc"].values[i]) for i in
                              range(len(recommendation))]
            recommendation = sorted(recommendation, key=lambda x: x[1], reverse=True)
            filtered_recommendation = []
            for meal in recommendation:
                if not r.filter_additives(user_id, get_meal_title_additives(meal[0])):
                    filtered_recommendation.append(meal)
            # current_day = []
            # for prediction in recommendation:
            #    current_day.append(clean_title_additives(prediction[0]))
            if filtered_recommendation != []:
                predictions.append([clean_title_additives(filtered_recommendation[0][0])])
                locations.append([filtered_recommendation[0][2]])

        answer = {}
        answer["locations"] = locations
        answer["meals"] = predictions
        answer["day"] = day
        return jsonify(answer)
    else:
        predictions = []
        locations = []
        days = []
        for d in day:
            current_day = []
            recommendation = r.predict(str(user_id), day=d)
            menu = r.menu.get_food_per_day(WEEKDAYS[d])
            if menu is None:
                continue
            else:
                recommendation = [(menu.title.values[i], recommendation[i][1], menu["loc"].values[i]) for i in
                                  range(len(recommendation))]
                recommendation = sorted(recommendation, key=lambda x: x[1], reverse=True)
                filtered_recommendation = []
                for meal in recommendation:
                    if not r.filter_additives(user_id, get_meal_title_additives(meal[0])):
                        filtered_recommendation.append(meal)
                if filtered_recommendation != []:
                    current_day.append(clean_title_additives(filtered_recommendation[0][0]))
                    locations.append([filtered_recommendation[0][2]])
                # for prediction in recommendation:
                #    current_day.append(clean_title_additives(prediction[0]))
                days.append(d)
            predictions.append(current_day)
            answer = {}
            answer["locations"] = locations
            answer["meals"] = predictions
            answer["day"] = days
        return jsonify(answer)


@app.route("/addrating", methods=["POST"])
def add_rating():
    data = request.get_json()
    user_id = data["user_id"]
    m_id = data["m_id"]
    rating = data["rating"]
    r.users.update_rating(user_id, m_id, rating)
    r.update_user_specific_data(user_id)
    return "Rating added!"


@app.route("/addadditives", methods=["POST"])
def add_additives():
    data = request.get_json()
    user_id = data["user_id"]
    additives = data["additives"]
    for additive in additives:
        r.users.update_user_additives(user_id, additive)
    return "Additives added!"


@app.route("/getmeals", methods=["POST"])
def get_meals():
    week = False
    data = request.get_json()
    try:
        day = data["day"]
        if day == 8:
            week = True
    except KeyError:
        day = r.day
    if week:
        menu = r.menu.df_menus.loc[:, 'title'].tolist()
        locs = r.menu.df_menus["loc"].values
    else:
        try:
            menu = r.menu.get_food_per_day(WEEKDAYS[day]).loc[:, "title"]
            locs = r.menu.get_food_per_day(WEEKDAYS[day])["loc"].values
        except AttributeError:
            menu = []
    meals = []
    locations = []
    for k, meal in enumerate(menu):
        meals.append([clean_title_additives(meal)])
        locations.append([locs[k]])
    answer = {}
    answer["locations"] = locations
    answer["meals"] = meals
    answer["day"] = day
    return jsonify(answer)


# @app.route("/getmeals", methods=['POST'])
# def get_meals():
#     data = request.get_json()
#     time = data["day"]
#     if time == 'heute':
#         today_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()]
#         return jsonify({'msg': r.menu.get_food_per_day(today_weekday).loc[:, 'title'].tolist()})
#     elif time == 'morgen':
#         tomorrow_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()+1]
#         return jsonify({'msg': r.menu.get_food_per_day(tomorrow_weekday).loc[:, 'title'].tolist()})
#     elif time == 'woche':
#         return jsonify({'msg': r.menu.df_menus.loc[:, 'title'].tolist()})
#     else:
#         return jsonify({'error': "Invalid value for attribute <time>."})


@app.route("/createuser", methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data["user_id"]
    user_ratings = data["ratings"]
    decision_points = r.cluster.get_decision_points()

    r.users.create_user(user_id)
    r.build_user_specific_data(user_id)

    for i in range(len(decision_points)):
        r.users.update_rating(user_id, decision_points[i], user_ratings[i])
    r.update_user_specific_data(user_id)

    return "User created!"


if __name__ == "__main__":
    # with open('config.json', 'r') as f:
    #    config = json.load(f)
    app.run(host='0.0.0.0', port='6000')

