import time

from core.job import Job
from scheduler import Scheduler
from implementation.tasks.empty_task import EmptyTask
from implementation.queue_processor import QueueProcessor
from implementation.file_read_write import FileReadWrite
from implementation.job_json_repository import JobJsonRepository
from implementation.task_factory import TaskFactory

file_name = './data/scheduler.dat'
# file_name = 'C:/temp/schedule.dat'
read_writer = FileReadWrite(file_name)
task_factory = TaskFactory()

task_factory.register_task(name_task='test_empty_task',
                           create_task=lambda: EmptyTask(''))

repository = JobJsonRepository(read_writer, task_factory)

scheduler = Scheduler(QueueProcessor(), repository, pool_size=2)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)  # 1
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
