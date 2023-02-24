import unittest

from scheduler import Scheduler
from core.job import Job

from tests.common.test_empty_task import TestEmptyTask
from tests.common.test_job_repository import TestJobRepository
from tests.common.test_queue_processor import TestQueueProcessor


class SchedulerTest(unittest.TestCase):
    def test_job_deskription_convert_datetime_from_string_to_datetime(self):
        pass


if __name__ == '__main__':
    unittest.main()