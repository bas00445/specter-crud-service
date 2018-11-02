from flask import Blueprint
from flask_restful import Api
from resources.Cpu import CpuResource
from resources.Gpu import GpuResource
from resources.Harddisk import HarddiskResource
from resources.Monitor import MonitorResource
from resources.PowerSupply import PowerSupplyResource
from resources.Ram import RamResource
from resources.Ssd import SsdResource
from resources.Mainboard import MainboardResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(CpuResource, '/cpu')
api.add_resource(GpuResource, '/gpu')
api.add_resource(HarddiskResource, '/harddisk')
api.add_resource(MonitorResource, '/monitor')
api.add_resource(PowerSupplyResource, '/powersupply')
api.add_resource(RamResource, '/ram')
api.add_resource(SsdResource, '/ssd')
api.add_resource(MainboardResource, '/mainboard')


