# coding=utf-8

import requests, json
from rasa_core_sdk import Action
from rasa_core_sdk.forms import FormAction, BooleanFormField
# from rasa_core_sdk.events import SlotSet

import os, sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)


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
                    msg_profile = "Ein bestehendes Benutzerprofil wurde gefunden."

                    res2 = requests.post('http://127.0.0.1:5000/prediction', json={"user_id":str(user_id)})
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
        res = requests.post('http://127.0.0.1:5000/createuser', json=json)
        
        dispatcher.utter_message("Neues User-Profil mit Bewertungen {} erstellt!".format(json['ratings']))
        return []
        