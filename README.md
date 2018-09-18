# tuk.mensa-kl-conv-ai

Code-base for the AI Project "*Conversational AI for Mensa food recommendations*"


## Rasa

Retrieved from the [Rasa docs](https://rasa.com/docs/getting-started/overview/).

### Training Rasa

Train your **dialogue-model** with

```Bash
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

and your **nlu-model** with 

```Bash
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

### Running Rasa 

To run the rasa instance [with nlu understanding], use

```Bash
python -m rasa_core.run -d models/dialogue [-u models/current/nlu] --endpoints endpoints.yml [--debug]
```

with an _ActionServer_ (`python -m rasa_core_sdk.endpoint --actions actions`) already running.

Note: Not utilizing NLU requires input in form of _\[intent]_.