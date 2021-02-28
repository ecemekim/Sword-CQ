import logging
from sword_client import run


class ShowServices:

    def activate_job(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(run())
