class SchedulerConfig:
    def __init__(self):
        self.__pool_size = 10
        self.__file_name = './data/scheduler.dat'

    @property
    def pool_size(self):
        return self.__pool_size

    @property
    def filename(self):
        return self.__file_name

    @staticmethod
    def GetConfig():
        return SchedulerConfig()
