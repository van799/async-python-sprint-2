import threading
from datetime import datetime
from threading import Event
from implementation.job_queue_dispatcher import JobQueueDispatcher

from core.queue_processor_base import QueueProcessorBase


class QueueProcessor(QueueProcessorBase):
    """Класс отвечает за обработку Jobs"""

    def __init__(self, logger, job_queue_dispatcher: JobQueueDispatcher, pool_size=10):
        self.__logger = logger
        self.__pool_size = pool_size
        self.__is_running = False
        self.__job_queue_dispatcher = job_queue_dispatcher

    @property
    def is_running(self) -> None:
        return self.__is_running

    @staticmethod
    def __process_queue(logger, event, job_queue_dispatcher, pool_size) -> None:
        """Метод для обработки очереди и запуска задач."""
        while True:
            jobs_count = 0
            jobs_to_run = job_queue_dispatcher.get_jobs_to_run()
            if len(jobs_to_run) > 0:
                logger.log_debug(f'{len(jobs_to_run)} jobs ready to run', 'JobQueueProcessor.__process_queue')

            for job in jobs_to_run:
                if jobs_count >= pool_size:
                    logger.log_error(f'Executing of jobs is postponed. Job pool is full',
                                     'JobQueueProcessor.__process_queue')
                    continue
                jobs_count += 1
                job.run(datetime.now())

                if job.error_message not in (None, ''):
                    logger.log_error(
                        f'Job "{job.task_name}", param: "{job.task_param}" finished with error. Error message: "{job.error_message}"',
                        'JobQueueProcessor.__process_queue')
                if job.done:
                    logger.log_info(
                        f'Job "{job.task_name}", param: "{job.task_param}" done.')

            if event.is_set():
                logger.log_debug(f'Received kill event. Processing will be stopped',
                                 'JobQueueProcessor.__process_queue')
                break

    def add_jobs_to_queue(self, jobs) -> None:
        """Метод вызывает метод job_queue_dispatcher для добавления jobs в очередь"""
        return self.__job_queue_dispatcher.add_jobs_to_queue(jobs)

    def add_job_to_queue(self, job) -> None:
        """Метод вызывает метод job_queue_dispatcher для добавления job в очередь"""
        return self.__job_queue_dispatcher.add_job_to_queue(job)

    def get_queue(self) -> None:
        """Метод получает job из очереди"""
        return self.__job_queue_dispatcher.get_all_jobs()

    def run(self) -> None:
        """Метод запускает Job в потоке"""
        if self.__is_running:
            self.__logger.log_debug(f'Queue processor is running', 'QueueProcessor.run')
            return

        self.__event = Event()
        self.__thread = threading.Thread(
            target=QueueProcessor.__process_queue,
            args=(self.__logger, self.__event, self.__job_queue_dispatcher, self.__pool_size,)
        )
        self.__thread.start()
        self.__is_running = True
        self.__logger.log_info(f'Queue processor is started')

    def stop(self) -> None:
        """Метод останавливает Job"""
        if not self.__is_running:
            self.__logger.log_debug(f'Queue processor is not running', 'QueueProcessor.stop')
            return

        self.__event.set()
        self.__thread.join()
        self.__is_running = False
        self.__logger.log_info(f'Queue processor is stopped')
