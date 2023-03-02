import json
from job import Job
from datetime import datetime
from core.repository_base import RepositoryBase
from implementation.job_descriptor import JobDescriptor


class JobJsonRepository(RepositoryBase):
    """Класс нужен для создания класса Job при считывании не выполненных TASK из файла."""

    def __init__(self, reader_writer, task_factory):
        super().__init__()
        self.__reader_writer = reader_writer
        self.__task_factory = task_factory

    @staticmethod
    def get_job_descriptor_from_dict(dict_obj):
        """Метод получение описание Job из словаря."""
        job_descriptor = JobDescriptor()
        if 'job_id' in dict_obj.keys():
            job_descriptor.job_id = dict_obj['job_id']
        job_descriptor.task_name = dict_obj['task_name']
        job_descriptor.task_param = dict_obj['task_param']
        job_descriptor.start_at = None

        if (not dict_obj['start_at'] in (None, '')):
            job_descriptor.start_at = datetime.fromisoformat(
                dict_obj['start_at'])

        job_descriptor.max_working_time = dict_obj['max_working_time']
        job_descriptor.tries = dict_obj['tries']
        job_descriptor.dependencies = dict_obj['dependencies']

        return job_descriptor

    def get(self):
        """Метод получение описание Job из словаря."""
        jobs = []
        data = self.__reader_writer.read_or_create()
        if data in (None, ''):
            return jobs
        json_job_descriptors = json.loads(data)
        for json_descriptor in json_job_descriptors:
            descriptor = JobJsonRepository.get_job_descriptor_from_dict(
                json_descriptor)
            job = Job.get_job(descriptor, self.__task_factory)
            jobs.append(job)
        return jobs

    @staticmethod
    def __json_converter(o):
        """Метод конвертирует datetime в isoformat,
         это сделано для возможности серилизации"""
        if isinstance(o, datetime):
            return o.isoformat()
        return o.__dict__

    def save(self, jobs):
        """Метод сохраняет Jobs в репозитарий"""
        job_descriptors = []
        for job in jobs:
            job_descriptors.append(job.get_job_descriptor())

        json_jobs = json.dumps(
            job_descriptors, default=lambda o: JobJsonRepository.__json_converter(o), sort_keys=True, indent=4)
        self.__reader_writer.write(json_jobs)
        return
