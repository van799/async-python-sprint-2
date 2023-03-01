from abc import ABC, abstractmethod


class LoggerBase(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_debug(self, message, source):
        pass

    @abstractmethod
    def log_error(self, message, source):
        pass
