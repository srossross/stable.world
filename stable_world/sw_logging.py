import os
import logging

import time


class Formatter(logging.Formatter):
    def __init__(self, fmt):
        logging.Formatter.__init__(self, fmt)
        self.last = time.time()

    def formatMessage(self, record):
        current = time.time()
        record.delta = '%sms' % int((current - self.last) * 1000 // 1)
        self.last = current
        return self._style.format(record)


def setup_logging():

    DEBUG_ENVVAR = os.getenv('DEBUG', '')
    if not DEBUG_ENVVAR:
        logging.getLogger().addHandler(logging.NullHandler())
        return

    log_names = DEBUG_ENVVAR.split(os.pathsep)

    handler = logging.StreamHandler()
    handler.setFormatter(Formatter('[+%(delta)s|%(name)s] %(message)s'))

    for log_name in log_names:
        if log_name == '*':
            log_name = None  # Root

        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)