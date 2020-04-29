import RPi.GPIO as GPIO 
import time 
import paho.mqtt.client as mqtt

broker_address = "10.0.0.130"

GPIO.setmode(GPIO.BCM)  

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(12, GPIO.OUT)

def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload)) # print incoming messages

    if message.payload == "on":
        print("Please turn on led")
        GPIO.output(12, GPIO.HIGH)

    elif message.payload == "off":
        #print("please turn off led")
        GPIO.output(12, GPIO.LOW)    


#********** SEND MESSAGE ********************* 
""" Send message from Pi to arduino..
This message will tell the arduino to turn on LED """

client = mqtt.Client() #create new mqtt client instance 

client.connect(broker_address) #connect to broker 

client.on_message = on_message # set the on message function 

client.subscribe("/test")

client.loop_start()

try:
    while True:
        
        buttonState = GPIO.input(23)
        #print(buttonState)

        if buttonState == 0:
            print("Erastus this works")
            client.publish("/led", "on")

        elif buttonState == 1: 
            client.publish("/led","off")
    
except KeyboardInterrupt: 
    pass
client.loop_stop()

