import datetime


class JobDescriptor:

    def __init__(self):

        # job_name = ''
        self.task_name = ''
        self.task_param = ''
        self.start_at = None,
        self.max_working_time = -1,
        self.tries = 0,
        self.dependencies = []
