import time
import os.path
from core.job import Job
from scheduler import Scheduler
from implementation.tasks.empty_task import EmptyTask
from implementation.tasks.create_file_task import CreateFileTask
from implementation.tasks.create_dir_task import CreateDirTask
from implementation.tasks.delete_file_task import DeleteFileTask

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
task_factory.register_task(name_task='create file',
                           create_task=lambda p: CreateFileTask(p))
task_factory.register_task(name_task='delete file',
                           create_task=lambda p: DeleteFileTask(p))
task_factory.register_task(name_task='create_dir',
                           create_task=lambda p: CreateDirTask(p))

repository = JobJsonRepository(read_writer, task_factory)
saved_job_count = len(repository.get_jobs())
scheduler = Scheduler(QueueProcessor(JobQueueDispatcher([])), repository, pool_size=config.pool_size)

if not os.path.exists(config.filename) or saved_job_count <= 0:
    job_create_dir = Job(CreateDirTask('data/create_file'))

    job_create_file = Job(CreateFileTask('data/create_file/create_file.txt'),
                          dependencies=[job_create_dir.job_id])
    job_delete_file = Job(DeleteFileTask('data/create_file/create_file.txt'), dependencies=[job_create_file.job_id])

    scheduler.schedule(job_create_dir)
    scheduler.schedule(job_create_file)
    scheduler.schedule(job_delete_file)

scheduler.run()
time.sleep(10)
scheduler.stop()
