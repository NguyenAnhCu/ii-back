from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bd70b9c3a2566b:6cade5ff@eu-cdbr-west-03.cleardb.net/heroku_0dbbbf44bb63069'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 90
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
db = SQLAlchemy(app)
CORS(app, support_credentials=True)
###Models####
 
class User(db.Model):
    __tablename__ = "User"
    id_user = db.Column(db.Integer, primary_key=True)
    user_pseudo = db.Column(db.String(20))
    user_score = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,user_pseudo, user_score):
        self.user_pseudo = user_pseudo
        self.user_score = user_score
    
    def __repr__(self):
        return '' % self.id_user

class Questions(db.Model):
    class Questions(db.Model):
    __tablename__ = "Questions"
    id_question = db.Column(db.Integer, primary_key=True)
    imageQuestion = db.Column(db.String(20))
    type_question = db.Column(db.String(20))
    description = db.Column(db.String(100))
    answer_correct = db.Column(db.String(100))
    explination = db.Column(db.String(100))
    option_1 = db.Column(db.String(30))
    option_2 = db.Column(db.String(30))
    option_3 = db.Column(db.String(30))
    option_4 = db.Column(db.String(30))
    option_5 = db.Column(db.String(30))
    option_6 = db.Column(db.String(30))
    option_7 = db.Column(db.String(30))

    #question_choices = relationship("QuestionChoices", backref="Questions")

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,imageQuestion, type_question, description, answer_correct, explination, option_1, option_2, option_3, option_4, option_5, option_6, option_7):
        self.imageQuestion = imageQuestion
        self.type_question = type_question
        self.description = description
        self.answer_correct = answer_correct
        self.explination = explination
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.option_5 = option_5
        self.option_6 = option_6
        self.option_7 = option_7
    
    def __repr__(self):
        return '' % self.id_question

class QuestionChoices(db.Model):
    __tablename__ = "Question_Choices"
    id_choice = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, ForeignKey('Questions.id_question'))
    is_right_choice = db.Column(db.Enum('N','Y'))
    choice = db.Column(db.String(20))

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,is_right_choice, choice):
        self.is_right_choice = is_right_choice
        self.choice = choice
    
    def __repr__(self):
        return '' % self.id_choice

db.create_all()

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session
    id_user = fields.Number(dump_only=True)
    user_pseudo = fields.String(required=True)
    user_score = fields.Number(required=True)

class QuestionsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Questions
        sqla_session = db.session
    id_question = fields.Number(dump_only=True)
    imageQuestion = fields.String(required=True)
    type_question = fields.String(required=True)
    description = fields.String(required=True)
    answer_correct = fields.String(required=True)
    explination = fields.String(required=True)
    option_1 = fields.String(required=True)
    option_2 = fields.String(required=True)
    option_3 = fields.String(required=True)
    option_4 = fields.String(required=True)
    option_5 = fields.String(required=True)
    option_6 = fields.String(required=True)
    option_7 = fields.String(required=True)

@app.route('/api/user/create', methods = ['POST'])
@cross_origin(supports_credentials=True)
def create_user():
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)
    result = user_schema.dump(user.create())
    return make_response(jsonify({"user": result}),200)

# endpoint to show all users
@app.route("/api/user", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_users():
    get_user = User.query.all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_user)
    return make_response(jsonify({"users": users}))

# endpoint to show 5 best users score
@app.route("/api/user/bestfive", methods=["GET"])
def get_five_users():
    get_user = User.query.order_by(User.user_score.desc()).limit(5).all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_user)
    return make_response(jsonify({"users": users}))


# endpoint to get user detail by id
@app.route("/api/user/<int:id>", methods=["GET"])
def user_detail(id):
    get_product = User.query.get(id)
    user_schema = UserSchema()
    user = user_schema.dump(get_product)
    return make_response(jsonify({"user": user}))


# endpoint to delete user
@app.route("/api/user/<int:id>", methods=["DELETE"])
def delete_product_by_id(id):
    get_user = User.query.get(id)
    db.session.delete(get_user)
    db.session.commit()
    return make_response("",204)

# endpoint to show all Question
@app.route("/api/questions", methods=["GET"])
def get_questions():
    get_questions = Questions.query.all()
    questions_schema = QuestionsSchema(many=True)
    questions = questions_schema.dump(get_questions)
    listoption = [questions[0]["option_1"],questions[0]["option_2"],questions[0]["option_3"],questions[0]["option_4"],questions[0]["option_5"],questions[0]["option_6"],questions[0]["option_7"]]
    questions[0]["listoption"] = listoption
    for i in range(1,9):
        del questions[0]["option_"+str(i)]
    return make_response(jsonify(questions))

# endpoint to show a specific Question
@app.route("/api/questions/<int:id>", methods=["GET"])
def get_questions_by_id(id):
    get_question = Questions.query.get(id)
    question_schema = QuestionsSchema()
    question = question_schema.dump(get_question)
    listoption = [question["option_1"],question["option_2"],question["option_3"],question["option_4"],question["option_5"],question["option_6"],question["option_7"]]
    question["listoption"] = listoption
    for i in range(1,8):
        del question["option_"+str(i)]
    return make_response(jsonify(question))

# endpoint to show a Question by type question
@app.route("/api/questions/<string:tyquestion>", methods=["GET"])
def get_question_by_type(tyquestion):
    get_question = Questions.query.filter(Questions.type_question == tyquestion).all()
    question_schema = QuestionsSchema(many=True)
    question = question_schema.dump(get_question)
    return make_response(jsonify(question))

# endpoint to show a Question by type question and by id
@app.route("/api/questions/<string:tyquestion>/<int:id>", methods=["GET"])
def get_question_by_type_id(tyquestion,id):
    get_question = Questions.query.filter(Questions.type_question == tyquestion, Questions.id_question == id).first()
    question_schema = QuestionsSchema()
    question = question_schema.dump(get_question)
    return make_response(jsonify(question))

if __name__ == "__main__":
    app.run(debug=True)