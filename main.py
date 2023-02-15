from job import Job
from scheduler import Scheduler
from utils.utils import DELAY_START_TIME

if __name__ == '__main__':

    create_file_job = Job('create_file')
    read_from_file_job = Job(
        'read_from_file',
        tries=3,
        dependencies=[create_file_job]
    )
    write_to_file_job = Job('write_to_file')
    delete_file_job = Job(
        'delete_file',
        dependencies=[create_file_job, write_to_file_job, read_from_file_job]
    )
    create_dir_job = Job('create_dir', start_at=DELAY_START_TIME)
    delete_dir_job = Job('delete_dir', dependencies=[create_dir_job])
    get_whether = Job('get_whether')

    scheduler = Scheduler(pool_size=7)

    # расписания задач
    scheduler.schedule([
        delete_file_job,
        read_from_file_job,
        create_file_job,
        write_to_file_job,
        create_dir_job,
        delete_dir_job,
        get_whether
    ])

    scheduler.run()
