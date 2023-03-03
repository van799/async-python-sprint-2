from core.repository_base import RepositoryBase


class TestJobRepository(RepositoryBase):
    def __init__(self, items=[]):
        super().__init__()
        self.__items = []
        self.__items.extend(items)

    def get(self):
        return self.__items

    def save(self, jobs):
        self.__items.extend(jobs)
