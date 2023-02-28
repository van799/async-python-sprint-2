from datetime import datetime

class JobQueueDispatcher():
    def __init__(self, queue:[]):
        self.__queue = queue

    def get_jobs_to_run(self)->[]:
        
        job_candidates = []
        for job in self.__queue:
            
            if(job.done or job.done_with_error):
                continue
            if(not self.__check_job_dependencies(job)):
                continue

            job_candidates.append(job)
        return job_candidates

    def __check_job_dependencies(self, job):
        for dependence_job_id in job.dependencies:
            job = next(filter(lambda o: o.job_id==dependence_job_id, self.__queue), None)
            if job is None: continue
            if not job.done: return False
        return True
    
    def add_jobs_to_queue(self, jobs): self.__queue.extend(jobs)
 
    def add_job_to_queue(self, job): self.__queue.append(job)

    def get_all_jobs(self): return self.__queue
            
