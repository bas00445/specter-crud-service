from flask import request
from flask_restful import Resource
from Model import db, Harddisk, HarddiskSchema

harddisks_schema = HarddiskSchema(many=True)
harddisk_schema = HarddiskSchema()

class HarddiskResource(Resource):
    def get(self):
        harddisks = Harddisk.query.all()
        harddisks = harddisks_schema.dump(harddisks).data
        return {'status': 'success', 'data': harddisks}, 200
