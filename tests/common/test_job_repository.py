from core.job_repository import JobRepository


class TestJobRepository(JobRepository):
    def __init__(self, items=[]):
        super().__init__()
        self.__items = items

    def get_jobs(self):
        return self.__items

    def save_jobs(self, jobs):
        self.__items = jobs
