from app.wrapper import App
from flask import request
from decouple import config

def callback_maker():
    vkRequest = request.json
    if vkRequest['type'] == 'confirmation' and vkRequest['group_id'] == 219784020:
        print('VK Callback are connected')
        return config('CALLBACK_TOKEN'), 200
    else:
        print('Different app are trying to connect')
        return 'Service Unavailable', 503

app = App()

app.add_endpoint(endpoint="/", endpoint_name="home", handler=callback_maker, methods=['GET', 'POST'])

app.run()

