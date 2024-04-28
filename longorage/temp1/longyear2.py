# encoding=utf-8
from flask import Flask, url_for

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return "hello %s" % name


if __name__ == "__main__":
    with app.test_request_context():
        print("####:", url_for("hello", name="test"))