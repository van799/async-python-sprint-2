from core.queue_processor_base import QueueProcessorBase


class TestQueueProcessor(QueueProcessorBase):

    def __init__(self, job_queue_dispatcher):
        self.__job_queue_dispatcher = job_queue_dispatcher

    @property
    def is_running(self):
        return

    def run(self):
        return

    def stop(self):
        return

    def add_jobs_to_queue(self, jobs):
        self.__job_queue_dispatcher.add_jobs_to_queue(jobs)

    def add_job_to_queue(self, jobs):
        self.__job_queue_dispatcher.add_job_to_queue(jobs)

    def get_queue(self):
        return self.__job_queue_dispatcher.get_all_jobs()
