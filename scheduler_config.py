class SchedulerConfig:
    def __init__(self):
        self.__pool_size = 10
        self.__file_name = './data/scheduler.dat'
        self.__log_filename = './data/logger.log'

    @property
    def pool_size(self):
        return self.__pool_size

    @property
    def filename(self):
        return self.__file_name

    @property
    def log_filename(self):
        return self.__log_filename

    @staticmethod
    def GetConfig():
        return SchedulerConfig()
