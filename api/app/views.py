from app import app

@app.route("/")
def index():
    return "Hello from Flask in a container!"


@app.route("/messages")
def test():
    return "test"