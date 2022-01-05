from random import randrange
import faust
import constants as const
import json, time
from datetime import datetime
from faust.types import settings
# import socketio
# import engineio
# import eventlet


#Create Faust Application
app = faust.App('producer', broker='kafka://'+const.SERVER, topic_partitions=10, internal=True) #, producer_max_request_size=3173440261
topic = app.topic(const.TOPIC_NAME, partitions=10, internal=True, value_serializer='json')


#Socket Application
# sio = socketio.Server(cors_allowed_origins='*')
# socketApp = socketio.WSGIApp(sio)



#Read Json file & stream it to kafka
def detectionResponse():
    f = open("response/response1.json")
    data = json.load(f)
    return data


#Streaming data when application starts
@app.task()
async def on_start():
    start_time = time.time()
    timeout = 300
    index = 0
    #while(time.time() < start_time + timeout):
    for i in range(5):
        value = detectionResponse()
        p = randrange(0, 10)
        value["partition"] = str(p)
        value["send_time"] = str(datetime.now())
        value["no"] = index
        print(index)
        try:
            await topic.send(value=value, partition=p)            
        except Exception as e:
            print(e)
        index += 1
        time.sleep(1)


# @app.agent(topic)
# async def receive(messages):
#     async for message in messages:
#         if message is not None:
#             try:
#                 print(message)
#                 last_message_from_topic = message
#                 # app.websockets.emitMessage(message)
#             except:
#                 pass
#         else:
#             print('No message received')


#Socket Events
# @sio.event
# def connect(sid, environ, auth):
#     print('connect ', sid)
#     for i in range(100):
#         sio.emit('livemap', {"message":"hello"+str(i)})
#         #time.sleep(3)


# @sio.on('livemap')
# def livemap(sid):
#     print('connect ', sid)
#     sio.emit('livemap', {"message":"hello"})

# @sio.on('disconnect')
# def disconnect(sid):
#     print('disconnect ', sid)



# if __name__ == '__main__':
    # eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), socketApp)

