from core.task import Task


class TestEmptyTaskAlwaysNotComplete(Task):
    def __init__(self, param=None):
        super().__init__(param)

    def name(self):
        return 'empty_task'

    @property
    def complete(self):
        return False

    def execute(self):
        print('hello world')

