from flask import request
from flask import jsonify
from flask_restful import Resource
#from databases import crud_database_connection
import psycopg2
import simplejson as json
from decimal import Decimal
from Model import db, PowerSupply, PowerSupplySchema

powerSupplies_schema = PowerSupplySchema(many=True)
powerSupply_schema = PowerSupplySchema()

class PowerSupplyResource(Resource):
    def __init__(self):
        pass
        #self.conn = crud_database_connection
        #self.cursor = self.conn.cursor()
    
    def get(self):
        powerSupplies = PowerSupply.query.all()
        powerSupplies = powerSupplies_schema.dump(powerSupplies).data
        return {'status': 'success', 'data': powerSupplies}, 200
    
        
    '''
    def get(self):
        command = """ select * from public."PowerSupply" """
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return {'status': 'success', 'data': json.dumps(data)}, 200
    '''