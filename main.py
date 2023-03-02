import logging
import time
import os.path
from datetime import datetime, timedelta
from job import Job
from scheduler import Scheduler
from scheduler_config import SchedulerConfig
from implementation.file_read_write import FileReadWrite
from implementation.job_json_repository import JobJsonRepository
from implementation.task_factory import TaskFactory
from implementation.queue_processor import QueueProcessor
from implementation.job_queue_dispatcher import JobQueueDispatcher
from implementation.logger import Logger
from implementation.tasks.create_file_task import CreateFileTask
from implementation.tasks.read_file_task import ReadFileTask
from implementation.tasks.delete_file_task import DeleteFileTask
from implementation.tasks.create_dir_task import CreateDirTask
from implementation.tasks.delete_dir_task import DeleteDirTask
from implementation.tasks.get_weather_task import GetWeatherTask
from implementation.tasks.empty_task import EmptyTask

# Привет, Николай Зимин. Проект решил полностью
# передать с использованием классов и использованию
# различных паттернов проектирования


# конфигурирование Scheduler
config = SchedulerConfig.GetConfig()
logger = Logger(config.log_filename, 'w', logging.INFO)

#     """Класс нужен для создания класса такса при считывании не выполненных TASK из файла."""
task_factory = TaskFactory()

# task factory нужен для создания класса такса при считывании тасок из файла.
# пример: мы считываем название таски из файла но как он создаст клас таски? а так что таска зарегистрирована
# c нужным класом
task_factory.register_task(EmptyTask)
task_factory.register_task(CreateDirTask)
task_factory.register_task(DeleteDirTask)
task_factory.register_task(CreateFileTask)
task_factory.register_task(ReadFileTask)
task_factory.register_task(DeleteFileTask)
task_factory.register_task(GetWeatherTask)

repository = JobJsonRepository(FileReadWrite(config.filename), task_factory)
scheduler = Scheduler(logger, QueueProcessor(
    logger, JobQueueDispatcher([])), repository, pool_size=config.pool_size)

if not os.path.exists(config.filename) or len(repository.get()) <= 0:
    #     Добавляем TASK в dependencies
    job_create_dir = Job(CreateDirTask('data/create_dir'), tries=5)
    job_create_file = Job(CreateFileTask('data/create_dir/create_file.txt'),
                          dependencies=[job_create_dir.job_id], tries=5)
    job_delete_file = Job(DeleteFileTask('data/create_file/create_file.txt'),
                          dependencies=[job_create_file.job_id], tries=5)

    #     Планировка выполнения TASK
    scheduler.schedule(job_create_dir)
    scheduler.schedule(job_create_file)
    scheduler.schedule(job_delete_file)
    scheduler.schedule(Job(task=CreateDirTask(
        'data/create_dir'), max_working_time=-1, tries=0))
    scheduler.schedule(Job(task=CreateFileTask('data/create_dir/create_file_weather.txt'),
                           max_working_time=-1, tries=0))
    scheduler.schedule(Job(task=GetWeatherTask('data/create_dir/create_file_weather.txt'),
                           max_working_time=-1, tries=0))
    scheduler.schedule(Job(task=EmptyTask('param'), max_working_time=-1,
                       tries=0, start_at=datetime.now() + timedelta(minutes=1)))

scheduler.run()
time.sleep(120)
scheduler.stop()
