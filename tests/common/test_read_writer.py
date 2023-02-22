from core.read_write import ReaderWriter


class TestReadWrite(ReaderWriter):
    def __init__(self, file_content=''):
        super().__init__()
        self.__file_content = file_content

    @property
    def file_content(self):
        return self.__file_content

    def read(self):
        return self.__file_content

    def write(self, data):
        self.__file_content = data
