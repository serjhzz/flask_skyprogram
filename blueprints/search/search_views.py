import logging

from flask import Blueprint, render_template, request

from implemented import post_services

search_blueprint = Blueprint("search_blueprint", __name__)
views_logger = logging.getLogger("views_logger")


@search_blueprint.get("/search/")
def page_posts_by_search():
    """
    Представление результата поиска.
    :return: search.html.
    """
    query: str = request.args.get("s", "")
    if query == "":
        posts: list = []
    else:
        posts = post_services.search_for_posts(query)
    return render_template("search.html", posts=posts, query=query, posts_len=len(posts))


@search_blueprint.route("/tag/<tagname>/")
def tag_page(tagname):
    """
    Представление результата поиска по тегам.
    :param tagname: Наименование тега.
    :return: tag.html.
    """
    posts_with_tags = post_services.get_posts_with_tags(tagname)
    return render_template('tag.html', posts_with_tags=posts_with_tags, tag=tagname)
