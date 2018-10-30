from flask import request
from flask_restful import Resource
from Model import db, Ssd, SsdSchema

ssds_schema = SsdSchema(many=True)
ssd_schema = SsdSchema()

class SsdResource(Resource):
    def get(self):
        ssds = Ssd.query.all()
        ssds = ssds_schema.dump(ssds).data
        return {'status': 'success', 'data': ssds}, 200
