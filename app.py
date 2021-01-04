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
questions_put_args.add_argument("response", type=str,
                                help="The response of the question", required=True)
questions_put_args.add_argument("explication", type=str,
                                help="The description of the response", required=True)
questions_put_args.add_argument("possibility",
                                help="All possibilities that we have for one question", required=True)
questions_put_args.add_argument("Questions_ID", type=int,
                                help="The description of the response", required=True)

Questions_dict = {"Questions1":
                      {"Questions_ID": 1,
                       "response": "aozheva",
                       "possibility": ["aozheva", "auziyevgao", "hahfhahav"],
                       "explication": "aoihzbeoab"},
                  "Questions2":
                      {"Questions_ID": 2,
                       "response": "aedvarav",
                       "possibility": ["aozheva", "auziyevgao", "hahfhahav", "aedvarav"],
                       "explication": "hobaozcva"}}

Questions_dict1 = [{"Questions_ID": 1,
                    "response": "aozheva",
                    "possibility": ["aozheva", "auziyevgao", "hahfhahav"],
                    "explication": "aoihzbeoab"},

                   {"Questions_ID": 2,
                    "response": "aedvarav",
                    "possibility": ["aozheva", "auziyevgao", "hahfhahav", "aedvarav"],
                    "explication": "hobaozcva"}]


def abort_if_question_doesnt_exist(Question):
    if Question not in Questions_dict:
        abort(404, message="Question is not found")


def abort_if_question_exist(Question):
    if Question in Questions_dict:
        abort(409, message="Question already exist")


def get_index_of_response(Questions_dict, Question):
    return Questions_dict[Question]["possibility"].index(Questions_dict[Question]["response"])


def having_the_json(Questions_dict):
    for i in range(len(Questions_dict)):
        ind = get_index_of_response(Questions_dict, i)
        Questions_dict[i]["index_response"] = ind

    return Questions_dict


class Questions(Resource):

    def get(self, Question):
        abort_if_question_doesnt_exist(Question)
        return {"Questions_ID": Questions_dict[Question]["Questions_ID"],
                "possibility": Questions_dict[Question]["possibility"],
                "explication": Questions_dict[Question]["explication"],
                "index_response": Questions_dict[Question]["possibility"].index(Questions_dict[Question]["response"])}

    def put(self, Question):
        abort_if_question_exist(Question)
        args = questions_put_args.parse_args()
        Questions_dict[Question] = args
        return Questions_dict


class All_questions(Resource):

    def get(self):
        res = having_the_json(Questions_dict1)
        return res


api.add_resource(Questions, "/Questions/<string:Question>")
api.add_resource(All_questions, "/Questions")

if __name__ == "__main__":
    app.run(debug=True)
