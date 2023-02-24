from datetime import datetime

class SchedulerConfig():
    def __init__(self):
        self.__pool_size = 10
        self.__datetime_format = datetime().isoformat()
        self.__file_name = './data/scheduler.dat'

    @property
    def pool_size():
        return self.__pool_size
    
    @property
    def datetime_format():
        return self.__datetime_format
    
    @property
    def filename(self):
        return self.__file_name

    @staticmethod
    def GetConfig():
        return SchedulerConfig()




