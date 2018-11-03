from flask import request
from flask import jsonify
from flask_restful import Resource
import psycopg2
import simplejson as json
from decimal import Decimal
from Model import db, Harddisk, HarddiskSchema


harddisks_schema = HarddiskSchema(many=True)
harddisk_schema = HarddiskSchema()


class HarddiskResource(Resource):
    def get(self):
        harddisks = Harddisk.query.all()
        harddisks = harddisks_schema.dump(harddisks).data
        return {'status': 'success', 'data': harddisks}, 200

    def put(self):
        harddisks = Harddisk.query.filter_by(Title = "title1").all()
        harddisks = harddisks_schema.dump(harddisks).data
        return {'status': 'success', 'data': harddisks}, 200

    def delete(self):
        harddisks = Harddisk.query.filter_by(Title = "title1").all()
        print(type(Harddisk))
        Harddisk.delete(harddisks)
        Harddisk.commit()
        return {'status': 'success', 'data': harddisks}, 200
    '''
    def __init__(self):
        #self.conn = crud_database_connection
        #self.cursor = self.conn.cursor()
        pass 

    def get(self):
        
        harddisks = Harddisk.query.all()
        harddisks = harddisks_schema.dump(harddisks).data
        return {'status': 'success', 'data': harddisks}, 200

    def put(self):
        command = """INSERT INTO public."Harddisk" ("Title", "Brand", "Capacity", "Device_Size", "RW_Speed", "Technology",
                                                         "Price", "CartURL", "ImgURL")
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s); """

        #self.cursor.execute(command, (data['Brand'], data['Brand']))
        self.cursor.execute(command, ("title1", "brand1", 1, 1.0, 1, "tech1", 1.00, "cURL1", "iURL1"))
        self.cursor.fetchall()
        self.conn.commit()
        return 'put'

    def post(self, data):
        command = """ UPDATE public."Harddisk"
                      SET "Brand" = "%s", "Capacity" = "%s", "Device_Size" = "%s", 
                          "RW_Speed" = "%s", "Technology" = "%s", "Price" = "%s", 
                          "CartURL" = "%s", "ImgURL" = "%s" 
                      WHERE "Title" = "%s"; """
        pass

    def delete(self):
        command = """ DELETE FROM public."Harddisk" 
                      WHERE "%s" = %s; """

        self.cursor.execute(command, ('Title', data))
        self.cursor.fetchall()
        self.conn.commit()
        return 'delete'
    '''

'''
        command = """ SELECT * FROM public."Harddisk" """
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return {'status': 'success', 'data': json.dumps(data)}, 200
'''