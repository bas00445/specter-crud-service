from flask import request
from flask_restful import Resource
from Model import db, Monitor, MonitorSchema

monitors_schema = MonitorSchema(many=True)
monitor_schema = MonitorSchema()

class MonitorResource(Resource):
    def get(self):
        monitors = Monitor.query.all()
        monitors = monitors_schema.dump(monitors).data
        return {'status': 'success', 'data': monitors}, 200
