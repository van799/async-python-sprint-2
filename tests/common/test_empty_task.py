from core.task_base import TaskBase


class TestEmptyTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    def name(self):
        return 'test_empty_task'

    def execute(self):
        print('hello world')
