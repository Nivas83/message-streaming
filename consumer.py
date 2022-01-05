import socketio
import engineio
import eventlet
import time
from kafka import KafkaConsumer
from json import loads
import constants as const

# mgr = socketio.KafkaManager('kafka://')
# sio = socketio.Server(client_manager=mgr, cors_allowed_origins='*')

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)
    groupdId = 'test' 
    topic=const.TOPIC_NAME

    # for i in range(100):
    #     msg = {'message': 'test message '+str(i)}
    #     print(msg)
    #     sio.emit('livemap', msg)


    # print('Listening Group', groupdId)
    # print('Topic: ', topic)
    # consumer = KafkaConsumer(
    #     bootstrap_servers=[const.SERVER],
    #     auto_offset_reset='earliest',
    #     enable_auto_commit=True,
    #     group_id=groupdId,
    #     value_deserializer=lambda x: loads(x.decode('utf-8')))
    # consumer.subscribe(topic)
    # for message in consumer:
    #     try:
    #         print(message)
    #         sio.emit('livemap', message)
    #     except Exception as e:
    #         print(e)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


def getLiveMapData(topic=const.TOPIC_NAME,groupdId='test'):
    print('Listening Group', groupdId)
    print('Topic: ', topic)
    consumer = KafkaConsumer(
        bootstrap_servers=[const.SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=groupdId,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    consumer.subscribe(topic)
    for message in consumer:
        try:
            # print(message)
            sio.emit('livemap', message)
        except Exception as e:
            print(e)

if __name__=='__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), app)







