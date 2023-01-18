import logging
from flask import Blueprint, render_template

from implemented import comments_services
from implemented import post_services

post_blueprint = Blueprint('post_blueprint', __name__)
views_logger = logging.getLogger("views_logger")


@post_blueprint.route('/')
def page_posts_index():
    """
    Представление главной страницы со всеми постами.
    :return: index.html.
    """
    all_posts = post_services.get_posts_all()
    return render_template("index.html", posts=all_posts)


@post_blueprint.get("/posts/<int:pk>/")
def page_posts_single(pk: int):
    """
    Представление страницы одного поста.
    :param pk: pk поста.
    :return: post.html.
    """
    post = post_services.get_post_by_pk(pk)
    if post is None:
        views_logger.debug(f"Post Not Found - {pk}")
        raise 'Errors 404'
    comments = comments_services.get_comments_by_post_pk(pk)
    tag_content = post_services.convert_tags_to_links(post)
    return render_template("post.html", post=tag_content, comments=comments, comments_len=len(comments))
