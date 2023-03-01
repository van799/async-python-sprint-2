import os
from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class DeleteFileTask(TaskBase):
    """Класс для удаления файла."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'delete file'

    def execute(self) -> None:
        if os.path.isfile(self.param):
            os.remove(self.param)
            logger.info('Deleted %s.', self.param)
        logger.info('Finished deleting file.')
