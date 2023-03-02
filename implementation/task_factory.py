class TaskFactory:
    """Класс нужен для создания класса такса при считывании не выполненных TASK из файла."""

    def __init__(self, creators={}):
        self.__creators = creators

    def register_task(self, name_task: str, create_task):
        """Метод для предварительной регистрации TASK"""
        self.__creators[name_task] = create_task

    def get_task_creator(self, name_task: str):
        """Метод получение TASK"""
        creator = self.__creators.get(name_task)
        if not creator:
            raise ValueError(name_task)
        return creator
