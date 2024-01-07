import json
import os
import re

from decorators import retry


class FileManager:

    @staticmethod
    @retry
    def get_filepath() -> str:
        """Получает путь до файла, который нужно изменить"""

        filepath = input("Введите путь к файлу: \n> ")

        if not os.path.exists(path=filepath):
            raise FileNotFoundError()

        return filepath

    @staticmethod
    def save_to_file(*, text: str, filepath: str = 'result.txt'):
        """Сохраняет текст в файл, возвращает текст, записанный в файл"""

        with open(file=filepath, mode='w') as file:
            file.write(text)

        return text

    @staticmethod
    def get_from_txt(*, filepath: str) -> str:
        """Чатает данные из txt, возвращает его содержимое"""

        with open(file=filepath, mode='r') as file:
            return file.read()

    @staticmethod
    def get_from_json(*, filepath: str = 'data.json') -> dict:
        """Читает данные из json, возвращая его содержимое в виде словаря"""

        with open(file=filepath, mode='r') as file:
            return json.load(fp=file)

    @staticmethod
    def write_to_json(*, filepath: str = 'data.json', data_dict: dict) -> dict:
        """Записывает словарь в json формат, возвращает записанный словарь"""

        with open(file=filepath, mode='w') as file:
            json.dump(obj=data_dict, fp=file, ensure_ascii=False, indent=4)

        return data_dict

    @staticmethod
    def get_text_after_substitution(*, initial_text: str, subs_dict: dict) -> str:
        result_text = initial_text

        for old_sequence, new_sequence in subs_dict.items():
            result_text = re.sub(pattern=old_sequence,
                                 repl=new_sequence,
                                 string=result_text
                                 )

        if result_text == initial_text:
            print('Программа не выполнила ни одной замены!')

        return result_text
