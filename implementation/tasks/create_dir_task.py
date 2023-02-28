import os
from core.task_base import TaskBase


class CreateDirTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'create dir'

    def execute(self):
        os.mkdir(self.param)
        print(f'Create dir  {self.param}')
