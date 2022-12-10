from bson import ObjectId
from pymongo import ReturnDocument
from domain.comment.comment_entity import Comment
from bson.errors import InvalidId
from pymongo.errors import ServerSelectionTimeoutError

class CommentRepositoryError:
    
    def __init__(self):
        self.name = "GENERIC_COMMENT_REPOSITORY_ERROR"
        self.message = "An unknown error occurred, please contact developer"

class CommentRepositoryErrorExtra(CommentRepositoryError):

    def __init__(self):
        super().__init__()
        self.extra_message = "Something must have gone wrong"
    
class TimeoutConnectionError(CommentRepositoryErrorExtra):

    def __init__(self, extra_message: str):
        super().__init__()
        self.name = "COMMENT_REPOSITORY_TIMEOUT_ERROR"
        self.message = "Connection with the database has timed out"
        self.extra_message = extra_message

class CommentRepository:

    def __init__(self, comment_repository_config):
        self.get_comment_collection = comment_repository_config

    def create_comment(self, comment: Comment) -> Comment \
                                            | TimeoutConnectionError \
                                            | None:
        comment_dict = comment.dict()
        del comment_dict["comment_id"]
        try:
            res = self.get_comment_collection().insert_one(comment_dict)
        except ServerSelectionTimeoutError as e:
            return TimeoutConnectionError(extra_message=e._message)
        comment.comment_id = str(res.inserted_id)
        return comment
    
    def find_comment_by_project_id(self, project_id: str) -> Comment \
                                            | TimeoutConnectionError \
                                            | None:
        try:          
            res = self.get_comment_collection().find({"project_id": project_id})
        except ServerSelectionTimeoutError as e:
            return TimeoutConnectionError(extra_message=e._message)
        ret = []
        try:
            for comment in res:
                comment["comment_id"] = str(comment["_id"])
                ret.append(Comment.parse_obj(comment))
            return ret[::-1]
        except ServerSelectionTimeoutError as e:
            return TimeoutConnectionError(extra_message=e._message)

    def update_comment(self, comment: Comment) -> Comment \
                                                    | TimeoutConnectionError \
                                                    | None:
        try:
            _id = ObjectId(comment.comment_id)
            try:
                res = self.get_comment_collection().find_one_and_replace({"_id": _id}, comment.dict(), return_document=ReturnDocument.AFTER)
            except ServerSelectionTimeoutError as e:
                return TimeoutConnectionError(extra_message=e._message)
            if not res:
                return None
            res["comment_id"] = str(res["_id"])
            comment = Comment.parse_obj(res)
            return comment
        except InvalidId:
            return None