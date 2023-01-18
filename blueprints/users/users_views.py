import logging
from flask import Blueprint, render_template

from implemented import post_services

user_blueprint = Blueprint('user_blueprint', __name__)
views_logger = logging.getLogger("views_logger")


@user_blueprint.get("/users/<user_name>/")
def page_posts_by_user(user_name: str):
    """
    Представление постов юзера.
    :param user_name: Имя пользователя.
    :return: user-feed.html.
    """
    """ Возвращает посты пользователя"""
    posts = post_services.get_posts_by_user(user_name)
    if not posts:
        views_logger.debug(f"Contacting a non-existent user {user_name}")
        raise 'Errors 404: Такого пользователя нет'

    return render_template("user-feed.html", posts=posts, user_name=user_name)
