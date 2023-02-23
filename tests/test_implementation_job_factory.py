import unittest

from implementation.job_factory import JobFactory


class TestJobFactory(unittest.TestCase):
    def test_register_job_register_new_job_creations_method(self):
        job_dict = {
            'create_file': 'create_file',
            'del_file': 'del_file',
        }
        job_object = JobFactory(job_dict)
        name_task = 'test_job'
        create_job = lambda: 'test_job'
        job_object.register_job(name_task, create_job)
        self.assertIn(name_task, job_dict)

    def test_get_job_creator_returns_creator_method(self):
        job_dict = {
            'create_file': 'create_file',
            'del_file': 'del_file',
        }
        name_task = 'create_file'
        job_object = JobFactory(job_dict)
        job_create_task = job_object.get_job_creator(name_task)
        self.assertEqual(job_create_task, name_task)

    def test_get_job_creator_returns_executable_creators_method(self):
        name_task = 'test_job'
        test_value = 'test_value'
        my_func = lambda: test_value
        job_object = JobFactory()
        job_object.register_job(name_task, my_func)
        job_create_task = job_object.get_job_creator(name_task)
        self.assertEqual(job_create_task(), test_value)

if __name__ == '__main__':
    unittest.main()