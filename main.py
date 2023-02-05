import uvicorn
from fastapi import FastAPI
import datetime 
from dotenv import load_dotenv
import os
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from adapter.router.comment import comment_router as comment

# load_dotenv()
COMMENT_BASE_PATH = os.getenv("BASE_PATH")
VERSION_1 = os.getenv("VERSION_1")
FE_URL = os.getenv("FE_URL")

app = FastAPI()
app.include_router(
    comment.router,
    prefix=f"{COMMENT_BASE_PATH}{VERSION_1}",
)

origins = [
    FE_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", tags=["Root"])
def read_root():
    now = datetime.datetime.now()
    return f"[{str(now)}] comment_service is ok"

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Comment Service",
        version="1.0.0",
        description="Schema for the comment service",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)
