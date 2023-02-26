import threading
from datetime import datetime
from threading import Event
from time import sleep

from core.queue_processor_base import QueueProcessorBase


class QueueProcessor(QueueProcessorBase):
    """Класс для обработки очереди и запуска задач."""
    def __init__(self, job_repository=None, pool_size=10):
        self.__pool_size = pool_size
        self.__queue = None
        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running

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

    def run(self, queue):
        """Метод отвечает за запуск TASK в потоке"""
        if self.__is_running:
            return

        self.__event = Event()
        self.__thread = threading.Thread(
            target=QueueProcessor.__process_queue,
            args=(self.__event, queue, self.__pool_size,)
        )
        self.__thread.start()
        self.__is_running = True

    def stop(self):
        if not self.__is_running:
            return

        self.__event.set()
        self.__thread.join()
        self.__is_running = False
