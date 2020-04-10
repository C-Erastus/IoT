import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import datetime 
import RPi.GPIO as GPIO
import time

# set up a client for InfluxDB
dbclient = InfluxDBClient('0.0.0.0', 8086, 'root', 'root', 'mydb')

GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)

#****************************************************
broker_address = "10.0.0.130" # the broker address

def on_message(client, userdata, message): 
    
    print(message.topic + " " + str(message.payload)) # print incoming messages 

    #get current time
    receiveTime = datetime.datetime.utcnow()

    #get sensor data from arudion using mqtt

    #create json to insert into db
    json_body = [
            {
                "measurement": 'test',
                "time": receiveTime, 
                "fields": {
                        "value": int(message.payload)
                }
             }
    ]

    #pi will save light sensor values to influxdb
    try:
        dbclient.write_points(json_body)
        #print("Finish wrting to InfluxDB")
    except Exception:
        print("This is totally not working")

    #print("DONE - On_message"

#*********************************************************

client = mqtt.Client() # create new client instance 
client.connect(broker_address) # coneect to broker

client.on_message = on_message # set the on message function

client.subscribe("/test") # subscribe to topic

client.loop_start()

try:
    while True:

        #print("after loop starts ")
       # print("Trying things out")
        
        try:
            # pi will querry influxdb for average light sensor value from the last 10 secons
            query = 'select mean("value") from "test" where "time" > now() - 10s'

            result = dbclient.query(query)

           # print("Try catch passed")
        except:
            pass 
        try:
            result = dbclient.query(query)
            light_avg = list(result.get_points(measurement='test'))[0]['mean']
            #print("Got the light average")
            #print(f"Light average {light_avg}")

            # if value is below 200 turn led on
            if light_avg < 200:
                #turn on led
                print("we made it")
                GPIO.output(12, GPIO.HIGH)

            elif light_avg > 200:
                #print(f" NEW MEAN: {mean}")
                #turn on led
                GPIO.output(12, GPIO.LOW)

        except:
            #print("FAILED TO TURN ON LEDS")
            pass

except KeyboardInterrupt: 
    pass

client.loop_stop()

