import json
from json import JSONDecodeError

from exceptions.data_exceptions import DataSourceError


class BookmarksDAO:
    """
    Менеджер закладок
    """

    def __init__(self, path: str):
        """
        При создании экземпляра DAO нужно указать путь к файлу с данными.
        :param path: Путь к файлу с данными
        """
        self.path = path

    def get_all_bookmarks(self) -> dict:
        """
        Метод получения всех закладок.
        :return:
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                bookmarks_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из файла {self.path}')
        return bookmarks_data

    def add_post_to_bookmarks(self, post: dict) -> None:
        """
        Метод добавления закладки.
        :param post: Словарь с постом.
        :return: None.
        """
        with open("data/bookmarks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        data.append(post)
        with open("data/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def remove_post_from_bookmarks(self, post: dict) -> None:
        """
        Метод удаления закладки.
        :param post: Словарь с постом.
        :return: None.
        """
        with open("data/bookmarks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        data.remove(post)
        with open("data/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
