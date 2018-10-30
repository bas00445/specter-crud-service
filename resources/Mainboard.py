from flask import request
from flask_restful import Resource
from Model import db, Mainboard, MainboardSchema

mainboards_schema = MainboardSchema(many=True)
mainboard_schema = MainboardSchema()

class MainboardResource(Resource):
    def get(self):
        mainboards = Mainboard.query.all()
        mainboards = mainboards_schema.dump(mainboards).data
        return {'status': 'success', 'data': mainboards}, 200
