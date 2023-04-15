import logging
from exceptionHanler import exceptionHandler


class proxyLogger():
    logging.basicConfig(level=logging.INFO, filename="py_log.log",
                        format="%(asctime)s %(levelname)s %(message)s")

    def log(self, err, func):
        self.logging.error("ERROR: " + err + "IN CLASS: " + func.__class__)
        exceptionHandler.exHandler(err, func)
