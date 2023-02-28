from time import sleep

from core.task_base import TaskBase


class EmptyTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'empty_task'

    def execute(self):
        print('hello world')
