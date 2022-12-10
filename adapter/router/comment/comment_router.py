from fastapi import APIRouter, Body, UploadFile
import adapter.router.comment.example as EXAMPLE
from adapter.router.comment.comment_handler import CommentHandler
from domain.comment.comment_service import CommentService
from adapter.repository.comment_repository import CommentRepository
from adapter.repository.config import get_database
from adapter.router.comment.comment_handler import  CreateCommentResponse, \
                                                    UpdateCommentResponse, \
                                                    FindCommentByProjectIdResponse

from domain.comment.comment_entity import Comment

router = APIRouter()
comment_handler = CommentHandler(
    comment_service=CommentService(
        comment_repository=CommentRepository(
            comment_repository_config=lambda: get_database()["comment"]
        )
    )
)

@router.post(
        "/",
        response_model=CreateCommentResponse,
        responses={
            200: {
                "description": "Comment successfully created",
                "content": {
                    "application/json": {
                        "example": EXAMPLE.CREATE_COMMENT_RESPONSE
                    }
                }
            }
        }
    )
def create_comment(comment: Comment = Body(example=EXAMPLE.CREATE_COMMENT_REQUEST_BODY)):
    return comment_handler.create_comment(comment)

@router.put(
    "/",
    response_model=UpdateCommentResponse,
    responses={
        200: {
            "description": "Comment successfully updated",
            "content": {
                "application/json": {
                    "example": EXAMPLE.UPDATE_COMMENT
                    }
                }
            }
        }
)
def update_commment(comment: Comment):
    return comment_handler.update_comment(comment)

@router.get(
    "/project/{project_id}",
    response_model=FindCommentByProjectIdResponse,
    responses={
            200: {
                "description": "Comments Found",
                "content": {
                    "application/json": {
                        "example": EXAMPLE.FIND_COMMENT_BY_PROJECT_ID_RESPONSE
                    }
                }
            }
        }
)
def find_comment_by_project_id(project_id: str):
    return comment_handler.find_comment_by_project_id(project_id)

