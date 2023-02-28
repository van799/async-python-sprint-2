import os
from core.task_base import TaskBase


class DeleteFileTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'delete dir'

    def execute(self):
        if os.path.isfile(self.param):
            os.remove(self.param)
        else:
            print('Path is not a file')
