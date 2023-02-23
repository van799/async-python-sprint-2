import unittest
import json

from core.job import Job
from core.read_write_base import ReaderWriterBase
from implementation.job_json_repository import JobJsonRepository
from implementation.task_factory import TaskFactory

from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_read_writer import TestReadWrite


class TestJobJsonRepository(unittest.TestCase):
    def setUp(self):
        self.task_factory = TaskFactory()

        self.task_factory.register_task( name_task='test_empty_task', create_task=lambda p: TestEmptyTask(p))

    def test_get_job_return_saved_jobs(self):
        job_descriptor = Job(task=TestEmptyTask(),
                             max_working_time=-1, tries=0).get_job_descriptor()
        jobs = [
            job_descriptor
        ]

        json_jobs = json.dumps(jobs,
                               default=lambda o: o.__dict__,
                               sort_keys=True,
                               indent=4
                               )
        job_json_repository = JobJsonRepository(reader_writer=TestReadWrite(json_jobs),
                                                task_factory=self.task_factory)
        saved_jobs = job_json_repository.get_jobs()
        job_empty_task = any(
            x.task.name == 'test_empty_task' for x in saved_jobs)
        self.assertNotEqual(job_empty_task, None)

    def test_get_jobs_return_saved_jobs(self):
        job_descriptor = Job(task=TestEmptyTask(),
                             max_working_time=-1, tries=0).get_job_descriptor()
        jobs = [
            job_descriptor
        ]

        json_jobs = json.dumps(jobs,
                               default=lambda o: o.__dict__,
                               sort_keys=True,
                               indent=4
                               )
        job_json_repository = JobJsonRepository(reader_writer=TestReadWrite(json_jobs),
                                                task_factory=self.task_factory)
        saved_jobs = job_json_repository.get_jobs()
        job_empty_task = any(
            x.task.name == 'test_empty_task' for x in saved_jobs)
        self.assertNotEqual(job_empty_task, None)

    def test_task_accepts_parameter_during_job_creation(self):
        task_param = 'test_task_param'

        job_descriptor = Job(task=TestEmptyTask(task_param),
                             max_working_time=-1, tries=0).get_job_descriptor()
        jobs = [
            job_descriptor
        ]

        json_jobs = json.dumps(jobs,
                               default=lambda o: o.__dict__,
                               sort_keys=True,
                               indent=4
                               )
        job_json_repository = JobJsonRepository(reader_writer=TestReadWrite(json_jobs),
                                                task_factory=self.task_factory)
        saved_jobs = job_json_repository.get_jobs()

        # job_empty_task = any(
        #     x.task.name == 'test_empty_task' for x in saved_jobs)

        job_empty_task = next((x for x in saved_jobs if x.task.name ==  'test_empty_task' ), None)

        self.assertEqual(job_empty_task.task.param, task_param)


if __name__ == '__main__':
    unittest.main()
