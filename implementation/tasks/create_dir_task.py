import os
from core.task_base import TaskBase


class CreateDirTask(TaskBase):
    """Класс создания директории."""

    def __init__(self, param: str):
        super().__init__(param)

    @property
    def name(self):
        return 'create dir'

    def execute(self) -> None:
        os.mkdir(self.param)
        print(f'Create dir  {self.param}')
