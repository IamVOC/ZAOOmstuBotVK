from app.patterns import Singleton
from app.utils import deserialize, send_message, generate_payload, main_server_request

class MessageHandler(metaclass=Singleton):
    
    def __init__(self):
        self.state = self.default_state 
        self.support = {
                    'CommandHandler': CommandHandler()
                }

    def default_state(self, json):
        chat_id, message = deserialize_tg(json)
        cmhandler = self.support['CommandHandler']
        handled, widgets = cmhandler.handle(message)
        if not handled:
            predicted_message = main_server_request(message)
            send_message_tg(generate_payload_tg(chat_id, predicted_message.json()['answer']))
            return 'OK', 200
        send_message_tg(generate_payload_tg(chat_id, handled, widgets=widgets))
        return 'OK', 200

    def update_state(self, state, support_objects=None):
        self.state = state
        self.support = support_objects

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

