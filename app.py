from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
#db = SQLAlchemy(app)

questions_put_args = reqparse.RequestParser()
questions_put_args.add_argument("response", type=str, help="The response of the question", required=True)
questions_put_args.add_argument("explication", type=str, help="The description of the response", required=True)


Questions_dict = { "Questions1" : {"response": "aozheva", "explication": "aoihzbeoab"},
                   "Questions2" : {"response": "aedvarav", "explication": "hobaozcva"} }

def abort_if_question_doesnt_exist(Question):
    if Question not in Questions_dict :
        abort(404, message="Question is not found")

def abort_if_question_exist(Question):
    if Question in Questions_dict :
        abort(409, message="Question already exist")

class Questions(Resource):
    def get(self, Question):
        abort_if_question_doesnt_exist(Question)
        return Questions_dict[Question]

    def put(self, Question):
        abort_if_question_exist(Question)
        args = questions_put_args.parse_args()
        Questions_dict[Question] = args
        return Questions_dict

api.add_resource(Questions, "/Questions/<string:Question>")

if __name__ == "__main__" :
    app.run(debug=True)