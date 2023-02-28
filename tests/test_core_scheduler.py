import unittest

from scheduler import Scheduler
from core.job import Job

from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_job_repository import TestJobRepository
from tests.common.test_queue_processor import TestQueueProcessor
from implementation.job_queue_dispatcher import JobQueueDispatcher


class SchedulerTest(unittest.TestCase):
    def test_scheduler_load_jobs_when_start(self):
        jobs = [
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0),
            Job(task=TestEmptyTask(), max_working_time=-1, tries=0)
        ]
        job_repository = TestJobRepository(items=jobs)
        queue = []
        scheduler = Scheduler(TestQueueProcessor(JobQueueDispatcher(queue)), job_repository)
        scheduler.run()
        self.assertEqual(len(queue), len(jobs))

    def test_scheduler_save_jobs_when_stop(self):
        max_job_count = 5
        job_repository = TestJobRepository()
        scheduler = Scheduler(TestQueueProcessor(JobQueueDispatcher([])), job_repository)
        for i in range(max_job_count):
            scheduler.schedule(Job(task=TestEmptyTask(), max_working_time=-1, tries=0))
        scheduler.stop()

        self.assertEqual(len(job_repository.get_jobs()), max_job_count)


if __name__ == '__main__':
    unittest.main()
