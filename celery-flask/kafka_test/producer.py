from kafka import KafkaProducer
import json

def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093', value_serializer=serializer)

# producer.send('usertopic', b'hi')
def send_message(message):
    producer.send('usertopic', {'message': message})
    producer.flush()
