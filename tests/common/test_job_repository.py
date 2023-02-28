from core.job_repository_base import JobRepositoryBase


class TestJobRepository(JobRepositoryBase):
    def __init__(self, items=[]):
        super().__init__()
        self.__items = []
        self.__items.extend(items)

    def get_jobs(self):
        return self.__items

    def save_jobs(self, jobs):
        self.__items.extend(jobs)
