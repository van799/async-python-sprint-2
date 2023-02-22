from abc import ABC, abstractmethod

class QueueProcessorBase(ABC):
    
    @property
    def is_running(self):
        pass
    
    def run(self, queue):
        pass

    def stop(self, queue):
        pass
