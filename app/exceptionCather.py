from app.patterns import Singleton
from app.logger import proxyLogger


class exceptionCather(metaclass=Singleton):

    def exCatcher(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as ex:
                proxyLogger.log(ex, func)

        return inner_function
