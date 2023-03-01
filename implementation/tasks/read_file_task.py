from core.task_base import TaskBase
from scheduler_config import get_logger

logger = get_logger()


class ReadFileTask(TaskBase):
    """Класс чтения из файла."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'create file'

    def execute(self) -> None:
        try:
            with open(f'{self.param}.txt', ) as f:
                lines = f.readlines()
            print(f'read file: {lines}')
            logger.info('Finished reading file.')
        except EnvironmentError as error:
            logger.error(error)
