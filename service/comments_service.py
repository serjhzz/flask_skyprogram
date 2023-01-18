from blueprints.comments.dao.comments_dao import CommentsDAO


class CommentService:
    def __init__(self, dao: CommentsDAO):
        self.dao = dao

    def load_data_comments(self):
        return self.dao.load_data_comments()

    def get_comments_by_post_pk(self, comment_id):
        return self.dao.get_comments_by_post_pk(comment_id)
