from app.wrapper import App
from app.handlers import MessageHandler
from app.endpoints import EndpointActions, main_route_post
import vk
from decouple import config

app = App()

api = vk.API(config('CALLBACK_TOKEN'), v='5.131')

messageHandler = MessageHandler()
messageHandler.update_state(
    messageHandler.default_state, support_objects={'vkapi': api})

homeEndpointActions = EndpointActions(post=main_route_post)
app.add_endpoint(endpoint="/", endpoint_name="home",
                 handler=homeEndpointActions, methods=['GET', 'POST'])

app.run()
