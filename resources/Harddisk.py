from flask import request
from flask import jsonify
from flask_restful import Resource
from databases import crud_database_connection
import psycopg2
import simplejson as json
from decimal import Decimal
from Model import db, Harddisk, HarddiskSchema

'''
harddisks_schema = HarddiskSchema(many=True)
harddisk_schema = HarddiskSchema()
'''

class HarddiskResource(Resource):
    def __init__(self):
        self.conn = crud_database_connection
        self.cursor = self.conn.cursor()

    def get(self):
        '''
        harddisks = Harddisk.query.all()
        harddisks = harddisks_schema.dump(harddisks).data
        return {'status': 'success', 'data': harddisks}, 200
        '''
        command = """ SELECT * FROM public."Harddisk" """
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return {'status': 'success', 'data': json.dumps(data)}, 200

    def post(self, data):
        command = """ UPDATE public."Harddisk"
                      SET "Brand" = "%s", "Capacity" = "%s", "Device_Size" = "%s", 
                          "RW_Speed" = "%s", "Technology" = "%s", Price = "%s", 
                          "CartURL" = "%s", "ImgURL" = "%s" 
                      WHERE "Title" = "%s""""
        self.cursor.execute(command, (data['Brand'], data['Brand']))
        data = self.cursor.fetchall()