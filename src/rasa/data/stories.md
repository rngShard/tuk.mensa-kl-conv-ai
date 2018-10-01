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

## create profile 1
* create_profile
  - action_set_user_wants_profile
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
* deny
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart

## create profile 2
* create_profile
  - action_set_user_wants_profile
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

## create profile 3
* create_profile
  - action_set_user_wants_profile
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

## greet create profile 1
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* create_profile
  - action_set_user_wants_profile
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
* deny
  - action_ask_specific_questions
  - slot{"like_q5": false}
  - action_restart

## greet create profile 2
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* create_profile
  - action_set_user_wants_profile
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

## greet create profile 3
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
* create_profile
  - action_set_user_wants_profile
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
  
## ask first question specifics with profiling 00000 without day
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
  - action_predict_meals_after_registration
* inform
  - action_predict_meals_after_registration
  - action_restart

## ask first question specifics with profiling 00000 with day
* ask{"time":"heute"} or ask{"time":"morgen"} or ask{"time":"woche"} or ask{"time":"montag"} or ask{"time":"dienstag"} or ask{"time":"mittwoch"} or ask{"time":"donnerstag"} or ask{"time":"freitag"} or ask{"time":"samstag"} or ask{"time":"sonntag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
  - action_predict_meals_after_registration
  - action_restart

## ask specifics with profiling 00000
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
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