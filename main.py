from managers import FileManager


def get_text_after_substitution(*, text: str, subs_dict: dict) -> str:
    return ''


def main():
    text_filepath = FileManager.get_filepath()
    text = FileManager.get_from_txt(filepath=text_filepath)
    subs_dict = FileManager.get_from_json()

    result_text = get_text_after_substitution(text=text, subs_dict=subs_dict)
    FileManager.save_to_file(text=result_text)


if __name__ == '__main__':
    main()
    print('Замены выполнены')
