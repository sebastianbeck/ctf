import paho.mqtt.client as mqtt
clientid = "0574425013127048"
# The callback for when the client receives a CONNACK response from the server.
#https://github.com/eclipse/paho.mqtt.python
#https://github.com/mqtt/mqtt.github.io/wiki/Example-Uses
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/broker/#")
    client.subscribe(f"HV19/#")
    client.subscribe(f"HV19/0574425013127048/flag-tbd/#")
    
    #flag-tbd
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id=clientid, transport="websockets", clean_session=True)
client.username_pw_set('workshop', password='2fXc7AWINBXyruvKLiX')
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish
#client.on_subscribe = on_subscribe
#client.on_log = on_log
client.connect("whale.hacking-lab.com", 9001, 60, '')
client.loop_forever()