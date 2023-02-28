import threading
from datetime import datetime
from threading import Event
from time import sleep
from implementation.job_queue_dispatcher import JobQueueDispatcher
# from core.job_base import JobBase

from core.queue_processor_base import QueueProcessorBase


class QueueProcessor(QueueProcessorBase):
    def __init__(self, job_queue_dispatcher: JobQueueDispatcher, pool_size=10):
        self.__pool_size = pool_size
        self.__is_running = False
        self.__job_queue_dispatcher = job_queue_dispatcher

    @property
    def is_running(self):
        return self.__is_running

    @staticmethod
    def __process_queue(event, job_queue_dispatcher, pool_size):
        """Метод для обработки очереди и запуска задач."""
        while True:
            jobs_count = 0
            jobs_to_run = job_queue_dispatcher.get_jobs_to_run()

            for job in jobs_to_run:
                if jobs_count >= pool_size:
                    print(f'Executing of jobs is postponed. Job pool is full')
                    continue
                jobs_count += 1
                job.run(datetime.now())
            if event.is_set():
                break
            #sleep(1)

    def add_jobs_to_queue(self, jobs): return self.__job_queue_dispatcher.add_jobs_to_queue(jobs)
    def add_job_to_queue(self, job): return self.__job_queue_dispatcher.add_job_to_queue(job)


    def get_queue(self): return self.__job_queue_dispatcher.get_all_jobs()

    def run(self):
        if self.__is_running:
            return

        self.__event = Event()
        self.__thread = threading.Thread(
            target=QueueProcessor.__process_queue,
            args=(self.__event, self.__job_queue_dispatcher, self.__pool_size,)
        )
        self.__thread.start()
        self.__is_running = True

    def stop(self):
        if not self.__is_running:
            return

        self.__event.set()
        self.__thread.join()
        self.__is_running = False
