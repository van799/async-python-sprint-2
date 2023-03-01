import os
from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class DeleteDirTask(TaskBase):
    """Класс для удаления папки."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'delete dir'

    def execute(self) -> None:
        if os.path.is_dir(self.param):
            os.rmdir(self.param)
            print(f'Delete dir  {self.param}')
            logger.info('Deleted %s.', self.param)
        logger.info('Finished deleting dir.')
