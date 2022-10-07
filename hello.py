from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "hello": "world",
    }

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

