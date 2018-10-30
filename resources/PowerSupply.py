from flask import request
from flask_restful import Resource
from Model import db, PowerSupply, PowerSupplySchema

powerSupplies_schema = PowerSupplySchema(many=True)
powerSupply_schema = PowerSupplySchema()

class PowerSupplyResource(Resource):
    def get(self):
        powerSupplies = PowerSupply.query.all()
        powerSupplies = powerSupplies_schema.dump(powerSupplies).data
        return {'status': 'success', 'data': powerSupplies}, 200
