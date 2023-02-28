from core.job import Job

class TestJobAlwaysComplete(Job):
    def __init__(self,
                 task,
                 job_id='',
                 start_at: datetime = None,
                 max_working_time: int = -1,
                 tries: int = 0,
                 dependencies: [] = [],
                 done: bool = False,
                 done_with_error: bool = False,
                 error_message: str = ''
                 ):
        pass
    @property
    def done(self): return True