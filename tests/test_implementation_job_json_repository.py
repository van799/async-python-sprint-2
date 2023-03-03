import datetime
import unittest
import json
import uuid
from job import Job
from implementation.job_json_repository import JobJsonRepository
from implementation.task_factory import TaskFactory
from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_read_writer import TestReadWrite


class TestJobJsonRepository(unittest.TestCase):
    def setUp(self):
        self.task_factory = TaskFactory()
        self.task_factory.register_task(TestEmptyTask)

    def test_get_job_return_saved_jobs(self):
        test_job_id = '_job_uuid_'
        job_descriptor = Job(task=TestEmptyTask(),
                             max_working_time=-1, tries=0, job_id=test_job_id).get_job_descriptor()
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
        saved_jobs = job_json_repository.get()
        saved_job = next(filter(lambda o: o.job_id
                         == test_job_id, saved_jobs), None)

        self.assertIsNotNone(saved_job)

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
        saved_jobs = job_json_repository.get()

        found = any(
            x.job_id == job_descriptor.job_id and x.task_param == task_param for x in saved_jobs)

        self.assertTrue(found)

    def test_get_job_descriptor_from_dict_maps_task_name(self):

        test_task_name = 'test_name123'
        test_dict = {
            'job_id': '',
            'task_name': test_task_name,
            'task_param': '',
            'start_at': '',
            'max_working_time': '',
            'tries': '',
            'dependencies': '',
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.task_name, test_task_name)

    def test_get_job_descriptor_from_dict_maps_task_param(self):
        test_task_param = 'test_param123'
        test_dict = {
            'job_id': '',
            'task_name': '',
            'task_param': test_task_param,
            'start_at': '',
            'max_working_time': '',
            'tries': '',
            'dependencies': '',
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.task_param, test_task_param)

    def test_get_job_descriptor_from_dict_maps_start_at(self):
        test_start_at = datetime.datetime(2017, 3, 11)
        test_dict = {
            'job_id': '',
            'task_name': '',
            'task_param': '',
            'start_at': test_start_at.isoformat(),
            'max_working_time': '',
            'tries': '',
            'dependencies': '',
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.start_at, test_start_at)

    def test_get_job_descriptor_from_dict_maps_max_working_time(self):
        test_max_working_time = 12
        test_dict = {
            'job_id': '',
            'task_name': '',
            'task_param': '',
            'start_at': '',
            'max_working_time': test_max_working_time,
            'tries': '',
            'dependencies': '',
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.max_working_time,
                         test_max_working_time)

    def test_get_job_descriptor_from_dict_maps_dependencies(self):
        test_dependencies = ['test_str1', 'test_str2']
        test_dict = {
            'job_id': '',
            'task_name': '',
            'task_param': '',
            'start_at': '',
            'max_working_time': '',
            'tries': '',
            'dependencies': test_dependencies,
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.dependencies, test_dependencies)

    def test_get_job_descriptor_from_dict_maps_dependencies(self):
        test_job_uid = uuid.uuid1()
        test_dict = {
            'job_id': test_job_uid,
            'task_name': '',
            'task_param': '',
            'start_at': '',
            'max_working_time': '',
            'tries': '',
            'dependencies': '',
        }

        test_job_descriptor = JobJsonRepository.get_job_descriptor_from_dict(
            test_dict)
        self.assertEqual(test_job_descriptor.job_id, test_job_uid)


if __name__ == '__main__':
    unittest.main()
