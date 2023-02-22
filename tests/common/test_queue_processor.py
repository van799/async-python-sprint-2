from core.queue_processor_base import QueueProcessorBase


class TestQueueProcessor(QueueProcessorBase):
    @property
    def is_running(self):
        return

    def run(self, queue):
        return

    def stop(self):
        return
