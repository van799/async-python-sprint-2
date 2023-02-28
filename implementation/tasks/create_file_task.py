from time import sleep

from core.task_base import TaskBase


class CreateFileTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'create file'

    def execute(self):
        with open(f'{self.param}', 'w') as f:
            f.write(f'{self.param}')
        print(f'Create file {self.param}')
