from abc import ABC, abstractmethod


class RepositoryBase(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def save(self, jobs):
        pass
