from core.task_base import TaskBase


class ReadFileTask(TaskBase):
    """Класс чтения из файла."""

    def __init__(self, param: str):
        super().__init__(param)

    def execute(self) -> None:
        with open(f'{self.param}', ) as f:
            lines = f.readlines()
        print(f'Readed file:\n {lines}')
