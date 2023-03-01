from time import sleep

from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class CreateFileTask(TaskBase):
    """Класс для создания файла."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'create file'

    def execute(self) -> None:
        with open(f'{self.param}', 'w') as f:
            f.write(f'{self.param}')
        print(f'Create file {self.param}')
