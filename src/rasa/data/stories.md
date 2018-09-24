## food today
* greet
  - utter_ask_howcanhelp
* ask
  - slot{"time":"heute"}
  - action_query_recommender

## food tomorrow
* greet
  - utter_ask_howcanhelp
* ask
  - slot{"time":"morgen"}
  - action_query_recommender

## food this week
* greet
  - utter_ask_howcanhelp
* ask
  - slot{"time":"woche"}
  - utter_cannot_do_that_yet

## urgent
* ask
  - action_query_recommender

## ask and deny
* ask
  - action_query_recommender
* deny
  - utter_ask_when
* inform{"time":"heute"}
  - action_get_all_meals