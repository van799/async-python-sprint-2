from datetime import datetime
import logging


def get_logger() -> logging.Logger:
    """Настройки логгера для проекта."""

    logging.basicConfig(
        filename='jobs.log',
        filemode='w',
        level=logging.INFO,
        format='%(name)s - %(levelname)s - %(message)s',
    )
    return logging.getLogger('scheduler')


class SchedulerConfig:
    def __init__(self):
        self.__pool_size = 10
        self.__file_name = './data/scheduler.dat'

    @property
    def pool_size(self):
        return self.__pool_size

    @property
    def filename(self):
        return self.__file_name

    @staticmethod
    def GetConfig():
        return SchedulerConfig()
