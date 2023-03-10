import os
from core.task_base import TaskBase


class DeleteFileTask(TaskBase):
    """Класс для удаления файла."""

    def __init__(self, param: str):
        super().__init__(param)

    def execute(self) -> None:
        os.remove(self.param)
