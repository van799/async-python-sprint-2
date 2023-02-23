import threading
from datetime import datetime
from threading import Event
from time import sleep

from core.job import Job
from core.job_repository_base import JobRepositoryBase


class Scheduler:
    """Класс описывающий планировщик задач и его методы."""

    def __init__(self, queue_processor, job_repository=None, pool_size=10):
        self.__pool_size = pool_size
        self.__queue = []
        self.__is_running = False
        self.__job_repository = job_repository
        self.__queue_processor = queue_processor

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

    def run(self):
        """Метод запуска задач в потоке."""
        if self.__queue_processor.is_running:
            return

        loaded_jobs = self.__load_queue()
        self.__queue.extend(loaded_jobs)
        self.__queue_processor.run(self.queue)

    @property
    def queue(self):
        return self.__queue

    def restart(self):
        """Метод перезапуска задач."""
        self.__queue_processor.stop()
        self.__queue_processor.run(self.queue)

    def __load_queue(self):
        if self.__job_repository == None:
            return []
        return self.__job_repository.get_jobs()

    def __save_queue(self):
        """Метод сохранения не выполненных задач."""
        if self.__job_repository == None:
            return
        self.__job_repository.save_jobs(self.__queue)

    def stop(self):
        """Метод остановки задач."""
        if not self.__queue_processor:
            return
        self.__queue_processor.stop()
        self.__save_queue()
