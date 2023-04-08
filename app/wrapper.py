from flask import Flask
from decouple import config 
import requests

class App:
    
    def __init__(self):
        self.app = Flask(__name__)
    
    def run(self):
        self.set_webhook()
        self.app.run(debug=True)
    
    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)

    def set_webhook(self):
        token = config('TOKEN')
        webhook_url = config('WEBHOOK_URL')
        webhook = f"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}"
        return requests.get(webhook)
