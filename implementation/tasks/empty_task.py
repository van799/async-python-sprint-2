from core.task_base import TaskBase


class EmptyTask(TaskBase):
    """Пустой тестовый класс"""

    def __init__(self, param: str):
        super().__init__(param)

    def execute(self) -> None:
        print('Finished test TASK.')
