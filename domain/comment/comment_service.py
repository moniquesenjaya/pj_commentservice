from adapter.repository.comment_repository import CommentRepository, TimeoutConnectionError
from domain.comment.comment_entity import Comment
import io, base64, binascii

class CommentServiceError:
    def __init__(self):
        self.name = "ERROR"
        self.message = "An unspecific error occurred, please contact developer"

class CommentServiceErrorExtra(CommentServiceError):
    def __init__(self):
        self.extra_message = ""

class CommentNotFound(CommentServiceError):
    
    def __init__(self, comment_id: str):
        super().__init__()
        self.name = "COMMENT_NOT_EXIST"
        self.message = f"project with id '{comment_id}' was not found"

class DatabaseConnectionError(CommentServiceErrorExtra):
    
    def __init__(self, extra_message: str):
        super().__init__()
        self.name = "DATABASE_CONNECTION_ERROR"
        self.message = "There was a problem connecting to the database"
        self.extra_message = extra_message


class CommentService:
    
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        
    def create_comment(self, comment: Comment) -> Comment | CommentServiceErrorExtra:
        res = self.comment_repository.create_comment(comment)
        if isinstance(res, TimeoutConnectionError):
            return DatabaseConnectionError(res.extra_message)
        return res

    def find_comment_by_project_id(self, project_id: str) -> list[Comment] | CommentServiceError:
        comments = self.comment_repository.find_comment_by_project_id(project_id)
        if isinstance(comments, TimeoutConnectionError):
            return DatabaseConnectionError(comments.extra_message)
        
        return comments

    def update_comment(self, comment: Comment) -> Comment | CommentServiceError:
        updated_comment = self.comment_repository.update_comment(comment)
        if isinstance(updated_comment, TimeoutConnectionError):
            return DatabaseConnectionError(updated_comment.extra_message)
        
        if not updated_comment:
            return CommentNotFound(comment.comment_id if not (comment.comment_id is None) else "None")
        return updated_comment
