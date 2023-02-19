from abc import ABC, abstractmethod


class JobRepository(ABC):
    @abstractmethod
    def get_jobs(self):
        pass

    @abstractmethod
    def save_jobs(self, jobs):
        pass