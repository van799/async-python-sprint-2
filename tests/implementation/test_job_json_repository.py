import json
import unittest

from tests.common.test_read_writer import TestReadWrite
from core.job import Job
from tests.common.test_empty_task import TestEmptyTask
from implementation.job_factory import JobFactory
from implementation.job_json_repository import JobJsonRepository
from implementation.job_descriptor_encoder import JobDescriptorEncoder


class TestJobJsonRepository(unittest.TestCase):
    def setUp(self):
        self.job_factory = JobFactory()

        self.job_factory.register_job(
            name_task='test_empty_task',
            create_job=lambda start_at, max_working_time, tries,
                              dependencies: Job(TestEmptyTask(''), start_at,
                                                max_working_time,
                                                tries,
                                                dependencies
                                                ))

    def test_get_jobs_return_saved_jobs(self):
        job_descriptor = Job(task=TestEmptyTask(), max_working_time=-1, tries=0).get_job_descriptor()
        jobs = [
            job_descriptor
        ]

        json_jobs = json.dumps(jobs,
                               default=lambda o: o.__dict__,
                               sort_keys=True,
                               indent=4
                               )
        job_json_repository = JobJsonRepository(reader_writer=TestReadWrite(json_jobs),
                                                job_factory=self.job_factory)
        saved_jobs = job_json_repository.get_jobs()
        job_empty_task = any(x.task.name == 'test_empty_task' for x in saved_jobs)
        self.assertNotEqual(job_empty_task, None)
