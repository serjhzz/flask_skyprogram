from blueprints.bookmarks.dao.bookmarks_dao import BookmarksDAO


class BookmarkService:
    def __init__(self, dao: BookmarksDAO):
        self.dao = dao

    def get_all_bookmarks(self):
        return self.dao.get_all_bookmarks()

    def add_post_to_bookmarks(self, post: dict) -> object:
        return self.dao.add_post_to_bookmarks(post)

    def remove_post_from_bookmarks(self, post: dict) -> object:
        return self.dao.remove_post_from_bookmarks(post)
