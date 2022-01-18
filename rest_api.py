from decimal import Decimal
from re import sub

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from marshmallow import Schema, fields, ValidationError

from src.vacation_payment import Person, calebs_algorithm

app = Flask(__name__)
CORS(app, resources={r"/payments": {"origins": "*"}})
api = Api(app)


class PersonSchema(Schema):
    name = fields.Str(required=True)
    amount = fields.Str(required=True)


schema = PersonSchema(many=True)


class Payments(Resource):
    @staticmethod
    def post():
        app.logger.info("{}".format(request.get_json()))

        try:
            data = schema.loads(request.get_data())
        except ValidationError as err:
            return err.messages, 400

        input_people = [Person(p['name'], Decimal(sub(r'[^\d.]', '', p['amount']))) for p in data]
        output_people = calebs_algorithm(input_people)
        return [{'name': p.name, 'amount': '$' + str(p.amount)} for p in output_people], 200


api.add_resource(Payments, '/payments')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
