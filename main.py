from datetime import datetime

from core.job import Job
from core.scheduler import Scheduler

from implementation.empty_task import EmptyTask

# job = Job(task=EmptyTask(), max_working_time=-1, tries=0)

# job.run(datetime.now())

scheduler = Scheduler(pool_size=2)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0) #1
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0) #10
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.schedule(task=EmptyTask(), max_working_time=-1, tries=0)
scheduler.run()
#scheduler.stop()


