import os
from core.task_base import TaskBase


class DeleteDirTask(TaskBase):
    """Класс для удаления папки."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'delete dir'

    def execute(self) -> None:
        os.rmdir(self.param)
        print(f'Delete dir  {self.param}')
