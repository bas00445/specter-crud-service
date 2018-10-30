from flask import request
from flask_restful import Resource
from Model import db, Gpu, GpuSchema

gpus_schema = GpuSchema(many=True)
gpu_schema = GpuSchema()

class GpuResource(Resource):
    def get(self):
        gpus = Gpu.query.all()
        gpus = gpus_schema.dump(gpus).data
        return {'status': 'success', 'data': gpus}, 200
