# encoding=utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route("/hello/")
def hello():
    # 从request中获取查询参数name的值，没有的话返回Flask
    name = request.args.get("name", "Flask")
    print("request.args:%s" % request.args)
    print("request.args.items():%s" % request.args.items())
    print("request.full_path:%s" % request.full_path)
    print("request.path:%s" % request.path)
    print("request.host:%s" % request.host)
    print("request.host_url:%s" % request.host_url)
    print("request.url:%s" % request.url)
    print("request.headers:%s\n" % request.headers)
    print("request.data:%s" % request.data)
    print("request.endpoint:%s" % request.endpoint)
    print("request.json:%s" % request.json)
    print("request.method:%s" % request.method)
    print("request.scheme:%s" % request.scheme)
    print("request.user_agent:%s" % request.user_agent)
    return "hello %s" % name


if __name__ == "__main__":
    app.run(debug=True)