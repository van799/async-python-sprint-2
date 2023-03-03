from core.task_base import TaskBase


class EmptyTask(TaskBase):
    """Пустой тестовый класс"""

    def __init__(self, param: str):
        super().__init__(param)
        self.__param = param

    def execute(self) -> None:
        print(self.__param)
