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

# Планируем выполнение тасок
repository = JobJsonRepository(FileReadWrite(config.filename), task_factory)
job_create_dir = Job(CreateDirTask('data/create_file'))
job_create_file = Job(CreateFileTask('data/create_file/create_file.txt'),
                dependencies=[job_create_dir.job_id], tries=5)
job_delete_file = Job(DeleteFileTask('data/create_file/create_file.txt'),
                dependencies=[job_create_file.job_id])
job_delete_dir = Job(DeleteDirTask('data/create_file'),
                dependencies=[job_delete_file.job_id])
job_create_weather_dir = Job(CreateDirTask('data/weather'))
job_create_weather_file = Job(CreateFileTask('data/weather/weather_forecast.txt'),
                dependencies=[job_create_weather_dir.job_id])
job_get_weather = Job(GetWeatherTask('data/weather/weather_forecast.txt'),
                dependencies=[job_create_weather_file.job_id])
job_read_weather_from_file = Job(task=ReadFileTask('data/weather/weather_forecast.txt'),
                dependencies=[job_get_weather.job_id])
job_delete_weather_file = Job(DeleteFileTask('data/weather/weather_forecast.txt'),
                dependencies=[job_read_weather_from_file.job_id])
job_delete_weather_dir = Job(DeleteDirTask('data/weather'),
                dependencies=[job_delete_weather_file.job_id])
job_try_to_delete_weather_dir_again = Job(DeleteDirTask('data/weather'),
                dependencies=[job_delete_weather_dir.job_id])

#Сохраняем в репозитарий
repository.save([
    job_create_dir,
    job_create_file,
    job_delete_file,
    job_delete_dir,
    job_create_weather_dir,
    job_create_weather_file,
    job_get_weather,
    job_read_weather_from_file,
    job_delete_weather_file,
    job_delete_weather_dir,
    job_try_to_delete_weather_dir_again
])

scheduler = Scheduler(logger, QueueProcessor(
    logger, JobQueueDispatcher()), repository, pool_size=config.pool_size)

scheduler.schedule(Job(task=EmptyTask('Emptytask says hello!'), max_working_time=-1, tries=5,
                       start_at=datetime.now() + timedelta(minutes=1)))
scheduler.run()
time.sleep(120)
scheduler.stop()
