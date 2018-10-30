from flask import request
from flask_restful import Resource
from Model import db, Cpu, CpuSchema

cpus_schema = CpuSchema(many=True)
cpu_schema = CpuSchema()

class CpuResource(Resource):
    def get(self):
        cpus = Cpu.query.all()
        cpus = cpus_schema.dump(cpus).data
        return {'status': 'success', 'data': cpus}, 200
