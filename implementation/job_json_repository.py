from core.job_repository_base import JobRepositoryBase
import json
from core.job import Job


class JobJsonRepository(JobRepositoryBase):
    def __init__(self, reader_writer, task_factory):
        super().__init__()
        self.__reader_writer = reader_writer
        self.__task_factory = task_factory

    def get_jobs(self):
        jobs = []
        data = self.__reader_writer.read()
        if data in (None, ''):
            return jobs
        json_jobs = json.loads(data, object_hook=lambda d: JobDescriptor(**d))
        for json_job in json_jobs:
            job = Job.get_job(json_job, self.__task_factory)
            jobs.append(job)
        return jobs

    def save_jobs(self, jobs):
        job_descriptors = []
        for job in jobs:
            job_descriptors.append(job.get_job_descriptor())
            json_jobs = json.dumps(
                job_descriptors, default=lambda o: o.__dict__, sort_keys=True, indent=4)

        self.__reader_writer.write(json_jobs)
        return
