CREATE_COMMENT_REQUEST_BODY = {
    "date_time": "20130623T13:22-0500",
    "comment": "This is my project",
    "user_id": "412693619381",
    "project_id": "123"
}

CREATE_COMMENT_RESPONSE = {
    "comment_id": "123456329478",
    "date_time": "20130623T13:22-0500",
    "comment": "This is my project",
    "user_id": "412693619381",
    "project_id": "123"
}

UPDATE_COMMENT = {
    "comment_id": "123456329478",
    "date_time": "20130623T13:22-0500",
    "comment": "NO THIS IS MINE!",
    "user_id": "412693619381",
    "project_id": "123"
}

FIND_COMMENT_BY_PROJECT_ID_RESPONSE = [
    {
        "comment_id": "123456329478",
        "date_time": "20130623T13:22-0500",
        "comment": "NO THIS IS MINE!",
        "user_id": "412693619381",
        "project_id": "123"
    },

    {
        "comment_id": "352897814",
        "date_time": "20130623T13:22-0500",
        "comment": "nice project!",
        "user_id": "1456362343413",
        "project_id": "123"
    }
]