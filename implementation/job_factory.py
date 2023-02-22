from core.task import Task


class JobFactory:
    def __init__(self, creators={}):
        self.__creators = creators

    def register_job(self, name_task, create_job):
        self.__creators[name_task] = create_job

    def get_job_creator(self, name_task):
        creator = self.__creators.get(name_task)
        if not creator:
            raise ValueError(name_task)
        return creator
