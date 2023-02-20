from core.job_repository import JobRepository
import json


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
            task_name = item.task_name
            job_creator = self.__job_factory.get_job_creator(task_name)
            job = job_creator(item.start_at,
                              item.max_working_time,
                              item.tries,
                              item.dependencies)
            jobs.append(job)
        return jobs

    def save_jobs(self, jobs):
        json_jobs = json.dumps(jobs, indent=4)
        self.__reader_writer.write(json_jobs)
        return
