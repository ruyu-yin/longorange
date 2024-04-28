from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/testcases?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=False)
    cyclename = db.Column(db.String(80),unique=False)
    executionresult = db.Column(db.String(80),unique=False)
    attachment = db.Column(db.String(80),unique =False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
        # return f'<User {self.username}>'

    def as_dict(self):
        #列表推导式：获取属性和值的一一对应
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class TestCaseServerORM(Resource):
    # 如果是get请求，认为是去查询所有case
    def get(self):
        app.logger.info(request.args)
        #从数据库中获取数据：id
        case_id = request.args.get("id")
        if case_id:
            #根据id过滤获得的的数据
            case_data = TestCase.query.filter_by(id=case_id).first()
            #对获取的数据进行格式转换，转换为字典格式
            testcases = [case_data.as_dict()]
        else:
            case_data = TestCase.query.all()
            #直接展示所有的数据
            testcases = [i.as_dict() for i in case_data]
            print(testcases)
        return {"data": testcases}

    # 如果是post请求，认为是去新增case
    def post(self):
        app.logger.info(request.args)
        app.logger.info(request.json)
        # 通过接口发送的数据进行TestCaseList类的实例化
        try:
            testcase = TestCase(**request.json)
            testcase.steps = request.json.get("steps")
            app.logger.info(testcase)
            db.session.add(testcase)
            db.session.commit()
            db.session.close()
            return {
                "error": 0,
                "msg": "OK"
            }
        except:
            return {
                "error": 500,
                "msg": "server has an error!"
            }
    def delete(self):
        app.logger.info(request.args)
        _id = request.args.get("case_id")
        caseid = TestCase.query.get(_id)
        if not caseid:
            return {'error':'Case id not found'},404
        db.session.delete(caseid)
        db.session.commit()
        return  {'message': 'One case is deleted successfully'}, 200

    def put(self,case_id):
        app.logger.info(request.args)
        # _id = request.args.get(case_id)
        # if not _id:
        #      return {'error': "Case not found"},404
        data = request.get_json()
        # if not name:
        #     return {'name': "Name isn't found"},400
        case_ = TestCase.query.get(case_id)
        if 'name' in data:
            case_.name = data['name']
        if 'cyclename' in data:
            case_.cyclename = data['cyclename']
        if 'executionresult' in data:
            case_.executionresult = data['executionresult']
        if 'attachment' in data:
            case_.attachment = data['attachment']
        if 'description' in data:
            case_.description = data['description']
        if 'steps' in data:
            case_.steps = data['description']
        db.session.commit()
        return {'message': 'Updated successfully'},200

api.add_resource(TestCaseServerORM, '/testcase_orm', '/testcase_orm_2/<int:case_id>')


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True, use_reloader=True, port=5007)