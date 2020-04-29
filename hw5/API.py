import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
from flask iimport Flask, request, json
from flask_restufl import Resource, Api
import datetime

broker_address="10.0.0.130" #broker address

client = mqtt.Client() # create new client 
client.connect(broker_address) #connect to broker

dbclient = InfluxDBClient('0.0.0.0', 8086, 'root', 'root', 'mydb')

app = Flask(__name__)
api = Api(app)

class Test(Resource):
	def get(self):

	def post(self):

api.add_resource(Test, '/test')

api.run(host='0.0.0.0', debug=True)
