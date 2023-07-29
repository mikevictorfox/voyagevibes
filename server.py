from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Hello, World!"

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('response', {'response': 'This is a response from Flask.'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001)
