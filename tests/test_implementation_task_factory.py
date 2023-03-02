import unittest
from implementation.task_factory import TaskFactory
from tests.common.test_empty_task import TestEmptyTask


class TestTaskFactory(unittest.TestCase):
    def test_register_task_register_new_task_creations_method(self):
        task_cls = TestEmptyTask
        task_dict = {
            'create_file': 'create_file',
            'del_file': 'del_file',
        }

        task_factory = TaskFactory(task_dict)
        task_factory.register_task(task_cls)
        self.assertIn(task_cls.__name__, task_dict)

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
        task_cls = TestEmptyTask
        task_factory = TaskFactory()
        task_factory.register_task(task_cls)
        task_create_task = task_factory.get_task_creator(task_cls.__name__)
        self.assertIsNotNone(task_create_task)


if __name__ == '__main__':
    unittest.main()
