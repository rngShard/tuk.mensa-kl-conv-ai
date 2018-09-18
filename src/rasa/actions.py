from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet

import os, sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_path)



class ActionDisplayMeals(Action):
    def name(self):
        return 'action_display_meals'

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        dispatcher.utter_message("Suche aktuelles Essen ({}):".format(tracker.get_slot("time")))

        # TODO replace with api calling instead of instanciating
        #
        import datetime
        STR_WEEKDAYS_DE = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
        from src.recommender.recommender import Recommender
        r = Recommender()

        if tracker.get_slot("time") == 'heute':
            today_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()]
            dispatcher.utter_message( str(r.menu.get_food_per_day(today_weekday).loc[:,'title'].tolist()) )
        elif tracker.get_slot("time") == 'morgen':
            tomorrow_weekday = STR_WEEKDAYS_DE[datetime.datetime.now().weekday()]
            dispatcher.utter_message( str(r.menu.get_food_per_day(tomorrow_weekday).loc[:,'title'].tolist()) )
        elif tracker.get_slot("time") == 'woche':
            dispatcher.utter_message( str(r.menu.df_menus.loc[:,'title'].tolist()) )


        return []