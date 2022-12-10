from pydantic import BaseModel, Field
from datetime import datetime

class Comment(BaseModel):
    comment_id: str | None
    date_time: datetime | None
    comment : str | None
    user_id: str | None
    project_id: str | None
