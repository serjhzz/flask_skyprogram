import json
from json import JSONDecodeError

from exceptions.data_exceptions import DataSourceError


class CommentsDAO:
    """
    Менеджер комментариев
    """

    def __init__(self, path: str):
        """
        При создании экземпляра DAO нужно указать путь к файлу с данными.
        :param path: Путь к файлу с данными
        """
        self.path = path

    def load_data_comments(self) -> list[dict]:
        """
        Метод загрузки данных из JSON.
        :return: Список словарей.
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из файла {self.path}')
        return posts_data

    def get_comments_by_post_pk(self, post_pk: int) -> list[dict]:
        """
        Метод получения комментариев к посту.
        :param post_pk: pk поста.
        :return: Список всех комментариев к определенному посту по его pk.
        """
        comments: list = self.load_data_comments()
        comments_match: list = [comment for comment in comments if post_pk == comment["post_id"]]
        return comments_match
