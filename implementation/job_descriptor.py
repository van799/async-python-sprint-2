import datetime


class JobDescriptor:
    """Класс описание для каждой созданной TASK """

    def __init__(self):
        self.job_id = ''
        self.task_name: str = ''
        self.task_param: str = ''
        self.start_at: datetime = None,
        self.max_working_time: int = -1,
        self.tries: int = 0,
        self.dependencies: list[str] = []
