import unittest
import json

from core.job import Job
from implementation.job_descriptor_encoder import JobDescriptorEncoder
from implementation.job_factory import JobFactory
from implementation.job_json_repository import JobJsonRepository

from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_read_writer import TestReadWrite


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
                                                job_factory=self.job_factory)
        saved_jobs = job_json_repository.get_jobs()
        job_empty_task = any(
            x.task.name == 'test_empty_task' for x in saved_jobs)
        self.assertNotEqual(job_empty_task, None)


# get test сделать завтра с этго начать, сохранение в файл не работает


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
                                                job_factory=self.job_factory)
        saved_jobs = job_json_repository.get_jobs()
        job_empty_task = any(
            x.task.name == 'test_empty_task' for x in saved_jobs)
        self.assertNotEqual(job_empty_task, None)


if __name__ == '__main__':
    unittest.main()
