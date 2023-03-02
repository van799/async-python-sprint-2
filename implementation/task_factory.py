class TaskFactory:
    """Класс нужен для создания класса такса при считывании не выполненных TASK из файла."""

    def __init__(self, creators={}):
        self.__creators = creators

    """Метод для предварительной регистрации TASK"""

    def register_task(self, task_cls: type):
        self.__creators[task_cls.__name__] = lambda p: TaskFactory.__get_object(
            task_cls, p)

    @staticmethod
    def __get_object(task_cls, p):
        o = object.__new__(task_cls, p)
        o.__init__(p)
        return o

    def get_task_creator(self, name_task: str):
        """Метод получение TASK"""
        creator = self.__creators.get(name_task)
        if not creator:
            raise ValueError(name_task)
        return creator
