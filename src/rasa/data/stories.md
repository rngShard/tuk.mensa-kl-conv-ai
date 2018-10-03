## hi no profile
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - utter_welcome
  - action_restart


## what can do
* help
  - utter_what_can_do
  - action_restart
  
## greet additive vegetarisch
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* vegetarisch
  - action_vegetarisch
  - utter_got_you
  - action_restart
  
## greet additive vegan
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* vegan
  - action_vegan
  - utter_got_you
  - action_restart
  
## greet additive laktose
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* laktose
  - action_laktose
  - utter_got_you
  - action_restart

## greet additive schwein
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* schwein
  - action_schwein
  - utter_got_you
  - action_restart
  
## greet additive rind
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* rind
  - action_rind
  - utter_got_you
  - action_restart
  
## greet additive fisch
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* fisch
  - action_fisch
  - utter_got_you
  - action_restart
  
## additive vegetarisch
* vegetarisch
  - action_check_profile
  - slot{"user_exists": true}
  - action_vegetarisch
  - utter_got_you
  - action_restart

## additive vegetarisch no profile
* vegetarisch
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart
  
## additive vegan
* vegan
  - action_check_profile
  - slot{"user_exists": true}
  - action_vegan
  - utter_got_you
  - action_restart

## additive vegan no profile
* vegan
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart
  
## additive laktose
* vegan
  - action_check_profile
  - slot{"user_exists": true}
  - action_laktose
  - utter_got_you
  - action_restart

## additive laktose no profile
* laktose
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart
  
## additive schwein
* schwein
  - action_check_profile
  - slot{"user_exists": true}
  - action_schwein
  - utter_got_you
  - action_restart

## additive schwein no profile
* schwein
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart

## additive rind
* rind
  - action_check_profile
  - slot{"user_exists": true}
  - action_rind
  - utter_got_you
  - action_restart

## additive rind no profile
* rind
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart
  
## additive fisch
* fisch
  - action_check_profile
  - slot{"user_exists": true}
  - action_fisch
  - utter_got_you
  - action_restart

## additive fisch no profile
* fisch
  - action_check_profile
  - slot{"user_exists": false}
  - utter_only_with_profile
  - action_restart


## ask hasProfile without day
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile heute
* ask{"time":"heute"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile donnerstag
* ask{"time":"donnerstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask first interaction without day
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform
  - action_meals_without_registration
  - action_restart
  
## ask first interaction dienstag
* ask{"time": "dienstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile without day
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile heute
* ask{"time":"heute"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile freitag
* ask{"time":"freitag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart

## hasNoProfile heute
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"heute"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile morgen
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"morgen"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile woche
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"woche"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile montag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"montag"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile dienstag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"dienstag"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile mittwoch
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"mittwoch"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile donnerstag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"donnerstag"}
  - action_meals_without_registration
  - action_restart

## hasNoProfile freitag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* ask{"time":"freitag"}
  - action_meals_without_registration
  - action_restart

## hasProfile without day
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask
  - action_predict_meals_after_registration
  - action_restart

## hasProfile heute
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"heute"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile morgen
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"morgen"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile woche
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"woche"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile montag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"montag"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile dienstag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"dienstag"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile mittwoch
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"mittwoch"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile donnerstag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"donnerstag"}
  - action_predict_meals_after_registration
  - action_restart

## hasProfile freitag
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
* ask{"time":"freitag"}
  - action_predict_meals_after_registration
  - action_restart
  

## NEW QUESTIONS ASKED: create profile 1
* create_profile
  - action_set_user_wants_profile
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q1": "0"}
  - slot{"requested_slot": "like_q2"}
* inform{"answer": "1"}
  - action_ask_specific_questions
  - slot{"like_q2": "1"}
  - slot{"requested_slot": "like_q3"}
* inform{"answer": "2"}
  - action_ask_specific_questions
  - slot{"like_q3": "2"}
  - slot{"requested_slot": "like_q4"}
* inform{"answer": "3"}
  - action_ask_specific_questions
  - slot{"like_q4": "3"}
  - slot{"requested_slot": "like_q5"}
* inform{"answer": "4"}
  - action_ask_specific_questions
  - slot{"like_q5": "4"}
  - action_restart

## create profile 2
* create_profile
  - action_set_user_wants_profile
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* inform{"answer": "5"}
  - action_ask_specific_questions
  - slot{"like_q1": "5"}
  - slot{"requested_slot": "like_q2"}
* inform{"answer": "4"}
  - action_ask_specific_questions
  - slot{"like_q2": "4"}
  - slot{"requested_slot": "like_q3"}
* inform{"answer": "3"}
  - action_ask_specific_questions
  - slot{"like_q3": "3"}
  - slot{"requested_slot": "like_q4"}
* inform{"answer": "2"}
  - action_ask_specific_questions
  - slot{"like_q4": "2"}
  - slot{"requested_slot": "like_q5"}
* inform{"answer": "1"}
  - action_ask_specific_questions
  - slot{"like_q5": "1"}
  - action_restart

## create profile 3
* create_profile
  - action_set_user_wants_profile
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q1": "0"}
  - slot{"requested_slot": "like_q2"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q2": "0"}
  - slot{"requested_slot": "like_q3"}
* inform{"answer": "1"}
  - action_ask_specific_questions
  - slot{"like_q3": "1"}
  - slot{"requested_slot": "like_q4"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q4": "0"}
  - slot{"requested_slot": "like_q5"}
* inform{"answer": "5"}
  - action_ask_specific_questions
  - slot{"like_q5": "5"}
  - action_restart

## create profile 4
* create_profile
  - action_set_user_wants_profile
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* inform{"answer": "5"}
  - action_ask_specific_questions
  - slot{"like_q1": "5"}
  - slot{"requested_slot": "like_q2"}
* inform{"answer": "4"}
  - action_ask_specific_questions
  - slot{"like_q2": "4"}
  - slot{"requested_slot": "like_q3"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q3": "0"}
  - slot{"requested_slot": "like_q4"}
* inform{"answer": "1"}
  - action_ask_specific_questions
  - slot{"like_q4": "1"}
  - slot{"requested_slot": "like_q5"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q5": "0"}
  - action_restart

## create profile 5
* create_profile
  - action_set_user_wants_profile
  - action_ask_specific_questions
  - slot{"requested_slot": "like_q1"}
* inform{"answer": "2"}
  - action_ask_specific_questions
  - slot{"like_q1": "2"}
  - slot{"requested_slot": "like_q2"}
* inform{"answer": "5"}
  - action_ask_specific_questions
  - slot{"like_q2": "5"}
  - slot{"requested_slot": "like_q3"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q3": "0"}
  - slot{"requested_slot": "like_q4"}
* inform{"answer": "0"}
  - action_ask_specific_questions
  - slot{"like_q4": "0"}
  - slot{"requested_slot": "like_q5"}
* inform{"answer": "2"}
  - action_ask_specific_questions
  - slot{"like_q5": "2"}
  - action_restart
