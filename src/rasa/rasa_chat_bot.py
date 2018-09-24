import logging
import os

from rasa_core.channels.rest import HttpInputChannel
from rasa_core.remote import RemoteAgent
from rasa_extensions.core.channels.rasa_chat import RasaChatInput       # instantiate the input channel you want to connect to

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")



    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)
# >>> agent.handle_text("hello")



    input_channel = HttpInputChannel(
        5005, "/", RasaChatInput(os.environ.get("RASA_API_ENDPOINT_URL")))

    core_endpoint_config = EndpointConfig(
        url=os.environ.get("RASA_REMOTE_CORE_ENDPOINT_URL"),
        token=os.environ.get("RASA_CORE_TOKEN")
    )

    nlg_endpoint_config = EndpointConfig(
        url=os.environ.get("RASA_NLG_ENDPOINT_URL"),
        token=os.environ.get("RASA_PLATFORM_TOKEN")
    )

    agent = RemoteAgent.load('models/dialogue',
                             core_endpoint=core_endpoint_config,
                             nlg_endpoint=nlg_endpoint_config)

    agent.handle_channel(input_channel)