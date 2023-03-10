import uuid
from datetime import datetime
from implementation.job_descriptor import JobDescriptor


class Job:
    """Класс описывающий задачу планировщика и её методы."""

    def __init__(self,
                 task,
                 job_id='',
                 start_at: datetime = None,
                 max_working_time: int = -1,
                 tries: int = 3,
                 dependencies: [] = [],
                 done: bool = False,
                 done_with_error: bool = False,
                 error_message: str = ''
                 ):

        self.__task = task
        self.__start_at = start_at
        self.__max_working_time = max_working_time
        self.__tries = tries
        self.__dependencies = dependencies
        self.__tries_count = 0
        self.__co_execute = None
        self.__coroutine = None
        self.__done = done
        self.__done_with_error = done_with_error
        self.__error_message = error_message
        self.__job_id = job_id

        if self.__job_id in (None, ''):
            self.__job_id = str(uuid.uuid1())

    def __ready_to_execute(self, time_now):
        if self.__co_execute is not None:
            return False
        if self.__start_at is not None and self.__start_at >= time_now:
            return False
        return True

    def run(self, time_now):
        if self.__coroutine is None:
            self.__coroutine = self.do_job(time_now)
            next(self.__coroutine)
            return
        self.__coroutine.send(time_now)

    def do_job(self, time_now):
        """Корутина для запуска задач на исполнение."""
        current_time = time_now
        while True:
            if self.__ready_to_execute(current_time) is True:
                if self.__tries_count <= self.__tries:
                    self.__tries_count += 1
                    try:
                        self.__error_message = None
                        self.__task.do_task()
                        self.__done = True
                    except Exception as e:
                        self.__error_message = f"Unexpected exception: {e}"
                else:
                    self.__done_with_error = True
                    self.__error_message = 'Attempts count is excided'

            current_time = yield

    @property
    def job_id(self):
        return self.__job_id

    @property
    def task_name(self):
        return type(self.__task).__name__

    @property
    def task_param(self):
        return self.__task.param

    @property
    def start_at(self) -> datetime:
        return self.__start_at

    @property
    def max_working_time(self) -> int:
        return self.__max_working_time

    @property
    def dependencies(self):
        return self.__dependencies

    @property
    def is_running(self) -> bool:
        return self.__task.is_running

    @property
    def done(self) -> bool:
        return self.__done

    @property
    def done_with_error(self) -> bool:
        return self.__done_with_error

    @property
    def error_message(self) -> str:
        return self.__error_message

    def pause(self):
        pass

    def stop(self):
        """Метод остановки TASK"""
        self.__co_execute.close()
        self.__co_execute = None

    def get_job_descriptor(self):
        """Метод получения описание TASK, если она считана из файла"""
        job_descriptor = JobDescriptor()
        job_descriptor.job_id = self.job_id
        job_descriptor.task_name = self.task_name
        job_descriptor.task_param = self.task_param
        job_descriptor.start_at = self.start_at
        job_descriptor.max_working_time = self.max_working_time
        job_descriptor.dependencies = self.dependencies
        return job_descriptor

    @staticmethod
    def get_job(job_descriptor, task_factory):
        """Метод создания JOB, после получение описание TASK"""
        task_creator = task_factory.get_task_creator(
            job_descriptor.task_name)
        task = task_creator(job_descriptor.task_param)
        return Job(
            job_id=job_descriptor.job_id,
            task=task,
            start_at=job_descriptor.start_at,
            max_working_time=job_descriptor.max_working_time,
            dependencies=job_descriptor.dependencies)
