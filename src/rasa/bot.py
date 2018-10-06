import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.fallback import FallbackPolicy

logger = logging.getLogger(__name__)
DEFAULT_EPOCHS = 100


def train_dialogue(domain_file="domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=None),
                            KerasPolicy(),
                            FallbackPolicy(fallback_action_name="action_default_fallback",
                                           core_threshold=0.2,
                                           nlu_threshold=0.2)])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=DEFAULT_EPOCHS,
            batch_size=100,
            validation_split=0.1      
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/nlu.md')
    trainer = Trainer(config.load("nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(description='starts the bot')
                                    #  argument_default='train-all')
    parser.add_argument('--task',
                        choices=["train-nlu", "train-dialogue", "train-all"],
                        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == 'train-all':
        train_nlu()
        train_dialogue()
