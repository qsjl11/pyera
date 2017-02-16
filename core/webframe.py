# -*- coding: UTF-8 -*-


import json

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, disconnect

binding_return_func = None
flowjson = {}
flowjson['content'] = []
order = 0
input_event_func = None

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''
socketio = SocketIO(app, async_mode='threading')
flowthread = None

open_func = None


# #######################################################################
# json 构建函数

def init_flowjson():
    global flowjson
    flowjson.clear()
    flowjson['content'] = []


def new_json():
    flowjson = {}
    flowjson['content'] = []
    return flowjson


def text_json(string):
    re = {}
    re['type'] = 'text'
    re['text'] = string.replace('\n', '<br/>')
    return re


def cmd_json(cmd_str, cmd_num):
    re = {}
    re['type'] = 'cmd'
    re['text'] = cmd_str.replace('\n', '<br/>')
    re['num'] = cmd_num
    return re


# #######################################################################
# 运行逻辑

def run(open_flow):
    global open_func
    open_func = open_flow
    socketio.run(app)


def send_input(*args):
    global input_event_func
    order = getorder()
    input_event_func(order)
    clearorder()


# ######################################################################
# ######################################################################
# ######################################################################
# 双框架公共函数

def bind_return(func):
    global input_event_func
    input_event_func = func
    return


# #######################################################################
# 输出格式化

# @copy_current_request_context
def print(string, style='standard'):
    jsonstr = new_json()
    jsonstr['content'].append(text_json(string))
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


def clear_screen():
    # io_clear_cmd()
    jsonstr = new_json()
    jsonstr['clear_cmd'] = 'true'
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


def style_def(style_name, **style_para):
    pass
    # textbox.tag_configure(style_name, **style_para)


# #########################################################3
# 输入处理函数

def getorder():
    global order
    return order


def setorder(orderstr):
    global order
    order = orderstr


def clearorder():
    jsonstr = new_json()
    jsonstr['clearorder_cmd'] = 'true'
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


# ############################################################

# 命令生成函数
def io_print_cmd(cmd_str, cmd_number):
    jsonstr = new_json()
    jsonstr['content'].append(cmd_json(cmd_str, cmd_number))
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


# 清除命令函数
def io_clear_cmd(*cmd_numbers):
    jsonstr = new_json()
    if cmd_numbers:
        jsonstr['clearcmd_cmd'] = cmd_numbers
    else:
        jsonstr['clearcmd_cmd'] = 'all'
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


####################################################################
####################################################################


@app.route('/')
def interactive():
    return render_template('index.html')


@socketio.on('run', namespace='/test')
def test_connect(*args):
    global gamebegin_flag
    global flowthread
    global open_func

    try:
        if flowthread == None:
            flowthread = socketio.start_background_task(target=open_func)

    except Exception as e:
        return str(e)


@socketio.on('dealorder', namespace='/test')
def test_message(value):
    try:
        setorder(value)
        send_input()
    except Exception as e:
        return str(e)
