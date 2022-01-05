from flask import Flask, send_from_directory, Response
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
import constants as const
from json import loads
from kafka import KafkaConsumer, TopicPartition


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'



@socketio.on('connect')
def kafkaconsumer():
    try:
        consumer = KafkaConsumer(const.TOPIC_NAME,
                            bootstrap_servers=const.SERVER, 
                            group_id="consumer",
                            auto_offset_reset='earliest')
        for msg in consumer:
            print(msg)
            # emit('livemap', {'message': 'test message'})
        consumer.close()

        # for i in range(100):
        #     msg = {'message': 'test message '+str(i)}
        #     print(msg)
        #     emit('livemap', msg)
    except Exception as e:
        print(e)

# @socketio.on('connect')
# def kafkaStream():
#     consumer = KafkaConsumer(const.TOPIC_NAME,
#                             bootstrap_servers=const.SERVER, 
#                             group_id="consumer",
#                             auto_offset_reset='earliest')
#     def events():
#         result = []
#         for message in consumer:
#            if message is not None:
#                result.append(message)
#            yield result
#     return Response(events())

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=3000)

