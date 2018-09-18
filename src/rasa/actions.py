from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet
### from bot import RestaurantAPI


class ActionDisplayMeals(Action):
    def name(self):
        return 'action_display_meals'

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        dispatcher.utter_message("Suche aktuelles Essen für {}".format(tracker.get_slot("time")))
        food_today = 'Pommes'
        dispatcher.utter_message("Heute gibt es: {}".format(food_today))
        return []