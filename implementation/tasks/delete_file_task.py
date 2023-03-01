import os
from core.task_base import TaskBase



class DeleteFileTask(TaskBase):
    """Класс для удаления файла."""

    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'delete file'

    def execute(self) -> None:
        #Do not affraid for exceptions!
        #if os.path.isfile(self.param):
        os.remove(self.param)

