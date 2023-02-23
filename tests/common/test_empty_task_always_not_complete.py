from core.task_base import TaskBase


class TestEmptyTaskAlwaysNotComplete(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    def name(self):
        return 'empty_task'

    @property
    def complete(self):
        return False

    def execute(self):
        print('hello world')
