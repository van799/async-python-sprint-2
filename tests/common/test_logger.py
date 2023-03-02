import logging

from core.logger_base import LoggerBase


class TestLogger(LoggerBase):

    def log_info(self, message: str):
        pass

    def log_debug(self, message: str, source: str = ''):
        pass

    def log_error(self, message: str, source: str):
        pass
