from core.read_write_base import ReaderWriterBase


class TestReadWrite(ReaderWriterBase):
    def __init__(self, file_content=''):
        super().__init__()
        self.__file_content = file_content

    @property
    def file_content(self):
        return self.__file_content

    def read_or_create(self):
        return self.__file_content

    def write(self, data):
        self.__file_content = data
