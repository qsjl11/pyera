# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'web'

import core.io as io
import core.flow
import core.data

import script.mainflow

#############################################################
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''
socketio = SocketIO(app)


@app.route('/')
def interactive():
    return render_template('index.html')


gamebegin_flag = 0


@socketio.on('run', namespace='/test')
def test_connect(*args):
    global gamebegin_flag
    try:
        if gamebegin_flag == 0:
            gamebegin_flag = 1
            jsonstr = io.run(core.flow.get_flow('open_flow'))
            emit('game_display', jsonstr)
    except Exception as e:
        return str(e)


@socketio.on('dealorder', namespace='/test')
def test_message(value):
    try:
        io.setorder(value)
        jsonstr = io.get_json_flow()
        emit('game_display', jsonstr)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    socketio.run(app)
