import os.path


DATA_PATH_POSTS = os.path.join("data", "posts.json")
DATA_PATH_COMMENTS = os.path.join("data", "comments.json")
DATA_PATH_BOOKMARKS = os.path.join("data", "bookmarks.json")

LOGGER_API_PATH = os.path.join("logs", "api.log")
LOGGER_VIEWS_PATH = os.path.join("logs", "views.log")
LOGGER_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
DATA_PATH = 'data/data.json'
UPLOAD_FOLDER = "./uploads/images/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 2048 * 2048
