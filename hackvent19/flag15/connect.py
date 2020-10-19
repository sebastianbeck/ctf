import paho.mqtt.client as mqtt

clientid = "0574425013127048"

def on_connect(mqttc, obj, flags, rc):
    #client.subscribe(f"HV19/gifts/{client_id}")
    client.subscribe(f"HV19/gifts/{clientid}")
    client.subscribe(f"HV19/{clientid}/flag-tbd/#")
    client.subscribe(f"$SYS/#")
    client.subscribe(f"#")
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

client = mqtt.Client(client_id=clientid, transport="websockets", clean_session=True)
client.username_pw_set('workshop', password='2fXc7AWINBXyruvKLiX')
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_log = on_log
client.connect("whale.hacking-lab.com", 9001, 60, '')
client.loop_forever()