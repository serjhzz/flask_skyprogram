from blueprints.posts.dao.posts_dao import PostsDAO
from blueprints.comments.dao.comments_dao import CommentsDAO
from blueprints.bookmarks.dao.bookmarks_dao import BookmarksDAO

from service.post_service import PostService
from service.comments_service import CommentService
from service.bookmarks_service import BookmarkService

from config import DATA_PATH_BOOKMARKS, DATA_PATH_COMMENTS, DATA_PATH_POSTS


posts_dao = PostsDAO(DATA_PATH_POSTS)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)
bookmarks_dao = BookmarksDAO(DATA_PATH_BOOKMARKS)

post_services = PostService(dao=posts_dao)
comments_services = CommentService(dao=comments_dao)
bookmarks_services = BookmarkService(dao=bookmarks_dao)
