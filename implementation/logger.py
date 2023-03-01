import logging

from core.logger_base import LoggerBase


class Logger(LoggerBase):
    def __init__(self, filename, filemode, level):
        logging.basicConfig(
            filename=filename,
            filemode=filemode,
            level=level,
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        )
        self.__logger = logging.getLogger('scheduler')

    def log_info(self, message):
        self.__logger.info(message)

    def log_debug(self, message, source=''):
        if source == '':
            self.__logger.debug(message)
            return
        self.__logger.debug(f'Source: "{source}", Message: "{message}"')

    def log_error(self, message, source):
        if source == '':
            self.__logger.error(message)
            return
        self.__logger.error(f'Source: "{source}", Message: "{message}"')
