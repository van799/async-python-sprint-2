import datetime

class JobDescriptor:

    def __init__(self, dict=None):
        
        #job_name = ''
        self.task_name = ''
        self.task_param = ''
        self.start_at = None,
        self.max_working_time = -1,
        self.tries = 0,
        self.dependencies = []

        if(dict == None):
            return
        #job_name = dict['job_name']
        self.task_name = dict['task_name']
        self.task_param = dict['task_param']
        self.start_at = None
        if(not dict['start_at'] in (None, '')):
            self.start_at =  datetime.strptime(dict['start_at'], '%Y-%m-%d %H:%M:%S')

        self.max_working_time = dict['max_working_time']
        self.tries = dict['tries']
        self.dependencies = dict['dependencies']

