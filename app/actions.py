
@exceptionCather.exCather
def getTelegramMessage(request: dict):
    chat_id, message = deserialize(request)
    handle = MessageHandler().handle(chat_id, message)
    return handle()

