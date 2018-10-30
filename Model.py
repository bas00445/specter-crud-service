from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Cpu(db.Model):
    __tablename__ = 'CPU'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Model = db.Column(db.String(150), unique=False, nullable=True)
    Socket = db.Column(db.String(150), unique=False, nullable=True)
    Core = db.Column(db.Integer)
    Thread = db.Column(db.Integer)
    Frequency = db.Column(db.Float)
    Turbo = db.Column(db.Float)
    Architecture = db.Column(db.Integer)
    Power_Peak = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

    # Don't need constructor


class Gpu(db.Model):
    __tablename__ = 'GPU'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Model = db.Column(db.String(150), unique=False, nullable=True)
    Chipset = db.Column(db.String(150), unique=False, nullable=True)
    Architecture = db.Column(db.Integer)
    GPU_Speed = db.Column(db.Integer)
    RAM_Speed = db.Column(db.Integer)
    RAM_Capacity = db.Column(db.Integer)
    RAM_Type = db.Column(db.String(150), unique=False, nullable=True)
    Bus_Width = db.Column(db.Integer)
    DirectX = db.Column(db.Integer)
    DVI_Port = db.Column(db.Integer)
    HDMI_Port = db.Column(db.Integer)
    Display_Port = db.Column(db.Integer)
    Power_Supply = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class Harddisk(db.Model):
    __tablename__ = 'Harddisk'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Capacity = db.Column(db.Integer)
    Device_Size = db.Column(db.Float)
    RW_Speed = db.Column(db.Integer)
    Technology = db.Column(db.String(150), unique=False, nullable=True)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class Monitor(db.Model):
    __tablename__ = 'Monitor'
    ProductID = db.Column(db.String(150), primary_key=True)
    Title = db.Column(db.String(150))
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Size = db.Column(db.Integer)
    Panel_Type = db.Column(db.String(150), unique=False, nullable=True)
    Resolution = db.Column(db.String(150), unique=False, nullable=True)
    Refresh_Rate = db.Column(db.Integer)
    Response_Time = db.Column(db.Integer)
    Brightness = db.Column(db.Integer)
    HDMI_Port = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class PowerSupply(db.Model):
    __tablename__ = 'PowerSupply'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Max_Power = db.Column(db.Integer)
    Standard = db.Column(db.String(150), unique=False, nullable=True)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class Ram(db.Model):
    __tablename__ = 'RAM'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    RAM_Type = db.Column(db.String(150), unique=False, nullable=True)
    Capacity = db.Column(db.Integer)
    RAM_Bus = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class Ssd(db.Model):
    __tablename__ = 'SSD'
    Title = db.Column(db.String(150), primary_key=True)
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Capacity = db.Column(db.Integer)
    Device_Size = db.Column(db.String(150), unique=False, nullable=True)
    Read = db.Column(db.Integer)
    Write = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)

class Mainboard(db.Model):
    __tablename__ = 'Mainboard'
    ProductID = db.Column(db.String(150), primary_key=True)
    Title = db.Column(db.String(150))
    Brand = db.Column(db.String(150), unique=False, nullable=True)
    Socket = db.Column(db.String(150), unique=False, nullable=True)
    Chipset = db.Column(db.String(150), unique=False, nullable=True)
    CPU_Series = db.Column(db.String(150))
    RAM_Slot = db.Column(db.Integer)
    RAM_Type = db.Column(db.String(150))
    RAM_Max = db.Column(db.Integer)
    RAM_Bus = db.Column(db.String(150))
    Port_USB_2 = db.Column(db.Integer)
    Port_USB_3 = db.Column(db.Integer)
    Port_USB_3_1_A = db.Column(db.Integer)
    HDMI_Output = db.Column(db.Integer)
    Port_PS2 = db.Column(db.Integer)
    Type = db.Column(db.String(150))
    Price = db.Column(db.Integer)
    CartURL = db.Column(db.String(150), unique=False, nullable=True)
    ImgURL = db.Column(db.String(150), unique=False, nullable=True)
  

#### For validation #####
class CpuSchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    Model = fields.String()
    Socket = fields.String()
    Core = fields.Integer()
    Thread = fields.Integer()
    Frequency = db.Column(db.Float)
    Turbo = db.Column(db.Float)
    Architecture = fields.Integer()
    Power_Peak = fields.Integer()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class GpuSchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    Model = fields.String()
    Chipset = fields.String()
    Architecture = fields.Integer()
    GPU_Speed = fields.Integer()
    RAM_Speed = fields.Integer()
    RAM_Capacity = fields.Integer()
    RAM_Type = fields.String()
    Bus_Width = fields.Integer()
    DirectX = fields.Integer()
    DVI_Port = fields.Integer()
    HDMI_Port = fields.Integer()
    Display_Port = fields.Integer()
    Power_Supply = fields.Integer()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class HarddiskSchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    Capacity = fields.Integer()
    Device_Size = db.Column(db.Float)
    RW_Speed = fields.Integer()
    Technology = fields.String()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class MonitorSchema(ma.Schema):
    ProductID = fields.String(primary_key=True)
    Title = fields.String()
    Brand = fields.String()
    Size = fields.Integer()
    Panel_Type = fields.String()
    Resolution = fields.String()
    Refresh_Rate = fields.Integer()
    Response_Time = fields.Integer()
    Brightness = fields.Integer()
    HDMI_Port = fields.Integer()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class PowerSupplySchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    Max_Power = fields.Integer()
    Standard = fields.String()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class RamSchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    RAM_Type = fields.String()
    Capacity = fields.Integer()
    RAM_Bus = fields.Integer()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class SsdSchema(ma.Schema):
    Title = fields.String(primary_key=True)
    Brand = fields.String()
    Capacity = fields.Integer()
    Device_Size = fields.String()
    Read = fields.Integer()
    Write = fields.Integer()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()

class MainboardSchema(ma.Schema):
    ProductID = fields.String(primary_key=True)
    Title = fields.String()
    Brand = fields.String()
    Socket = fields.String()
    Chipset = fields.String()
    CPU_Series = fields.String()
    RAM_Slot = fields.Integer()
    RAM_Type = fields.String()
    RAM_MAX = fields.Integer()
    RAM_Bus = fields.String()
    Port_USB_2 = fields.Integer()
    Port_USB_3 = fields.Integer()
    Port_USB_3_1_A = fields.Integer()
    HDMI_Output = fields.Integer()
    Port_PS2 = fields.Integer()
    Type = fields.String()
    Price = fields.Integer()
    CartURL = fields.String()
    ImgURL = fields.String()
