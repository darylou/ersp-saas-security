from app import app
from flask import abort, request

@app.get("/api/paste")
def get_paste():
    # user = request.form['user']

    # TODO: Query database container for paste
    title = "My Paste"
    body = "This is my paste."
    
    return {
        "title": title,
        "body": body,
    }


@app.post("/api/paste")
def post_paste():
    return {
        "stub": "stub",
    }