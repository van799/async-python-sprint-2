class Scheduler:
    """Класс описывающий планировщик задач и его методы."""

    def __init__(self, logger, queue_processor, job_repository=None, pool_size=10):
        self.__logger = logger
        self.__pool_size = pool_size
        self.__is_running = False
        self.__job_repository = job_repository
        self.__queue_processor = queue_processor

    def schedule(self, job):
        """Постановка задач в очередь. Сперва проверяются есть ли запущенные задачи,
        если есть выполнение задач останавливается. В очередь можно добавить любое
        количество задач, но за один запуск планировщика будет обработано только
        то количество задач, которое соответствует pool_size планировщика. """
        self.__logger.log_info(f'Schedule job: "{job.task_name}".'
                               f' Param: "{job.task_param}"')
        was_running = self.__is_running
        if self.__is_running:
            self.stop(save=False)

        self.__queue_processor.add_job_to_queue(job)
        if was_running is True:
            self.run()

    def run(self):
        """Метод запуска задач в потоке."""
        if self.__queue_processor.is_running:
            return

        loaded_jobs = self.__load_jobs()
        self.__queue_processor.add_jobs_to_queue(loaded_jobs)
        self.__queue_processor.run()
        self.__logger.log_info('Scheduler started')

    def restart(self):
        """Метод перезапуска задач."""
        self.__queue_processor.stop()
        self.__queue_processor.run()
        self.__logger.log_info('Scheduler restart')

    def __load_jobs(self):
        if self.__job_repository is None:
            self.__logger.log_debug('Job repository is empty', 'Scheduler.__load_jobs')
            return []
        return self.__job_repository.get()

    def __save_jobs(self):
        """Метод сохранения не выполненных задач."""
        if self.__job_repository is None:
            self.__logger.log_debug('No Jobs to save', 'Scheduler.__save_jobs')
            return
        jobs_to_save = list(
            filter(
                lambda o: o.done is False or o.done_with_error is True, self.__queue_processor.get_queue())
        )
        self.__job_repository.save(jobs_to_save)

    def stop(self):
        """Метод остановки задач."""
        if not self.__queue_processor:
            self.__logger.log_debug('No queue processor', 'Scheduler.stop')
            return
        self.__queue_processor.stop()
        self.__save_jobs()
        self.__logger.log_info('Scheduler stopped')
