from flask import request
from flask_restful import Resource
from Model import db, Ram, RamSchema

rams_schema = RamSchema(many=True)
ram_schema = RamSchema()

class RamResource(Resource):
    def get(self):
        rams = Ram.query.all()
        rams = rams_schema.dump(rams).data
        return {'status': 'success', 'data': rams}, 200
