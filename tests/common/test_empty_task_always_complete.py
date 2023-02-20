from core.task import Task


class TestEmptyTaskAlwaysComplete(Task):
    def __init__(self, param=None):
        super().__init__(param)

    def name(self):
        return 'empty_task'

    @property
    def complete(self):
        return True

    def execute(self):
        print('hello world')
