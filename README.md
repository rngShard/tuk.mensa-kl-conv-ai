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

Note that the `bot.py` class implements the training procedure. Running the bot without parameters trains both *dialogue* and *nlu*, while providing flags of `... --task train-[dialogue|nlu]` train only the respective step.

### Running Rasa 

To run the rasa instance [with nlu understanding], use

```Bash
python -m rasa_core.run -d models/dialogue [-u models/current/nlu] --endpoints endpoints.yml [--debug] [--enable_api]
```

with an _ActionServer_ (`python -m rasa_core_sdk.endpoint --actions actions`) already running.
The *enable_api* flag allows for http-request in the form of

```bash
curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"hallo"}'
```

to access the Rasa instance.

Note: Not utilizing NLU requires input in form of _\[intent]_.