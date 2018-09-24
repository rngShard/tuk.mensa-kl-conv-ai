import requests, json
from rasa_core_sdk import Action
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
        dispatcher.utter_message("Aktuelles Essen <{}>:".format(time))


        res = requests.post('http://127.0.0.1:5000/getmeals', 
                            json={"time":time})

        dispatcher.utter_message(str(res.json()['msg']))
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
            dispatcher.utter_message("Ein bestehendes Benutzerprofil wurde gefunden.")
        else:
            dispatcher.utter_message("Es wurde kein bestehendes Nutzerprofil gefunden. Soll ein persönliches Profil erstellt werden?")
        return []