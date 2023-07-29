import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('message', 'Hello from client!')

@sio.event
def disconnect():
    print("I'm disconnected!")

sio.connect('http://localhost:8001')

# Stay connected for 10 seconds
time.sleep(10)

sio.disconnect()
