from blueprints.posts.dao.posts_dao import PostsDAO


class PostService:

    def __init__(self, dao: PostsDAO):
        self.dao = dao

    def get_posts_all(self):
        return self.dao.get_posts_all()

    def get_post_by_pk(self, pk):
        return self.dao.get_post_by_pk(pk)

    def get_posts_by_user(self, user_name):
        return self.dao.get_posts_by_user(user_name)

    def search_for_posts(self, substring) -> list:
        """ Возвращает список постов по ключевому слову"""
        return self.dao.search_for_posts(substring)

    def get_posts_with_tags(self, tag):
        """ Возвращает посты по тэгами"""
        return self.dao.get_posts_with_tags(tag)

    def convert_tags_to_links(self, post):
        """ Возвращает посты по тэгами"""
        return self.dao.convert_tags_to_links(post)
