# Import package
import paho.mqtt.client as mqtt
import getpass
import datetime

username = getpass.getuser()
# Define Variables
MQTT_HOST = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = input("Enter the Topic you wish to send message to: ")

# Define on_publish event function
def on_publish(client, userdata, mid):
 print("Message Published...")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

while True: 
    userInput = input("Enter a message: ")
    MQTT_MSG = "Message: {} Sent at: {} Sent from Host: {}".format(userInput, datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), username)
    # Publish message to MQTT Broker 
    mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
# mqttc.disconnect()