## what can do
* help
  - utter_what_can_do
  - action_restart

## who am i
* who_am_i
  - action_get_user_id
  - action_restart
  
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
  
## hi no profile 1
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* affirm
  - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q1
    - slot{"like_q1": "1"}
    - utter_ask_like_q2
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q2
    - slot{"like_q2": "0"}
    - utter_ask_like_q3
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q3
    - slot{"like_q3": "3"}
    - utter_ask_like_q4
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q4
    - slot{"like_q4": "5"}
    - utter_ask_like_q5
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q5
    - slot{"like_q5": "2"}
    - action_create_profile
    - action_restart
## Hi no profile 2
* greet
    - action_check_user_wants_profile
    - slot{"wants_no_profile": false}
    - action_check_profile
    - slot{"user_exists": false}
    - utter_ask_create_profile
* affirm
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q1
    - slot{"like_q1": "5"}
    - utter_ask_like_q2
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q2
    - slot{"like_q2": "4"}
    - utter_ask_like_q3
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q3
    - slot{"like_q3": "3"}
    - utter_ask_like_q4
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q4
    - slot{"like_q4": "2"}
    - utter_ask_like_q5
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q5
    - slot{"like_q5": "1"}
    - action_create_profile
    - action_restart
  
## hi wants no profile
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_welcome
  - action_restart
  
## hi has profile
* greet
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - utter_welcome
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
* laktose
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


