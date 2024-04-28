class User:
    def __init__(self, name):
        self.rr= name

    def __repr__(self):
        return '<User %r>' % self.rr

    # 创建一个User对象


user = User('ruyu')

# 直接打印这个对象
print(user)  # 输出: <User 'Alice'>