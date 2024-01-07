import logging
import datetime
from managers import FileManager

logging.basicConfig(level=logging.ERROR,
                    filename=f"substitution.ERROR.{datetime.date.today()}.log",
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    text_filepath = FileManager.get_filepath()
    text = FileManager.get_from_txt(filepath=text_filepath)
    subs_dict = FileManager.get_from_json()

    result_text = FileManager.get_text_after_substitution(initial_text=text, subs_dict=subs_dict)
    FileManager.save_to_file(text=result_text)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Программа завершена с ошибкой: \"{error}\"")
        logging.exception(msg=error, exc_info=True)
