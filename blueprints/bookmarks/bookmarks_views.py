from flask import Blueprint, render_template, redirect

from implemented import bookmarks_services
from implemented import post_services

bookmarks_blueprint = Blueprint('bookmarks', __name__)


@bookmarks_blueprint.get("/bookmarks/")
def all_bookmark():
    """
    Представление со всеми сохраненными закладками.
    :return: bookmarks.html.
    """
    bookmarks: dict = bookmarks_services.get_all_bookmarks()
    return render_template("bookmarks.html", bookmarks=bookmarks)


@bookmarks_blueprint.get('/bookmarks/add/<int:post_pk>/')
def add_bookmarks(post_pk: int):
    """
    Представление добавления поста в закладки.
    :param post_pk: pk поста.
    :return: None.
    """
    post: dict = post_services.get_post_by_pk(post_pk)
    bookmarks_services.add_post_to_bookmarks(post)
    return redirect('/', code=302)


@bookmarks_blueprint.get('/bookmarks/remove/<int:post_pk>/')
def remove_bookmarks(post_pk: int):
    """
    Представление удаления поста из закладок.
    :param post_pk: pk поста.
    :return: None.
    """
    post: dict = post_services.get_post_by_pk(post_pk)
    bookmarks_services.remove_post_from_bookmarks(post)
    return redirect('/bookmarks/', code=302)
