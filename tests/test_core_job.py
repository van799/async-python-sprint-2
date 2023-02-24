import unittest
from datetime import datetime

from core.job import Job
from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_empty_task_always_complete import TestEmptyTaskAlwaysComplete
from tests.common.test_empty_task_always_not_complete import TestEmptyTaskAlwaysNotComplete


class JobTest(unittest.TestCase):
    def test_job_run_task_without_any_conditions(self):
        self.task = TestEmptyTask()
        self.job = Job(self.task)
        time_now = datetime.strptime(
            '2023-01-30 23:37:13', '%Y-%m-%d %H:%M:%S')

        self.job.run(time_now)
        self.assertTrue(self.task.complete)

    def test_job_not_run_task_before_start_time(self):
        self.task = TestEmptyTask()
        start_at = datetime.strptime(
            '2023-01-29 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job = Job(self.task, start_at=start_at)
        time_now = datetime.strptime(
            '2023-01-28 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job.run(time_now)
        self.assertFalse(self.task.complete)

    def test_job_run_task_after_start_time(self):
        self.task = TestEmptyTask()
        start_at = datetime.strptime(
            '2023-01-30 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job = Job(self.task, start_at=start_at)
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job.run(time_now)
        self.assertTrue(self.task.complete)

    def test_job_run_task_when_tries_count_less_max(self):
        self.task = TestEmptyTask()
        tries = 5
        self.job = Job(self.task, tries=tries)
        self.job.tries_count = 4
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job.run(time_now)
        self.assertTrue(self.task.complete)

    def test_job_not_run_task_when_tries_count_great_max(self):
        self.task = TestEmptyTask()
        tries = 5
        self.job = Job(self.task, tries=tries)
        self.job.tries_count = 6
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job.run(time_now)
        self.assertFalse(self.task.complete)

    def test_job_run_task_when_dependencies_complete(self):
        self.task = TestEmptyTask()
        dependencies = [
            TestEmptyTaskAlwaysComplete(),
            TestEmptyTaskAlwaysComplete(),
            TestEmptyTaskAlwaysComplete()
        ]
        self.job = Job(self.task, dependencies=dependencies)
        time_now = datetime.strptime(
            '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        self.job.run(time_now)
        self.assertTrue(self.task.complete)

        
    ## dependencies is not implemented
    def test_job_run_task_when_dependencies_not_complete(self):
        pass
        # self.task = TestEmptyTask()
        # dependencies = [
        #     TestEmptyTaskAlwaysComplete(),
        #     TestEmptyTaskAlwaysNotComplete(),
        #     TestEmptyTaskAlwaysComplete()
        # ]
        # self.job = Job(self.task, dependencies=dependencies)
        # time_now = datetime.strptime(
        #     '2023-02-01 23:37:13', '%Y-%m-%d %H:%M:%S')
        # self.job.run(time_now)
        # self.assertFalse(self.task.complete)


if __name__ == '__main__':
    unittest.main()
