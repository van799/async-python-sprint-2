class JobQueueDispatcher:
    """Класс управляет обработкой Job"""

    def __init__(self, queue: []):
        self.__queue = queue

    def get_jobs_to_run(self) -> []:
        """Метод возвращает Job которые нужно обработать"""
        job_candidates = []
        for job in self.__queue:

            if job.done or job.done_with_error:
                continue
            if not self.__check_job_dependencies(job):
                continue

            job_candidates.append(job)
        return job_candidates

    def __check_job_dependencies(self, job) -> None:
        """Метод проверяет Job dependencies"""
        for dependence_job_id in job.dependencies:
            job = next(filter(lambda o: o.job_id == dependence_job_id, self.__queue), None)
            if job is None:
                continue
            if not job.done:
                return False
        return True

    def add_jobs_to_queue(self, jobs) -> None:
        """Метод добавляет Jobs в очередь"""
        self.__queue.extend(jobs)

    def add_job_to_queue(self, job) -> None:
        """Метод добавляет Job в очередь"""
        self.__queue.append(job)

    def get_all_jobs(self) -> None:
        """Метод возвращает Job из очереди"""
        return self.__queue
