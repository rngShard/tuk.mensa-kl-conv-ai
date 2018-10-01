# coding=utf-8
import datetime
import json
import os
import sys

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction, BooleanFormField

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)

WEEKDAYS = {
    "montag": 1,
    "dienstag": 2,
    "mittwoch": 3,
    "donnerstag": 4,
    "freitag": 5
}


def get_day(time):
    current_day = datetime.datetime.now().weekday() + 1
    if time == "heute":
        return current_day
    elif time == "morgen":
        if current_day == 7:
            current_day = 1
        else:
            current_day += 1
        return current_day
    elif time == "woche":
        return 8
    else:
        return WEEKDAYS[time]


class action_check_profile(Action):
    def name(self):
        return "action_check_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        res = requests.post('http://127.0.0.1:5000/userexists', json={"user_id": str(user_id)})
        if res.json()['user_exists'] == 1:
            return [SlotSet("user_exists", True)]
        else:
            return [SlotSet("user_exists", False)]


class action_check_user_wants_profile(Action):
    def name(self):
        return "action_check_user_wants_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        res = requests.post('http://127.0.0.1:5000/usernoprofile', json={"user_id": str(user_id)})
        if res.json()['no_profile'] == 1:
            return [SlotSet("wants_no_profile", True)]
        else:
            return [SlotSet("wants_no_profile", False)]


class set_user_wants_no_profile(Action):
    def name(self):
        return "action_set_user_wants_no_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        requests.post('http://127.0.0.1:5000/setusernoprofile', json={"user_id": str(user_id)})
        return []


class set_user_wants_profile(Action):
    def name(self):
        return "action_set_user_wants_profile"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        requests.post('http://127.0.0.1:5000/setuserprofile', json={"user_id": str(user_id)})
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
        print("DAy:" + str(day))
        res = requests.post('http://127.0.0.1:5000/prediction', json={"user_id":str(user_id), "day":day})
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
        res = requests.post('http://127.0.0.1:5000/getmeals', json={"day": day})
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


class ActionGetMeals(Action):
    def name(self):
        return 'action_get_meals'

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        user_id = tracker.sender_id
        time = tracker.get_slot("time")
        if not time:
            dispatcher.utter_message("Es ist kein Zeit-Attribut (heute/morgen/woche) gesetzt. Für wann soll Essen erfragt werden?")
        else:
            try:
                msg_time = "Essen für <{}>.".format(time)

                res = requests.post('http://127.0.0.1:5000/userexists', json={"user_id":str(user_id)})
                if res.json()['user_exists'] == 1:
                    day = get_day(time)
                    if day == 6 or day == 7:
                        dispatcher.utter_message("Heute gibt es nichts zu essen.")
                        return []

                    msg_profile = "Ein bestehendes Benutzerprofil wurde gefunden."

                    res2 = requests.post('http://127.0.0.1:5000/prediction', json={"user_id":str(user_id), "day": day})
                    res2_dict = json.loads(res2.text)

                    res2_meal_list = res2_dict['prediction']
                else:
                    msg_profile = "Es wurde kein bestehendes Nutzerprofil gefunden."

                    res2 = requests.post('http://127.0.0.1:5000/getmeals', json={"time":time})
                    res2_dict = json.loads(res2.text)

                    res2_meal_list = res2_dict['msg']

                utter_msg = "({} \t {})".format(msg_time, msg_profile)
                for meal in res2_meal_list:
                    utter_msg += "\n - " + meal
                dispatcher.utter_message(utter_msg)
            except KeyError:
                # pass
                dispatcher.utter_message("An error occured: <{}>".format(str(res.json()['error'])))
            
            return []

class ActionAskSpecificQuestions(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            BooleanFormField("like_q1", "affirm", "deny"),
            BooleanFormField("like_q2", "affirm", "deny"),
            BooleanFormField("like_q3", "affirm", "deny"),
            BooleanFormField("like_q4", "affirm", "deny"),
            BooleanFormField("like_q5", "affirm", "deny")
        ]

    def name(self):
        return 'action_ask_specific_questions'

    def submit(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        likes = [tracker.get_slot("like_q{}".format(i+1)) for i in range(5)]
        
        json = {
            "user_id": str(user_id),
            "ratings": [5 if like else 1 for like in likes]
        }
        print(json)
        requests.post('http://127.0.0.1:5000/createuser', json=json)
        
        dispatcher.utter_message("Neues User-Profil mit Bewertungen {} erstellt! Von nun an kannst du Empfehlungen von mir bekommen!".format(json['ratings']))
        return []

