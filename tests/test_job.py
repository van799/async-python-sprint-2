import unittest
from datetime import datetime
from job import Job
from tests.common.test_empty_task import TestEmptyTask


class TestJob(unittest.TestCase):
    def test_job_run_task_without_any_conditions(self):
        task = TestEmptyTask()
        job = Job(task)
        time_now = datetime.strptime(
            '2023-01-30 23:37:13', '%Y-%m-%d %H:%M:%S')

        job.run(time_now)
        self.assertTrue(job.done)

    def test_job_not_run_task_before_start_time(self):
        task = TestEmptyTask()
        start_at = datetime.strptime(
            '2023-01-29 23:37:13', '%Y-%m-%d %H:%M:%S')
        job = Job(task, start_at=start_at)
        time_now = datetime.strptime(
            '2023-01-28 23:37:13', '%Y-%m-%d %H:%M:%S')
        job.run(time_now)
        self.assertFalse(job.done)

    def test_job_run_task_after_start_time(self):
        task = TestEmptyTask()
        start_at = datetime.strptime(
            '2023-01-30 23:37:13', '%Y-%m-%d %H:%M:%S')
        job = Job(task, start_at=start_at)
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        job.run(time_now)
        self.assertTrue(job.done)

    def test_job_run_task_when_tries_count_less_max(self):
        task = TestEmptyTask()
        tries = 5
        job = Job(task, tries=tries)
        job.tries_count = 4
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        job.run(time_now)
        self.assertTrue(job.done)

    def test_job_not_run_task_when_tries_count_great_max_and_has_error(self):
        task = TestEmptyTask()
        tries = 5
        job = Job(task, tries=tries)
        job.tries_count = 6
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        job.run(time_now)
        self.assertFalse(job.done_with_error)

if __name__ == '__main__':
    unittest.main()

