from abc import ABC, abstractmethod


class TaskBase(ABC):
    def __init__(self, param=None):
        self.__param = param
        self.__complete = False
        self.__is_running = False

    @property
    def param(self):
        return self.__param

    @abstractmethod
    def execute(self):
        pass

    @property
    def is_running(self):
        return self.__is_running

    def do_task(self):
        self.__is_running = True
        self.execute()
        self.__complete = True
        self.__is_running = False
