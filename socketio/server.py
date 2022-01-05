import socketio
import engineio
import eventlet
import time

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)
    for i in range(100):
        sio.emit('livemap', {"message":"hello"+str(i)})
        #time.sleep(3)


@sio.on('livemap')
def livemap(sid):
    print('connect ', sid)
    sio.emit('livemap', {"message":"hello"})

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__=='__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), app)



