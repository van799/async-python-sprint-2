from core.task_base import TaskBase


class TestEmptyTaskAlwaysNotComplete(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    def execute(self):
        print('hello world')
