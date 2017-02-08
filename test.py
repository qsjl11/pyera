# -*- coding: UTF-8 -*-


import core.webio as io
import core.flow
import core.data

open_flow = core.flow.Flow('open_flow')


def open_func():
    io.printline()
    io.printl('pyera 启动中，准备开始游戏')
    io.printl(open_flow.cmd(1, '[001] 开始游戏', 'newgame_flow'))
    io.printl(open_flow.cmd(2, '[002] 加载游戏', None))


open_flow.func = open_func

#############################################################
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def interactive():
    return render_template('index.html')


@app.route('/background_process')
def background_process():
    try:
        value = request.args.get('proglang', 0, type=str)
        jsonstr = io.run(open_flow)
        return jsonify(jsonstr)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()

