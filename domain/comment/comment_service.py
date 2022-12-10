
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
