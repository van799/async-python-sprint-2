from abc import ABC, abstractmethod


class ReaderWriter(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass
