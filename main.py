import time
import os.path
from core.job import Job
from scheduler import Scheduler
from implementation.tasks.empty_task import EmptyTask
from implementation.queue_processor import QueueProcessor
from implementation.file_read_write import FileReadWrite
from implementation.job_json_repository import JobJsonRepository
from implementation.task_factory import TaskFactory
from implementation.job_queue_dispatcher import JobQueueDispatcher 
from scheduler_config import SchedulerConfig

config = SchedulerConfig.GetConfig()

read_writer = FileReadWrite(config.filename)
task_factory = TaskFactory()

# task factory нужен для создания класса такса при считывании тасок из файла.
# пример: мы считываем название таски из файла но как он создаст клас таски? а так что таска зарегистрирована
# c нужным класом
task_factory.register_task(name_task='empty_task',
                           create_task=lambda p: EmptyTask(p))

repository = JobJsonRepository(read_writer, task_factory)
scheduler = Scheduler(QueueProcessor(JobQueueDispatcher([])), repository, pool_size=config.pool_size)

if(not os.path.exists(config.filename)):
    scheduler.schedule(task=EmptyTask('name_file'), max_working_time=-1, tries=0)  # 1
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)  # 10
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
    scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)

scheduler.run()
time.sleep(10)
scheduler.stop()
