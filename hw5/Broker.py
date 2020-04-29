import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from influxdb import InfluxDBClient
import datetime

broker_address="10.0.0.130"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def on_message(client, userdata, message):
	print(message.topic + " " + str(message.payload)) 

	if message.topic = '/light':

	if message.topic = '/piled': 

client = mqtt.Client()
client.connect(broker_address)

client.on_message = on_message

client.subscribe("/light")
client.subscribe("/piled")

dbclient = InfluxDBClient('0.0.0.0' 8086, 'root', 'root', 'mydb')

client.loop_start()

try:
	while True:
		pass

except keyBoardInterrupt:
	pass

client.loop_start()
GPIO.cleanup()
