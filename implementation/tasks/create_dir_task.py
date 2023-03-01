import os
from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class CreateDirTask(TaskBase):
    """Класс создания директории."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'create dir'

    def execute(self) -> None:
        if not os.path.isdir(self.param):
            os.mkdir(self.param)
            print(f'Create dir  {self.param}')
            logger.info('Created %s.', self.param)
        logger.info('Finished creating dir.')
