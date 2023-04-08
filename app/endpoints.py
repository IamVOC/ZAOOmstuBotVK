from flask import request
from app.handlers import MessageHandler

class EndpointActions:

    def __init__(self, get=None, post=None, put=None, delete=None):
        self.methods = {
                "GET": get,
                "POST": post,
                "PUT": put,
                "DELETE": delete
                }

    def __call__(self):
        return self.methods[request.method](request.json)


def main_route_post(json):
    mh = MessageHandler()
    return mh.handle(json)
