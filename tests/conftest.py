import os

import pytest as pytest

from blueprints.posts.dao.posts_dao import PostsDAO
from blueprints.comments.dao.comments_dao import CommentsDAO


@pytest.fixture(scope='function')
def post_dao():
    post_dao_instance = PostsDAO(os.path.join("tests", "post_mock.json"))
    # post_dao_instance = PostsDAO(os.path.join("post_mock.json")) # раскоментить если запускать через кнопку)
    return post_dao_instance


@pytest.fixture(scope='function')
def comment_dao():
    comment_dao_instance = CommentsDAO(os.path.join("tests", "comments_mock.json"))
    # comment_dao_instance = CommentsDAO(os.path.join("comments_mock.json")) # раскоментить если запускать через кнопку)
    return comment_dao_instance
