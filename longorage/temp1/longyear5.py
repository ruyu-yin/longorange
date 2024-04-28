from flask import Flask, request

app = Flask(__name__)


@app.route('/example')
def example():
    key1 = request.args.getlist('key1')  # 返回一个列表，包含所有 'key1' 的值
    key1_value = request.args.get('key1')  # 如果 'key1' 存在，返回其第一个值；否则返回 None
    return f"key1: {key1}, key1_value: {key1_value}"

if __name__ == "__main__":
    app.run(debug=True)