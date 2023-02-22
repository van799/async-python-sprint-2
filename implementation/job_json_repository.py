from core.job_repository import JobRepository
import json
from core.job import Job


class JobJsonRepository(JobRepository):
    def __init__(self, reader_writer, job_factory):
        super().__init__()
        self.__reader_writer = reader_writer
        self.__job_factory = job_factory

    def get_jobs(self):
        jobs = []
        data = self.__reader_writer.read()
        json_jobs = json.load(data)
        for item in json_jobs:
            job = Job.get_job(item)
            jobs.append(job)
        return jobs

    def save_jobs(self, jobs):
        job_descriptors = []
        for job in jobs:
            job_descriptors.append(job.get_job_descriptor())
        json_jobs = json.dumps(job_descriptors, indent=4)
        self.__reader_writer.write(json_jobs)
        return
