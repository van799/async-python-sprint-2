from abc import ABC, abstractmethod


class ReaderWriterBase(ABC):
    @abstractmethod
    def read_or_create(self):
        pass

    @abstractmethod
    def write(self, data):
        pass
