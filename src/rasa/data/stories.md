## hi and what with profile
* greet
   - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* help
  - utter_what_can_do
  - action_restart

## hi and what without profile
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny 
  - utter_welcome_existing_user
* help
  - utter_what_can_do
  - action_restart

## what can do
* help
  - utter_what_can_do

## hasProfile heute
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"heute"}
  - action_predict_meals_after_registration
  - action_restart
## hasProfile morgen
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"morgen"}
  - action_predict_meals_after_registration
  - action_restart
## hasProfile woche
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"woche"}
  - action_predict_meals_after_registration
  - action_restart
## hasProfile montag
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"montag"}
  - action_predict_meals_after_registration
  - action_restart
  ## hasProfile dienstag
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"dienstag"}
  - action_predict_meals_after_registration
  - action_restart
  ## hasProfile mittwoch
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"mittwoch"}
  - action_predict_meals_after_registration
  - action_restart
  ## hasProfile donnerstag
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"donnerstag"}
  - action_predict_meals_after_registration
  - action_restart
  ## hasProfile freitag
* greet
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome_existing_user
* ask{"time":"freitag"}
  - action_predict_meals_after_registration
  - action_restart
## hasNoProfile -> no Profile
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny 
  - action_restart

## ask specifics with profiling 00000
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* deny
  - action_ask_specific_questions
  - slot{"like_q1": false}
  - slot{"requested_slot": "like_q2"}
* deny
  - action_ask_specific_questions
  - slot{"like_q2": false}
  - slot{"requested_slot": "like_q3"}
* deny
  - action_ask_specific_questions
  - slot{"like_q3": false}
  - slot{"requested_slot": "like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot": "like_q5"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart
## ask specifics with profiling 00001
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 00010
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 00011
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 00100
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 00101
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 00110
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 00111
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 01000
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* deny
  - action_ask_specific_questions
  - slot{"like_q1": false}
  - slot{"requested_slot": "like_q2"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q2": true}
  - slot{"requested_slot": "like_q3"}
* deny
  - action_ask_specific_questions
  - slot{"like_q3": false}
  - slot{"requested_slot": "like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot": "like_q5"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart
## ask specifics with profiling 01001
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 01010
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 01011
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 01100
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 01101
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 01110
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 01111
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* deny
    - action_ask_specific_questions
    - slot{"like_q1": false}
    - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 10000
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
  - action_ask_specific_questions
  - slot{"like_q2": false}
  - slot{"requested_slot": "like_q3"}
* deny
  - action_ask_specific_questions
  - slot{"like_q3": false}
  - slot{"requested_slot": "like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot": "like_q5"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart
## ask specifics with profiling 10001
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 10010
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 10011
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 10100
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 10101
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 10110
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 10111
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* deny
    - action_ask_specific_questions
    - slot{"like_q2": false}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 11000
* greet
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* affirm
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q2": true}
  - slot{"requested_slot": "like_q3"}
* deny
  - action_ask_specific_questions
  - slot{"like_q3": false}
  - slot{"requested_slot": "like_q4"}
* deny
  - action_ask_specific_questions
  - slot{"like_q4": false}
  - slot{"requested_slot": "like_q5"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart
## ask specifics with profiling 11001
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 11010
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 11011
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* deny
    - action_ask_specific_questions
    - slot{"like_q3": false}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 11100
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 11101
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* deny
    - action_ask_specific_questions
    - slot{"like_q4": false}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart
## ask specifics with profiling 11110
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* deny
    - action_ask_specific_questions
    - slot{"like_q5": false}
    - action_restart
## ask specifics with profiling 11111
* greet
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_ask_specific_questions
    - slot{"requested_slot": "like_q1"}
* affirm
  - action_ask_specific_questions
  - slot{"like_q1": true}
  - slot{"requested_slot": "like_q2"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q2": true}
    - slot{"requested_slot": "like_q3"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q3": true}
    - slot{"requested_slot": "like_q4"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q4": true}
    - slot{"requested_slot": "like_q5"}
* affirm
    - action_ask_specific_questions
    - slot{"like_q5": true}
    - action_restart