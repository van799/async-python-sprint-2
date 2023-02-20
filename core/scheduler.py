import threading
from datetime import datetime
from threading import Event
from time import sleep

from core.job import Job
from core.job_repository import JobRepository


class Scheduler:
    """Класс описывающий планировщик задач и его методы."""

    def __init__(self, job_repository=None, pool_size=10):
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
        """Постановка задач в очередь. Сперва проверяются есть ли запущеные задачи,
        если есть выполнение задач останавливается. В очередь можно добавить любое
        количество задач, но за один запуск планировщика будет обработано только
        то количество задач, которое соответствует pool_size планировщика. """
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
        """Метод  для обработки очереди и запуска задач."""
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
        """Метод запуска задач в потоке."""
        if self.__is_running:
            return
        loaded_jobs = self.__load_queue()
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
        """Метод перезапуска задач."""
        self.stop()
        self.run()

    def __load_queue(self):
        if self.__job_repository == None:
            return []
        self.__job_repository.__load_queue()

    def __save_queue(self):
        """Метод сохранения не выполненных задач."""
        if self.__job_repository == None:
            return
        self.__job_repository.save_jobs(self.__queue)

    def __save_and_clear_queue(self):
        self.__save_queue()
        self.__queue = []

    def stop(self, save=True):
        """Метод остановки задач."""
        if not self.__is_running and save == True:
            self.__save_and_clear_queue()
            return
        self.__event.set()
        self.__thread.join()
        self.__is_running = False
        if save == True:
            self.__save_and_clear_queue()
