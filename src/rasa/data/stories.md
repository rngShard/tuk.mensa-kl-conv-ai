## greet & ask
* greet
  - utter_ask_howcanhelp
* ask
  - action_get_meals

## urgent with profile readily available
* ask{"time":"heute"} OR ask{"time":"morgen"} OR ask{"time":"woche"}
  - action_get_meals

## ask without date and deny profiling
* ask
  - action_get_meals
* inform
  - action_get_meals

## ask specifics with profiling 001
* ask{"time":"heute"} OR ask{"time":"morgen"} OR ask{"time":"woche"}
  - action_get_meals
* profile
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
  - action_get_meals
* inform
  - action_get_meals
* profile
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

## hi and what
* greet
  - utter_ask_howcanhelp
* help
  - utter_what_can_do

## what can do
* help
  - utter_what_can_do