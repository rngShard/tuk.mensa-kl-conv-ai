## greet & ask
* greet
  - utter_ask_howcanhelp
* ask{"time":"heute"} OR ask{"time":"morgen"} OR ask{"time":"woche"}
  - action_query_recommender

## urgent with profile readily available
* ask{"time":"heute"} OR ask{"time":"morgen"} OR ask{"time":"woche"}
  - action_query_recommender

## ask without date and deny profiling
* ask
  - utter_ask_time
* inform <!-- * inform{"time":"heute"} OR inform{"time":"morgen"} OR inform{"time":"woche"} -->
  - action_query_recommender
* deny
  - action_get_all_meals

## ask specifics with profiling 001
* ask{"time":"heute"} OR ask{"time":"morgen"} OR ask{"time":"woche"}
  - action_query_recommender
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot":"like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot":"like_q2"}
* affirm
  - slot{"like_q2": true}
  - action_ask_specific_questions
  - slot{"requested_slot":"like_q3"}
* deny
  - action_ask_specific_questions
  - slot{"like_q3": false}
  - slot{"requested_slot":"like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot":"like_q5"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q5": true}

## ask specifics with profiling 002
* ask
  - utter_ask_time
* inform <!-- * inform{"time":"heute"} OR inform{"time":"morgen"} OR inform{"time":"woche"} -->
  - action_query_recommender
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot":"like_q1"}
* deny
  - action_ask_specific_questions
  - slot{"like_q1": false}
  - slot{"requested_slot":"like_q2"}
* deny
  - action_ask_specific_questions
  - slot{"like_q2": false}
  - slot{"requested_slot":"like_q3"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q3": true}
  - slot{"requested_slot":"like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot":"like_q5"}
* deny
  - action_ask_specific_questions
  - slot{"like_q5": false}