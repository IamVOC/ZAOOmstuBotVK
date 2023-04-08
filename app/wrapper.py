from flask import Flask, request
from decouple import config 
import requests
from time import sleep
from threading import Timer
from app.endpoints import EndpointActions, main_route_post

class App:
    
    def __init__(self):
        self.app = Flask(__name__)
    
    def run(self):
        self.app.run(debug=True)
    
    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)


 
