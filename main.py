from flask import Flask, render_template

from blueprints.api.api_views import api_blueprint
from blueprints.bookmarks.bookmarks_views import bookmarks_blueprint
from blueprints.posts.posts_views import post_blueprint
from blueprints.search.search_views import search_blueprint
from blueprints.users.users_views import user_blueprint
from blueprints.error.error import page_error
import config_logger


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(post_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(search_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(bookmarks_blueprint)
    app.register_blueprint(page_error)
    app.config.from_pyfile(config_path)
    config_logger.config(app)
    return app


app = create_and_config_app("config.py")


if __name__ == '__main__':
    app.run()
