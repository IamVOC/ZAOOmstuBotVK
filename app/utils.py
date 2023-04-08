import requests
from decouple import config 
from os import environ
import json

def deserialize(json):
    chat_id = json['object']['message']['from_id']
    text = json['object']['message']['text']
    return chat_id, text

def default_state(json):
    chat_id, message = deserialize_vk(json)
    send_message_vk(generate_payload_vk(chat_id, handled, widgets=widgets))
    return 'OK', 200


def main_server_request(message):
    payload = {
            "bot_guid": config('BOT_GUID'),
            "message": message
            }
    return requests.post(config('MAIN_SERVER_ADDRESS'), json=payload)
                 
def send_message(payload):
    url = "https://api.vk.com/method/messages.send"
    params = payload
    print(payload)
    response = requests.post(url, params=params)
    return response.json()

def generate_payload(chat_id, text):
    payload = {
            "access_token": config('ACCESS_TOKEN'),
            "v": 5.131,
            "peer_id": chat_id,
            "message": text['detail']
            }

    return payload
