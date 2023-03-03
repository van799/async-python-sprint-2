from job import Job
from tests.common.test_empty_task import TestEmptyTask


class TestJobAlwaysComplete(Job):
    def __init__(self):
        super().__init__(task=TestEmptyTask())

    @property
    def done(self):
        return True