## ask hasProfile without day heute
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "heute"}
  - slot{"time": "heute"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day morgen
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "morgen"}
  - slot{"time": "morgen"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day woche
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "woche"}
  - slot{"time": "woche"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day Montag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "montag"}
  - slot{"time": "montag"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day Dienstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "dienstag"}
  - slot{"time": "dienstag"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day Mittwoch
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "mittwoch"}
  - slot{"time": "mittwoch"}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile without day donnerstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "donnerstag"}
  - slot{"time": "donnerstag"}
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile without day Freitag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
* inform{"time": "freitag"}
  - slot{"time": "freitag"}
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile heute
* ask{"time":"heute"}
  - slot{"time": "heute"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile morgen
* ask{"time":"morgen"}
  - slot{"time": "morgen"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile woche
* ask{"time":"woche"}
  - slot{"time": "woche"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile montag
* ask{"time":"montag"}
  - slot{"time": "montag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile dienstag
* ask{"time":"dienstag"}
  - slot{"time": "dienstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile mittwoch
* ask{"time":"mittwoch"}
  - slot{"time": "mittwoch"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart

## ask hasProfile donnerstag
* ask{"time":"donnerstag"}
  - slot{"time": "donnerstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask hasProfile freitag
* ask{"time":"freitag"}
  - slot{"time": "freitag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": true}
  - action_predict_meals_after_registration
  - action_restart
  
## ask first interaction without day heute
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "heute"}
  - slot{"time": "heute"}
  - action_meals_without_registration
  - action_restart
  
## ask first interaction without day morgen
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "morgen"}
  - slot{"time": "morgen"}
  - action_meals_without_registration
  - action_restart
  
## ask first interaction without day woche
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "woche"}
  - slot{"time": "woche"}
  - action_meals_without_registration
  - action_restart
  
## ask first interaction without day montag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "montag"}
  - slot{"time": "montag"}
  - action_meals_without_registration
  - action_restart
  
## ask first interaction without day dienstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "dienstag"}
  - slot{"time": "dienstag"}
  - action_meals_without_registration
  - action_restart

## ask first interaction without day mittwoch
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "mittwoch"}
  - slot{"time": "mittwoch"}
  - action_meals_without_registration
  - action_restart

## ask first interaction without day donnerstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "donnerstag"}
  - slot{"time": "donnerstag"}
  - action_meals_without_registration
  - action_restart

## ask first interaction without day freitag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
* inform{"time": "freitag"}
  - slot{"time": "freitag"}
  - action_meals_without_registration
  - action_restart

## ask first interaction heute
* ask{"time": "heute"}
  - slot{"time": "heute"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction morgen
* ask{"time": "morgen"}
  - slot{"time": "morgen"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction woche
* ask{"time": "woche"}
  - slot{"time": "woche"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart

## ask first interaction montag
* ask{"time": "montag"}
  - slot{"time": "montag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction dienstag
* ask{"time": "dienstag"}
  - slot{"time": "dienstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction mittwoch
* ask{"time": "mittwoch"}
  - slot{"time": "mittwoch"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction donnerstag
* ask{"time": "donnerstag"}
  - slot{"time": "donnerstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart
  
## ask first interaction freitag
* ask{"time": "freitag"}
  - slot{"time": "freitag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": false}
  - action_check_profile
  - slot{"user_exists": false}
  - utter_ask_create_profile
* deny
  - action_set_user_wants_no_profile
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile without day heute
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "heute"}
  - slot{"time": "heute"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day morgen
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "morgen"}
  - slot{"time": "morgen"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day woche
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "woche"}
  - slot{"time": "woche"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day montag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "montag"}
  - slot{"time": "montag"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day dienstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "dienstag"}
  - slot{"time": "dienstag"}
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile without day Mittwoch
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "mittwoch"}
  - slot{"time": "mittwoch"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day donnerstag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "donnerstag"}
  - slot{"time": "donnerstag"}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile without day freitag
* ask
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
* inform{"time": "freitag"}
  - slot{"time": "freitag"}
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile heute
* ask{"time":"heute"}
  - slot{"time": "heute"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile morgen
* ask{"time":"morgen"}
  - slot{"time": "morgen"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile woche
* ask{"time":"woche"}
  - slot{"time": "woche"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile montag
* ask{"time":"montag"}
  - slot{"time": "montag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile dienstag
* ask{"time":"dienstag"}
  - slot{"time": "dienstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile mittwoch
* ask{"time":"mittwoch"}
  - slot{"time": "mittwoch"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart

## ask hasNoProfile donnerstag
* ask{"time":"donnerstag"}
  - slot{"time": "donnerstag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart
  
## ask hasNoProfile freitag
* ask{"time":"freitag"}
  - slot{"time": "freitag"}
  - action_check_user_wants_profile
  - slot{"wants_no_profile": true}
  - action_check_profile
  - slot{"user_exists": false}
  - action_meals_without_registration
  - action_restart

## Create profile alles 0
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q1
    - slot{"like_q1": "0"}
    - utter_ask_like_q2
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q2
    - slot{"like_q2": "0"}
    - utter_ask_like_q3
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q3
    - slot{"like_q3": "0"}
    - utter_ask_like_q4
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q4
    - slot{"like_q4": "0"}
    - utter_ask_like_q5
* inform{"answer": "0"}
    - slot{"answer": "0"}
    - action_set_q5
    - slot{"like_q5": "0"}
    - action_create_profile
    - action_restart
    
## Create profile alles 1
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q1
    - slot{"like_q1": "1"}
    - utter_ask_like_q2
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q2
    - slot{"like_q2": "1"}
    - utter_ask_like_q3
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q3
    - slot{"like_q3": "1"}
    - utter_ask_like_q4
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q4
    - slot{"like_q4": "1"}
    - utter_ask_like_q5
* inform{"answer": "1"}
    - slot{"answer": "1"}
    - action_set_q5
    - slot{"like_q5": "1"}
    - action_create_profile
    - action_restart

## Create profile alles 2
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q1
    - slot{"like_q1": "2"}
    - utter_ask_like_q2
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q2
    - slot{"like_q2": "2"}
    - utter_ask_like_q3
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q3
    - slot{"like_q3": "2"}
    - utter_ask_like_q4
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q4
    - slot{"like_q4": "2"}
    - utter_ask_like_q5
* inform{"answer": "2"}
    - slot{"answer": "2"}
    - action_set_q5
    - slot{"like_q5": "2"}
    - action_create_profile
    - action_restart
    
## Create profile alles 3
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q1
    - slot{"like_q1": "3"}
    - utter_ask_like_q2
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q2
    - slot{"like_q2": "3"}
    - utter_ask_like_q3
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q3
    - slot{"like_q3": "3"}
    - utter_ask_like_q4
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q4
    - slot{"like_q4": "3"}
    - utter_ask_like_q5
* inform{"answer": "3"}
    - slot{"answer": "3"}
    - action_set_q5
    - slot{"like_q5": "3"}
    - action_create_profile
    - action_restart

## Create profile alles 4
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q1
    - slot{"like_q1": "4"}
    - utter_ask_like_q2
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q2
    - slot{"like_q2": "4"}
    - utter_ask_like_q3
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q3
    - slot{"like_q3": "4"}
    - utter_ask_like_q4
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q4
    - slot{"like_q4": "4"}
    - utter_ask_like_q5
* inform{"answer": "4"}
    - slot{"answer": "4"}
    - action_set_q5
    - slot{"like_q5": "4"}
    - action_create_profile
    - action_restart

## Create profile alles 5
* create_profile
    - action_set_user_wants_profile
    - utter_ask_like_q1
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q1
    - slot{"like_q1": "5"}
    - utter_ask_like_q2
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q2
    - slot{"like_q2": "5"}
    - utter_ask_like_q3
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q3
    - slot{"like_q3": "5"}
    - utter_ask_like_q4
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q4
    - slot{"like_q4": "5"}
    - utter_ask_like_q5
* inform{"answer": "5"}
    - slot{"answer": "5"}
    - action_set_q5
    - slot{"like_q5": "5"}
    - action_create_profile
    - action_restart
