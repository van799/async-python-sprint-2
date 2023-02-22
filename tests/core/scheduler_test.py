import unittest
from datetime import datetime

from core.job import Job
from core.scheduler import Scheduler
from implementation.empty_task import EmptyTask
from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_job_repository import TestJobRepository


class SchedulerTest(unittest.TestCase):
    def test_scheduler_load_jobs_when_start(self):
        jobs = [
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0)
        ]
        job_repository = TestJobRepository(items=jobs)
        scheduler = Scheduler(job_repository)
        scheduler.run()
        self.assertEqual(len(scheduler.queue), len(jobs))
        scheduler.stop()

    def test_scheduler_save_jobs_when_stop(self):
        max_job_count = 5
        job_repository = TestJobRepository()
        scheduler = Scheduler(job_repository)
        for i in range(max_job_count):
            scheduler.schedule(task=TestEmptyTask(), max_working_time=-1, tries=0)
        scheduler.stop()

        self.assertEqual(len(job_repository.get_jobs()), max_job_count)
