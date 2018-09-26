# tuk.mensa-kl-conv-ai

Code-base for the AI Project "*Conversational AI for Mensa food recommendations*"

To use the _Telegram_-bot, add copy [t.me/mensakl_bot](t.me/mensakl_bot) into your browser window (when using the Telegram Web-App) or simply search globally for "MensaKL" or "mensakl_bot" as Telegram-contact.


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

## Deploying Rasa on Remote server

First generate a venv, install packages and prepare data.

```bash
# create venv and activate
virtualenv -p python3 venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
python -m spacy download de

# copy private files
mkdir data
mkdir .cluster_data
# ... [do copying] ...
```

Then spin-up the recommender_server (internel recommender-data-cluster-API; --> :5000), the Rasa action server (for defined custom actions; --> :5055) and the Rasa instance (--> :5005).

```
cd src/rasa
python bot.py --task train-all

python src/recommender/recommender_server.py &
cd src/rasa
python -m rasa_core_sdk.endpoint --actions actions &
python -m rasa_core.run -d models/dialogue -u models/nlu/default/current/ --endpoints endpoints.yml --debug --enable_api &
```