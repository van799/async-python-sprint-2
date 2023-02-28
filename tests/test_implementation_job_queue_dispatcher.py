import unittest
from datetime import datetime

from core.job import Job
from implementation.job_queue_dispatcher import JobQueueDispatcher
from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_empty_task_always_complete import TestEmptyTaskAlwaysComplete
from tests.common.test_empty_task_always_not_complete import TestEmptyTaskAlwaysNotComplete
from tests.common.test_Job_always_complete import TestJobAlwaysComplete


class JobQueueDispatcherTest(unittest.TestCase):
 
    def test_job_queue_dispatcher_returns_job_when_dependencies_complete(self):
        job_1 = TestJobAlwaysComplete()
        job_2 = TestJobAlwaysComplete()
        job_3 = TestJobAlwaysComplete()

        dependencies = [
            job_1.job_id,
            job_2.job_id,
            job_3.job_id
        ]

        job = Job(task, dependencies=dependencies)
        queue = [job_1, job_2, job_3, job]

        job_queue_dispatcher = JobQueueDispatcher(queue)
        jobs_to_run = job_queue_dispatcher.get_jobs_to_run()
        job_to_run = next(filter(lambda o: o.job_id
                          == job.job_id, jobs_to_run), None)

        self.assertIsNotNone(job_to_run)

    # dependencies is not implemented

    def test_job_queue_dispatcher_not_returns_job_when_dependencies_are_not_complete(self):
        task = TestEmptyTask()
        job_1 = Job(TestEmptyTaskAlwaysComplete())
        job_2 = Job(TestEmptyTaskAlwaysNotComplete())
        job_3 = Job(TestEmptyTaskAlwaysComplete())

        dependencies = [
            job_1.job_id,
            job_2.job_id,
            job_3.job_id
        ]

        job = Job(task, dependencies=dependencies)
        queue = [job_1, job_2, job_3, job]

        job_queue_dispatcher = JobQueueDispatcher(queue)
        jobs_to_run = job_queue_dispatcher.get_jobs_to_run()
        job_to_run = next(filter(lambda o: o.job_id
                          == job.job_id, jobs_to_run), None)

        self.assertIsNone(job_to_run)


if __name__ == '__main__':
    unittest.main()
