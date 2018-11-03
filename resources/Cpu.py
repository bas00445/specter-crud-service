from flask import request
from flask import jsonify
from flask_restful import Resource
#from databases import crud_database_connection
import psycopg2
import simplejson as json
from decimal import Decimal
from Model import db, Cpu, CpuSchema

cpus_schema = CpuSchema(many=True)
cpu_schema = CpuSchema()

class CpuResource(Resource):
    def get(self):
        cpus = Cpu.query.all()
        cpus = cpus_schema.dump(cpus).data
        return {'status': 'success', 'data': cpus}, 200

    '''
    def __init__(self):
        self.conn = crud_database_connection
        self.cursor = self.conn.cursor()

    def get(self):
        name = 'AMD TR4 RYZEN THREDRIPPER 1920X'
        self.cursor.execute(""" select * from public."CPU" """)
        data = self.cursor.fetchall()
        return {'status': 'success', 'data': json.dumps(data)}, 200

    
    def post(self,test):
        args = parser.parse_args()
     
        to= {'task': args['task']}
        print(to)   
        return to, 201
    
    #def add(self, title, brand, model, socket, core, thread, frequency, turbo, architecture, power_peak, price, cartURL, imgURL):
    '''