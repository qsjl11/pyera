from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.debug = True
app.config['SECRET_KEY'] = ''

socketio = SocketIO(app)

@app.route('/')
def get_index_page():
    return render_template('index.html')

@socketio.on('connect',namespace='/test')
def test_connect():
    print('connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('my event',namespace='/test')
def handle_my_custom_event(data):
    print('received json: ' + str(data))
    return 1

@socketio.on('disconnect',namespace='/test')
def disconnect_func():
    print('test websocket disconnected')


if __name__ == "__main__":
    socketio.run(app)