import json
import os
import re
from decorators import retry


class FileManager:

    def __init__(self, filepath):
        self.content = self.get_from_txt(filepath=filepath)
        self.filepath = filepath

    def save_to_file(self, *, filepath: str = None):
        """Сохраняет текст в файл, возвращает текст, записанный в файл"""

        if not filepath:
            filepath = self.filepath

        with open(file=filepath, mode='w') as file:
            file.write(self.content)

        return self.content

    def substitute_in_text(self, *, subs_dict: dict) -> str:
        substituted_content = self.content

        for old_sequence, new_sequence in subs_dict.items():
            substituted_content = re.sub(pattern=fr"(?:(?<=^)|(?<=\s)"
                                                 fr"{old_sequence}"
                                                 fr"(?=[\s,.!?\'\"]|$)",
                                         repl=new_sequence,
                                         string=substituted_content,
                                         flags=re.IGNORECASE
                                         )

        if substituted_content == self.content:
            print('Программа не выполнила ни одной замены!')
        else:
            print('Замены успешно выполнены!')
            self.content = substituted_content

        return self.content

    @staticmethod
    @retry
    def get_filepath() -> str:
        """Получает путь до файла, который нужно изменить"""

        filepath = input("Введите путь к файлу: \n> ")

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
