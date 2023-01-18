import logging

from flask import Blueprint, jsonify, abort

from implemented import post_services

api_blueprint = Blueprint("api", __name__)
api_logger = logging.getLogger("api_logger")


@api_blueprint.get('/')
def api_posts_hello():
    return "Смотри документацию"


@api_blueprint.get('/posts/')
def api_posts_all() -> tuple:
    """
    Эндпойнт всех постов.
    :return: json.
    """
    all_posts: list[dict] = post_services.get_posts_all()
    all_posts_as_dicts: list[dict] = ([post for post in all_posts])
    api_logger.debug(f"All posts requested")
    return jsonify(all_posts_as_dicts), 200


@api_blueprint.get('/posts/<int:post_pk>/')
def api_posts_single(post_pk: int) -> tuple:
    """
    Эндпойнт для одного поста.
    :param post_pk: pk поста.
    :return: json.
    """
    post: dict = post_services.get_post_by_pk(post_pk)
    if post is None:
        api_logger.debug(f"Referring to a non-existent post {post_pk}")
        abort(404)
    api_logger.debug(f"Post requested {post_pk}")
    return jsonify(post), 200


@api_blueprint.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Error {error}")
    return jsonify({"error": str(error)}), 404
