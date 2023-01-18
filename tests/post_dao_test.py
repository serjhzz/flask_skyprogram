import pytest as pytest


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        print('field', field)
        assert field in post, f"Нет поля {field}"


class TestPostsDAO:
    # Функция получения всех

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "Incorrect type for result"
        post = post_dao.get_posts_all()[0]
        assert type(post) == dict, "Incorrect type for result single item"

    def test_get_all_fields(self, post_dao):
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_posts_all()
        correct_pks = {1, 2, 3}
        pks = set([post['pk'] for post in posts])
        assert pks == correct_pks, "Не совпадают полученные ID"

    # Функция получения одного по pk

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        assert type(post) == dict, "Incorrect type for result single item"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        print(post)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None, "Should be None for non existent pk"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post['pk'] == pk, f"Incorrect post.pk for request post with pk == {pk}"

    # Функция получения постов по вхождению строки

    def test_search_in_content_types(self, post_dao):
        posts = post_dao.search_for_posts("ага")
        assert type(posts) == list, "Incorrect type for result"
        post = post_dao.get_posts_all()[0]
        assert type(post) == dict, "Incorrect type for result single item"

    def test_search_in_content_fields(self, post_dao):
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_search_in_content_not_found(self, post_dao):
        posts = post_dao.search_for_posts("999")
        assert posts == [], "Should be [] for not substring not found"

    @pytest.mark.parametrize("s, expected_pks", [("Ага", {1}), ("Пошел", {2}), ("на", {1, 2, 3})])
    def test_search_in_content_results(self, post_dao, s, expected_pks):
        posts = post_dao.search_for_posts(s)
        pks = set([post['pk'] for post in posts])
        assert pks == expected_pks, f"Incorrect results searching for {s}"
