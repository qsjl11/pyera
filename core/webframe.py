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
sysprint = print


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


def text_json(string, style):
    re = {}
    re['type'] = 'text'
    re['text'] = string.replace('\n', '<br/>')
    re['style'] = style
    return re


def cmd_json(cmd_str, cmd_num, normal_style, on_style):
    re = {}
    re['type'] = 'cmd'
    re['text'] = cmd_str.replace('\n', '<br/>')
    re['num'] = cmd_num
    re['normal_style'] = normal_style
    re['on_style'] = on_style
    return re


def style_json(style_name, foreground, background, font, fontsize, bold, underline, italic):
    re = {}
    re['style_name'] = style_name
    re['foreground'] = foreground
    re['background'] = background
    re['font'] = font
    re['fontsize'] = fontsize
    re['bold'] = bold
    re['underline'] = underline
    re['italic'] = italic
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


def set_background(color):
    jsonstr = new_json()
    jsonstr['bgcolor'] = color
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


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
    jsonstr['content'].append(text_json(string, style))
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


def clear_screen():
    # io_clear_cmd()
    jsonstr = new_json()
    jsonstr['clear_cmd'] = 'true'
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


def frame_style_def(style_name, foreground, background, font, fontsize, bold, underline, italic):
    jsonstr = new_json()
    jsonstr['set_style'] = style_json(style_name, foreground, background, font, fontsize, bold, underline, italic)
    socketio.emit('game_display', json.dumps(jsonstr, ensure_ascii=False), namespace='/test')


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
def io_print_cmd(cmd_str, cmd_number, normal_style='standard', on_style='onbutton'):
    jsonstr = new_json()
    jsonstr['content'].append(cmd_json(cmd_str, cmd_number, normal_style, on_style))
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


@socketio.on('connect', namespace='/test')
def test_connect():
    sysprint('connected')
