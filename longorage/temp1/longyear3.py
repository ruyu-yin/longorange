from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the home page!'


@app.route('/about')
def about():
    return 'This is the about page.'


with app.test_request_context():
    print(url_for('home'))  # 输出 '/'
    print(url_for('about'))  # 输出 '/about'

if __name__ == '__main__':
    app.run()


"""
端点是用于在Flask内部唯一标识一个视图函数的字符串。
在Flask框架中，“端点”是一个用于唯一标识视图函数的字符串。当你在Flask中定义了一个视图函数，Flask会自动生成一个端点字符串，通常是视图函数所在的Blueprint（如果有的话）加上视图函数的名称。如果没有Blueprint，就只是视图函数的名称。

端点可以在视图函数被请求时使用，比如在模板中生成URL链接或者在JavaScript中发起AJAX请求。
在这个例子中，home和about就是两个视图函数的端点。url_for函数可以根据端点生成对应的URL。
注意：在实际的应用中，不需要手动创建端点，Flask会自动为每个视图函数生成端点。
"""