import time
import random
from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]

topic = "naturalnumbers"

producer = KafkaProducer(bootstrap_servers=bootstrap_server)

producer = KafkaProducer()

def sendata():
    naturalnumber = random.randint(0,1000)
    message = producer.send(topic,bytes(str(naturalnumber),"utf-8"))
    metadata = message.get()    
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)
while True:
    sendata()