from flask import Flask, request, jsonify, make_response
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
db = SQLAlchemy(app)

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
    __tablename__ = "Questions"
    id_question = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Enum('N','Y'))

    question_choices = relationship("QuestionChoices", backref="Questions")

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self,is_active):
        self.is_active = is_active
    
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

@app.route('/api/user/create', methods = ['POST'])
def create_user():
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)
    result = user_schema.dump(user.create())
    return make_response(jsonify({"user": result}),200)

# endpoint to show all users
@app.route("/api/user", methods=["GET"])
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

if __name__ == "__main__":
    app.run(debug=True)