from abc import ABC, abstractmethod


class ReaderWriterBase(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass
