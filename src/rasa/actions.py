# coding=utf-8
import datetime
import json
import os
import sys

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

WEEKDAYS = {
    "montag": 1,
    "Montag": 1,
    "dienstag": 2,
    "Dienstag": 2,
    "mittwoch": 3,
    "Mittwoch": 3,
    "donnerstag": 4,
    "Donnerstag": 4,
    "freitag": 5,
    "Freitag": 5,
    "samstag": 6,
    "Samstag": 6,
    "sonntag": 7,
    "Sonntag": 7,
    "woche": 8,
    "Woche": 8
}

VALID_RATINGS = (0, 1, 2, 3, 4, 5)


def get_day(time):
    time = time.lower()
    current_day = datetime.datetime.now().weekday() + 1
    if time == "heute":
        return current_day
    elif time == "morgen":
        if current_day == 7:
            current_day = 1
        else:
            current_day += 1
        return current_day
    # elif time == "woche":
    #    return 8
    else:
        return WEEKDAYS[time]


class action_get_user_id(Action):
    def name(self):
        return "action_get_user_id"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        dispatcher.utter_message("{}".format(user_id))


class action_check_profile(Action):
    def name(self):
        return "action_check_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        res = requests.post('http://127.0.0.1:6000/userexists', json={"user_id": str(user_id)})
        if res.json()['user_exists'] == 1:
            return [SlotSet("user_exists", True)]
        else:
            return [SlotSet("user_exists", False)]


class action_check_user_wants_profile(Action):
    def name(self):
        return "action_check_user_wants_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        res = requests.post('http://127.0.0.1:6000/usernoprofile', json={"user_id": str(user_id)})
        if res.json()['no_profile'] == 1:
            return [SlotSet("wants_no_profile", True)]
        else:
            return [SlotSet("wants_no_profile", False)]


class set_user_wants_no_profile(Action):
    def name(self):
        return "action_set_user_wants_no_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        requests.post('http://127.0.0.1:6000/setusernoprofile', json={"user_id": str(user_id)})
        return []


class set_user_wants_profile(Action):
    def name(self):
        return "action_set_user_wants_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        requests.post('http://127.0.0.1:6000/setuserprofile', json={"user_id": str(user_id)})
        return []


class action_predict_meals_after_registration(Action):
    def name(self):
        return "action_predict_meals_after_registration"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        time = tracker.get_slot("time")
        if not time:
            dispatcher.utter_message("Es ist kein Zeit-Attribut (heute/morgen/woche) gesetzt. "
                                     "Für wann soll Essen erfragt werden?")
            return []

        day = get_day(time)
        if day == 6 or day == 7:
            dispatcher.utter_message("Heute gibt es nichts zu essen.")
            return []
        res = requests.post('http://127.0.0.1:6000/prediction', json={"user_id":str(user_id), "day":day})
        res_dict = json.loads(res.text)
        meals = res_dict["meals"]
        no_meals = True
        if day != 0 and meals == []:
            answer = "Für diesen Tag kann ich dir leider nichts empfehlen."
        else:
            answer = "Meine Empfehlung für {}:".format(time)
            for meal in meals:
                if meal != []:
                    answer += "\n - " + meal[0]
                    no_meals = False
        if not no_meals:
            dispatcher.utter_message(answer)
        else:
            dispatcher.utter_message("Ich kann dir leider nichts empfehlen, es wurden keine Essen gefunden.")
        return []


class action_meals_without_registration(Action):
    def name(self):
        return "action_meals_without_registration"

    def run(self, dispatcher, tracker, domain):
        time = tracker.get_slot("time")
        if not time:
            dispatcher.utter_message(
                "Es ist kein Zeit-Attribut (heute/morgen) gesetzt. Für wann soll Essen erfragt werden?")
            return []
        day = get_day(time)
        if day == 8:
            dispatcher.utter_message("Wenn du nicht registriert bist, kann ich dir keine Wochenübersicht ausgeben.")
            return []
        if day == 6 or day == 7:
            dispatcher.utter_message("Heute gibt es nichts zu essen.")
            return []
        print("DAy:" + str(day))
        res = requests.post('http://127.0.0.1:6000/getmeals', json={"day": day})
        res_dict = json.loads(res.text)
        meals = res_dict["meals"]
        print(meals)
        if day != 0 and meals == []:
            answer = "An diesem Tag gibt es nichts zu essen."
        else:
            answer = "Meine Empfehlung für {}:".format(time)
            for meal in meals:
                answer += "\n - " + meal[0]
        dispatcher.utter_message(answer)
        return []


class ActionSetQ1(Action):
    def name(self):
        return "action_set_q1"

    def run(self, dispatcher, tracker, domain):
        q1 = tracker.get_slot("answer")
        return [SlotSet("like_q1", q1)]


class ActionSetQ2(Action):
    def name(self):
        return "action_set_q2"

    def run(self, dispatcher, tracker, domain):
        q2 = tracker.get_slot("answer")
        return [SlotSet("like_q2", q2)]


class ActionSetQ3(Action):
    def name(self):
        return "action_set_q3"

    def run(self, dispatcher, tracker, domain):
        q3 = tracker.get_slot("answer")
        return [SlotSet("like_q3", q3)]


class ActionSetQ4(Action):
    def name(self):
        return "action_set_q4"

    def run(self, dispatcher, tracker, domain):
        q4 = tracker.get_slot("answer")
        return [SlotSet("like_q4", q4)]


class ActionSetQ5(Action):
    def name(self):
        return "action_set_q5"

    def run(self, dispatcher, tracker, domain):
        q5 = tracker.get_slot("answer")
        return [SlotSet("like_q5", q5)]


class ActionCreateProfile(Action):
    def name(self):
        return "action_create_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        # likes = [tracker.get_slot("like_q{}".format(i+1)) for i in range(5)]
        ratings = []
        for i in range(5):
            rating = int(tracker.get_slot("like_q{}".format(i + 1)))
            if rating in VALID_RATINGS:
                ratings.append(rating)
            else:
                msg = "Bitte achte darauf, die Gerichte nur mit 0-5 zu bewerten." \
                      " Probiere noch einmal ein Profil zu erstellen!"
                dispatcher.utter_message(msg)
                return []
        json = {
            "user_id": str(user_id),
            "ratings": ratings
            # "ratings": [5 if like else 1 for like in likes]
        }
        print(json)
        requests.post('http://127.0.0.1:6000/createuser', json=json)

        msg = "Neues User-Profil mit Bewertungen {} erstellt! Von nun an bekommst du persönliche Empfehlungen!".format(
            json['ratings'])
        dispatcher.utter_message(msg)
        return []


class ActionVegetarisch(Action):
    def name(self):
        return "action_vegetarisch"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["V"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []


class ActionVegan(Action):
    def name(self):
        return "action_vegan"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["V+"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []


class ActionLaktose(Action):
    def name(self):
        return "action_laktose"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["La"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []


class ActionSchwein(Action):
    def name(self):
        return "action_schwein"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["S"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []


class ActionRind(Action):
    def name(self):
        return "action_rind"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["R"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []


class ActionFisch(Action):
    def name(self):
        return "action_fisch"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        additive = ["Fi"]
        requests.post('http://127.0.0.1:6000/addadditives', json={"user_id": str(user_id),
                                                                  "additives": additive})
        return []
