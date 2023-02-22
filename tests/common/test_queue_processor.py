from core.queue_processor_base import QueueProcessorBase

class TestQueueProcessor(QueueProcessorBase):
    
    @property()
    def is_running():
        return
    
    def run(self, queue):
        return

    def stop(self, queue):
        return