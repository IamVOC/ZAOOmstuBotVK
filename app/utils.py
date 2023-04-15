import requests
from decouple import config


def deserialize(json):
    chat_id = json['object']['message']['from_id']
    text = json['object']['message']['text']
    return chat_id, text


def main_server_request(message):
    payload = {
        "bot_guid": config('BOT_GUID'),
        "message": message
    }
    return requests.post(config('MAIN_SERVER_ADDRESS'), json=payload)
