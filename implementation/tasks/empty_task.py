from core.task_base import TaskBase


class EmptyTask(TaskBase):
    """Пустой тестовый класс"""

    def __init__(self, param: str):
        super().__init__(param)

    @property
    def name(self):
        return 'empty task'

    def execute(self) -> None:
        print('Finished test TASK.')
