import json
from json import JSONDecodeError

from exceptions.data_exceptions import DataSourceError


class PostsDAO:
    """
    Менеджер постов
    """

    def __init__(self, path: str):
        """
        При создании экземпляра DAO нужно указать путь к файлу с данными.
        :param path: Путь к файлу с данными
        """
        self.path = path

    def load_data_posts(self) -> list[dict]:
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

    def get_posts_all(self) -> list[dict]:
        """
        Метод получения всего списка постов.
        :return: Список постов.
        """
        return self.load_data_posts()

    def get_post_by_pk(self, pk: int) -> dict:
        """
        Метод поиска поста по pk.
        :param pk: pk поста.
        :return: Найденный пост по pk.
        """
        if type(pk) != int:
            raise TypeError("pk must be an int")

        posts = self.load_data_posts()
        for post in posts:
            if post['pk'] == pk:
                return post

    def search_for_posts(self, substring: str) -> list[dict]:
        """
        Метод поиска поста по substring.
        :param substring: Строка поиска.
        :return: Список найденных постов.
        """
        if type(substring) != str:
            raise TypeError("substring must be an str")
        substring = substring.lower()
        posts = self.get_posts_all()
        matching_posts = [post for post in posts if substring in post['content'].lower()]
        return matching_posts

    def get_posts_by_user(self, user_name: str) -> list[dict]:
        """
        Метод поиска постов определенного автора.
        :param user_name: Имя автора.
        :return: Список найденных постов.
        """
        if type(user_name) != str:
            raise TypeError("user_name must be an str")
        user_name = user_name.lower()
        posts = self.load_data_posts()
        matching_posts = [post for post in posts if user_name.lower() in post['poster_name'].lower()]
        return matching_posts

    def get_posts_with_tags(self, tag: str) -> list[dict]:
        """
        Метод получения постов с заданным тегом.
        :param tag: Тег.
        :return: Список постов с тегами
        """
        posts = self.get_posts_all()
        posts_with_tags = []
        hashtag = '#' + tag
        for post in posts:
            if hashtag in post["content"]:
                posts_with_tags.append(self.convert_tags_to_links(post))
        return posts_with_tags

    def convert_tags_to_links(self, post: dict) -> dict:
        """
        Метод конвертации поста с тегами в теги ссылочного типа.
        :param post: Пост.
        :return: Конвертированный контент поста.
        """
        temp_content_word_list = []
        for word in post["content"].split(" "):
            if word.startswith('#'):
                temp_content_word_list.append(
                    f'<a href="/tag/{word[1:]}">{word}</a>'
                )
            else:
                temp_content_word_list.append(word)
        post["content"] = " ".join(temp_content_word_list)
        return post
