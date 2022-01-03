import socketio
import eventlet

sio = socketio.Server()
socketapp = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(sid, 'connected')
    for i in range(100):
        print(i)
        sio.emit('livemap', {'msg': 'hello' + str(i)})


@sio.on('disconnect')
def disconnect(sid):
    print(sid, 'disconnected')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3000)), socketapp)
