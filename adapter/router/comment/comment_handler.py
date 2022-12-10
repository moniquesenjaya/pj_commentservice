import io
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from domain.comment.comment_service import CommentService

from domain.comment.comment_service import CommentServiceError, CommentServiceErrorExtra
from domain.comment.comment_entity import Comment
from pydantic import BaseModel

class CreateCommentResponse(BaseModel):
    message: str
    comment: Comment | None

class UpdateCommentResponse(BaseModel):
    message: str
    comment: Comment | None

class FindCommentByProjectIdResponse(BaseModel):
    message: str
    comments: list[Comment] | None

class CommentHandler:

    def __init__(self, comment_service: CommentService):
        self.comment_service = comment_service

    def create_comment(self, comment: Comment) -> JSONResponse:
        res = self.comment_service.create_comment(comment)
        if isinstance(res, CommentServiceErrorExtra):
            content = jsonable_encoder(CreateCommentResponse(
                message=f"{res.name}: {res.message}. {res.extra_message}",
                comment=None
            ))
            return JSONResponse(content=content, status_code=500, media_type="application/json")
            
        else:
            comment = res
            create_comment_response = jsonable_encoder(CreateCommentResponse(
                message="comment was successully created",
                comment=comment
            ))
            return JSONResponse(content=create_comment_response, status_code=200, media_type="application/json")

    def update_comment(self, comment: Comment) -> JSONResponse:
        res = self.comment_service.update_comment(comment)
        if isinstance(res, CommentServiceErrorExtra):
            content = jsonable_encoder(CreateCommentResponse(
                message=f"{res.name}: {res.message}. {res.extra_message}",
                comment=None
            ))
            return JSONResponse(content=content, status_code=500, media_type="application/json")
        else:
            comment = res
            update_comment_response = jsonable_encoder(UpdateCommentResponse(
                message="comment was successfully updated",
                comment=comment
            ))
            return JSONResponse(content=update_comment_response, status_code=200, media_type="application/json")

    def find_comment_by_project_id(self, project_id: str) -> JSONResponse:
        
        res = self.comment_service.find_comment_by_project_id(project_id)
        if isinstance(res, CommentServiceErrorExtra):
            content = jsonable_encoder(CreateCommentResponse(
                message=f"{res.name}: {res.message}. {res.extra_message}",
                comment=None
            ))
            return JSONResponse(content=content, status_code=500, media_type="application/json")
    
        else:
            content = jsonable_encoder(FindCommentByProjectIdResponse(
                message="below are the comments found",
                comments=res
            ))
            return JSONResponse(content=content, status_code=200, media_type="application/json")
    
   
