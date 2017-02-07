# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def interactive():
    return render_template('index.html')


@app.route('/background_process')
def background_process():
    try:
        value = request.args.get('proglang', 0, type=str)
        jsonstr = '{"content":[[{"type":"text", "text":"[001]开始游戏"},{"type":"cmd", "order":1, "text":""}],[{"type":"text", "text":"[002]加载游戏"},{"type":"text", "text":""}]]}'
        return jsonify(jsonstr)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()
