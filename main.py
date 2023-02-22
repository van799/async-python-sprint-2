import time

from implementation.empty_task import EmptyTask
from implementation.queue_processor import QueueProcessor
from implementation.file_read_write import FileReadWrite
from implementation.job_json_repository import JobJsonRepository
from implementation.job_factory import JobFactory
from core.scheduler import Scheduler
from core.job import Job

read_writer = FileReadWrite('C:/temp/schedule.dat')
job_factory = JobFactory()
job_factory.register_job(
    name_task='test_empty_task',
    create_job=lambda start_at, max_working_time, tries,
                      dependencies: Job(EmptyTask(''), start_at,
                                        max_working_time,
                                        tries,
                                        dependencies
                                        ))
repository = JobJsonRepository(read_writer, job_factory)

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
