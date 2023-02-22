import os.path

from core.read_write import ReaderWriter


class FileReadWrite(ReaderWriter):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name

    def read(self):
        with open(self.__file_name, 'a+') as user_file:
            file_contents = user_file.read()
            return file_contents

    def write(self, data):
        with open(self.__file_name, 'w') as outfile:
            outfile.write(data)
