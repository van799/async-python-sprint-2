from datetime import datetime
from typing import Optional

from job import Job
from utils.utils import get_logger

logger = get_logger()


class Scheduler:
    """Класс планировщика задач и его методы."""

    def __init__(self, pool_size: int = 10):
        self.pool_size = pool_size
        self.job_manager = Job.run()
        self.queue = []

    def schedule(self, job_list: list[Job]) -> None:
        """В очередь добавляются задачи которые нужно выполнить
        один запуск планировщика будет обработано только то количество задач,
        которое соответствует pool_size планировщика."""

        for job in job_list:
            self.queue.append(job)
            task_name = job.task.__name__
            if self.pool_size < len(self.queue):
                logger.error(
                    'Tried schedule "%s", but the queue is full',
                    task_name
                )
                continue
            if job.start_at:
                if job.start_at > datetime.now():
                    logger.warning(
                        'Task "%s" added to scheduling at %s',
                        task_name,
                        job.start_at
                    )
                else:
                    logger.info('Task "%s" is added to the schedule', task_name)

    def get_job(self) -> Optional[Job]:
        """Метод управляющий получением задач из очереди. Если задача
        не выполнена просрочена, она удаляется из очереди и не передается
         на исполнение планировщику. Если у задачи есть зависимости,
         проверяется - завершились ли их процессы/потоки. Если да, задача передается на
        исполнение планировщику, если нет, задача возвращается в очередь."""

        job = self.queue.pop(0)
        task_name = job.task.__name__
        if job.start_at:
            if job.start_at < datetime.now():
                logger.warning(
                    'Tried to add task "%s" to the schedule, but time is expired',
                    task_name
                )
                return None
        if job.dependencies:
            for dependency in job.dependencies:
                if (dependency in self.queue
                        or dependency.worker
                        and dependency.worker.is_alive()):
                    self.queue.append(job)
                    return None
        return job

    def run(self) -> None:
        """
         Планировщик исполняет задания пока они есть в
         очереди или пока количество задач не превысит pool_size. Иначе он
         останавливается."""

        count = 0
        if self.queue:
            logger.info('>>>Starting schedule jobs.')
        while self.queue:
            if count < self.pool_size:
                job = self.get_job()
                if job:
                    count += 1
                    self.job_manager.send(job)
        else:
            logger.info('Finish schedule jobs.')
            print(f'Задачи завершены')
