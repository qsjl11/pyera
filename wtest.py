# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'web'

import core.io as io
import core.flow
import core.data

import script.mainflow

#############################################################
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''
socketio = SocketIO(app)


@app.route('/')
def interactive():
    return render_template('indextest.html')


@socketio.on('run', namespace='/test')
def test_connect(*args):
    try:
        print('aaa')
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
