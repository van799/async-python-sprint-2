import os.path
from pathlib import Path

from core.read_write_base import ReaderWriterBase


class FileReadWrite(ReaderWriterBase):
    """Класс отвечает за создание, чтение, и записи не выполненных TASK"""
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name

    def read_or_create(self):
        filename = Path(self.__file_name)
        filename.touch(exist_ok=True)  # will create file, if it exists will do nothing
        with open(self.__file_name, 'r') as user_file:
            file_contents = user_file.read()
            return file_contents

    def write(self, data):
        with open(self.__file_name, 'w') as outfile:
            outfile.write(data)
