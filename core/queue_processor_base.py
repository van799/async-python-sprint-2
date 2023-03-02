from abc import ABC, abstractmethod


class QueueProcessorBase(ABC):

    @property
    def is_running(self):
        pass

    @abstractmethod
    def run(self, queue):
        pass

    @abstractmethod
    def stop(self, queue):
        pass

    @abstractmethod
    def add_jobs_to_queue(self, jobs):
        pass

    @abstractmethod
    def add_job_to_queue(self, jobs):
        pass
