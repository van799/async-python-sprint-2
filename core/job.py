import time


class Job:
    def __init__(self,
                 task,
                 start_at=None,
                 max_working_time=-1,
                 tries=0,
                 dependencies=[]
                 ):
        self.task = task
        self.start_at = start_at
        self.max_working_time = max_working_time
        self.tries = tries
        self.dependencies = dependencies
        self.tries_count = 0
        self.__co_execute = None
        self.__coroutine = None

    def __check_dependencies(self):
        for task in self.dependencies:
            if task.complete == False:
                return False
        return True

    def __ready_to_execute(self, time_now):
        if self.__co_execute != None:
            return False
        if self.start_at != None and self.start_at >= time_now:
            return False
        if self.tries_count > self.tries and self.tries > 0:
            return False
        if self.__check_dependencies() == False:
            return False
        return True

    def run(self, time_now):
        if self.__coroutine == None:
            self.__coroutine = self.do_job(time_now)
            next(self.__coroutine)
            return
        self.__coroutine.send(time_now)

    def do_job(self, time_now):
        current_time = time_now
        while True:
            if self.__ready_to_execute(current_time) == True:
                self.tries_count += 1
                self.task.do_task()
            current_time = (yield)

    @property
    def is_running(self):
        return self.task.is_running

    @property
    def is_complete(self):
        return self.task.complete

    def pause(self):
        pass

    def stop(self):
        self.__co_execute.close()
        self.__co_execute = None
