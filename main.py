import logging
import datetime
from managers import FileManager

logging.basicConfig(level=logging.ERROR,
                    filename=f"substitution.ERROR.{datetime.date.today()}.log",
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    text_object = FileManager(filepath=FileManager.get_filepath())
    subs_dict = FileManager.get_from_json(filepath='data.json')

    text_object.substitute_in_text(subs_dict=subs_dict)
    text_object.save_to_file()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Программа завершена с ошибкой: \"{error}\"")
        logging.exception(msg=error, exc_info=True)
