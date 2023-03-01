from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class EmptyTask(TaskBase):
    """Пустой тестовый класс"""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'empty task'

    def execute(self) -> None:
        print('Finished test TASK.')
        logger.info('Finished test TASK.')
