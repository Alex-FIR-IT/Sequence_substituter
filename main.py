from managers import FileManager


def main():
    text_filepath = FileManager.get_filepath()
    text = FileManager.get_from_txt(filepath=text_filepath)
    subs_dict = FileManager.get_from_json()

    result_text = FileManager.get_text_after_substitution(initial_text=text, subs_dict=subs_dict)
    FileManager.save_to_file(text=result_text)


if __name__ == '__main__':
    main()
    print('Замены выполнены')
