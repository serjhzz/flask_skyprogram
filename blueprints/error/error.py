import logging
from flask import Blueprint, render_template

page_error = Blueprint('page_error', __name__)
views_logger = logging.getLogger("views_logger")


@page_error.errorhandler(404)
def pageNotFound(error):
    """
    Обработчик запросов к несуществующим страницам.
    :param error: Ошибка.
    :return: 404.html.
    """
    views_logger.debug(f"Page Not Found - {error}")
    return render_template('404.html', title="Страница не найдена", error=error)


@page_error.errorhandler(500)
def pageNotFound(error):
    """
    Обработчик ошибок, возникших на стороне сервера.
    :param error: Ошибка.
    :return: 500.html.
    """
    views_logger.debug(f"Page Not Found - {error}")
    return render_template('500.html', title="Сервер не отвечает", error=error)
