import json
import os
import re
from decorators import retry


class FileManager:

    def __init__(self, filepath):
        self.filepath = filepath
        self.content = self.get_from_txt(filepath=self.filepath)

    def save_to_file(self, *, filepath: str = 'result.txt'):
        """Сохраняет текст в файл, возвращает текст, записанный в файл"""

        with open(file=filepath, mode='w') as file:
            file.write(text)

        if not os.path.exists(path=filepath):
            raise FileNotFoundError()

        return filepath

    @staticmethod
    def get_from_txt(*, filepath: str) -> str:
        """Считывает данные из txt, возвращает его содержимое"""

        with open(file=filepath, mode='r') as file:
            return file.read()

    @staticmethod
    def get_from_json(*, filepath: str = 'data.json') -> dict:
        """Читает данные из json, возвращая его содержимое в виде словаря"""

        with open(file=filepath, mode='r') as file:
            return json.load(fp=file)
