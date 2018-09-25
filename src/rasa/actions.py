import requests, json
from rasa_core_sdk import Action
from rasa_core_sdk.forms import FormAction, BooleanFormField
# from rasa_core_sdk.events import SlotSet

import os, sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)


class ActionGetAllMeals(Action):
    def name(self):
        return 'action_get_all_meals'

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        time = tracker.get_slot("time")
        dispatcher.utter_message("Essen für <{}>:".format(time))

        res = requests.post('http://127.0.0.1:5000/getmeals', 
                            json={"time":time})

        try:
            dispatcher.utter_message(str(res.json()['msg']))
        except KeyError:
            dispatcher.utter_message("An error occured: <{}>".format(str(res.json()['error'])))
        
        return []


class ActionQueryRecommender(Action):
    def name(self):
        return 'action_query_recommender'

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        res = requests.post('http://127.0.0.1:5000/userexists', 
                            json={"user_id":str(user_id)})

        # dispatcher.utter_message(str(res.json()['user_exists']))
        if res.json()['user_exists'] == 1:
            time = tracker.get_slot("time")
            dispatcher.utter_message("Ein bestehendes Benutzerprofil wurde gefunden.")
            dispatcher.utter_message("Ein bestehendes Benutzerprofil wurde gefunden. Essen für <{}> nach persönlichen Präferenzen:".format(time))

            res2 = requests.post('http://127.0.0.1:5000/prediction', 
                                json={"user_id":str(user_id)})

            dispatcher.utter_message(res2.text)
        else:
            dispatcher.utter_message("Es wurde kein bestehendes Nutzerprofil gefunden. Soll ein persönliches Profil erstellt werden?")
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
        likes = [tracker.get_slot("like_q{}".format(i+1)) for i in range(5)]
        

        dispatcher.utter_message("Got likes <{}>".format(likes))
        return []
        
        # TODO: proper hand-over of user-q-likes to recommender to create profile

        # results = RestaurantAPI().search(
        #     tracker.get_slot("cuisine"),
        #     tracker.get_slot("people"),
        #     tracker.get_slot("vegetarian"))
        # return [SlotSet("search_results", results)]