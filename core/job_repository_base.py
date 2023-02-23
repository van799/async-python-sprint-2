from abc import ABC, abstractmethod


class JobRepositoryBase(ABC):
    @abstractmethod
    def get_jobs(self):
        pass

    @abstractmethod
    def save_jobs(self, jobs):
        pass
