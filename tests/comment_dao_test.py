import pytest as pytest


def check_fields(comment):
    fields = ["pk", "post_id", "commenter_name", "comment"]

    for field in fields:
        assert field in comment, f"Нет поля {field}"


class TestCommentsDAO:

    def test_get_by_pk_types_c(self, comment_dao):
        comments = comment_dao.get_comments_by_post_pk(1)
        assert type(comments) == list, "Incorrect type for result single item"

    def test_get_by_pk_fields_c(self, comment_dao):
        comments = comment_dao.get_comments_by_post_pk(1)
        print(comments)
        check_fields(comments[0])

    def test_get_by_pk_none_c(self, comment_dao):
        comments = comment_dao.get_comments_by_post_pk(999)
        assert comments == [], "Should be None for non existent pk"

    @pytest.mark.parametrize("pk", [1])
    def test_get_by_pk_correct_id_c(self, comment_dao, pk):
        comments = comment_dao.get_comments_by_post_pk(pk)
        assert comments[0]['pk'] == pk, f"Incorrect post.pk for request post with pk == {pk}"
