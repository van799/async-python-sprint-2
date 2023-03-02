from core.task_base import TaskBase


class CreateFileTask(TaskBase):
    """Класс для создания файла."""

    def __init__(self, param: str) -> None:
        super().__init__(param)

    @property
    def name(self):
        return 'create file'

    def execute(self) -> None:
        with open(f'{self.param}', 'w') as f:
            f.write(f'{self.param}')
        print(f'Create file {self.param}')
