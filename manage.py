from app.wrapper import App
from app.handlers import MessageHandler, CommandHandler
from app.endpoints import EndpointActions, main_route_post

app = App()

messageHandler = MessageHandler()

homeEndpointActions = EndpointActions(post=main_route_post)
app.add_endpoint(endpoint="/", endpoint_name="home", handler=homeEndpointActions, methods=['GET', 'POST'])

app.set_webhook()

app.run()
