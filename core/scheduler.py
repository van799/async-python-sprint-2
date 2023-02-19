import threading
from datetime import datetime
from threading import Event
from time import sleep

from core.job import Job
from core.job_repository import JobRepository


class Scheduler:
    def __init__(self, job_repository, pool_size=10):
        self.__pool_size = pool_size
        self.__queue = []
        self.__is_running = False
        self.__job_repository = job_repository

    def schedule(self, task,
                 start_at=None,
                 max_working_time=-1,
                 tries=0,
                 dependencies=[]
                 ):

        was_running = self.__is_running
        if self.__is_running:
            self.stop(save=False)
        self.__queue.append(
            Job(task,
                start_at=start_at,
                max_working_time=max_working_time,
                tries=tries,
                dependencies=dependencies
                )
        )
        if was_running == True:
            self.run()

    @staticmethod
    def __process_queue(event, queue, pool_size):
        while True:
            job_count = 0
            for job in queue:
                if job.is_complete:
                    continue
                job_count += 1
                print("запускаем job")
                if job_count < pool_size:
                    job.run(datetime.now())
                else:
                    print('pool is full')
            if event.is_set():
                break
            sleep(1)

    def run(self):
        if self.__is_running:
            return
        loaded_jobs = self.__job_repository.get_jobs()
        self.__queue.extend(loaded_jobs)
        self.__event = Event()
        self.__thread = threading.Thread(
            target=self.__process_queue,
            args=(self.__event, self.__queue, self.__pool_size,)
        )
        self.__thread.start()
        self.__is_running = True

    @property
    def queue(self):
        return self.__queue

    def restart(self):
        self.stop()
        self.run()

    def __save_queue(self):
        self.__job_repository.save_jobs(self.__queue)

    def __save_and_clear_queue(self):
        self.__save_queue()
        self.__queue = []

    def stop(self, save=True):
        if not self.__is_running and save == True:
            self.__save_and_clear_queue()
            return
        self.__event.set()
        self.__thread.join()
        self.__is_running = False
        if save == True:
            self.__save_and_clear_queue()
