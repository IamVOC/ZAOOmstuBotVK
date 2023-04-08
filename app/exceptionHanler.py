from app.patterns import Singleton

class exceptionHandler():

    def exHandler(exception, func):
        print(f'Err: {exception}, class: {func.__class__}, func: {func}')
