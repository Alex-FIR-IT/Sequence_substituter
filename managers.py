import json


class FileManager:

    @staticmethod
    def get_filepath() -> str:
        """Получает путь до файла, который нужно изменить"""

        return input("Введите путь к файлу: \n> ")

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
