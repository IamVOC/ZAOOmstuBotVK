import requests
from decouple import config 
from os import environ
import json
import vk

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
                
