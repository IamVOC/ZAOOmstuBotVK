from app.patterns import Singleton
from app.utils import deserialize, main_server_request
from decouple import config
import random


class MessageHandler(metaclass=Singleton):

    def __init__(self):
        self.state = self.default_state
        self.support = {
            'CommandHandler': CommandHandler()
        }

    def default_state(self, json):
        chat_id, message = deserialize(json)
        predicted_message = main_server_request(chat_id, message)
        self.send_message(chat_id, predicted_message.json())
        return 'OK', 200

    def update_state(self, state, support_objects=None):
        self.state = state
        self.support = support_objects

    def send_message(self, chat_id, message, widgets=None):
        self.support['vkapi'].messages.send(
            access_token=config('ACCESS_TOKEN'),
            user_id=str(chat_id),
            message=message,
            random_id=random.getrandbits(64))

    def handle(self, json):
        return self.state(json)


class CommandHandler:

    def __init__(self):
        self.command_dicts = {
            '/start': self.default_start_command
        }

    def default_start_command(self):
        return "<b>ZAO bot</b> - это бот в котором вы наверняка сможете найти ответ на ваш вопрос по заочному образованию. Если вы хотите получить ответ, то просто напишите мне нужный вопрос", 200

    def change_commands(self, command, action):
        self.command_dicts[command] = action

    def handle(self, message):
        if message in self.command_dicts:
            return self.command_dicts[message]()
        return None, None
