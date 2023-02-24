import unittest

from implementation.task_factory import TaskFactory
from core.job import Job


class TestTaskFactory(unittest.TestCase):
    def test_register_task_register_new_task_creations_method(self):
        task_dict = {
            'create_file': 'create_file',
            'del_file': 'del_file',
        }

        task_factory = TaskFactory(task_dict)
        name_task = 'test_job'
        create_job = lambda: 'test_job'
        task_factory.register_task(name_task, create_job)
        self.assertIn(name_task, task_dict)

    def test_get_task_creator_returns_creator_method(self):
        task_dict = {
            'create_file': 'create_file',
            'del_file': 'del_file',
        }
        name_task = 'create_file'
        task_factory = TaskFactory(task_dict)
        create_task = task_factory.get_task_creator(name_task)
        self.assertEqual(create_task, name_task)

    def test_get_task_creator_returns_executable_creators_method(self):
        name_task = 'test_job'
        test_value = 'test_value'
        creator_func = lambda: test_value
        task_factory = TaskFactory()
        task_factory.register_task(name_task, creator_func)
        task_create_task = task_factory.get_task_creator(name_task)
        self.assertEqual(task_create_task(), test_value)


if __name__ == '__main__':
    unittest.main()
