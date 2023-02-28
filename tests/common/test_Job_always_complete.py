from core.job import Job
from tests.common.test_empty_task import TestEmptyTask

class TestJobAlwaysComplete(Job):
    def __init__(self,
                 task=None,
                 job_id='',
                 start_at = None,
                 max_working_time: int = -1,
                 tries: int = 0,
                 dependencies: [] = [],
                 done: bool = False,
                 done_with_error: bool = False,
                 error_message: str = ''
                 ):
        super().__init__(task = TestEmptyTask())
    @property
    def done(self): return True