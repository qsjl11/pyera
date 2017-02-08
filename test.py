# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'web'

import core.io as io
import core.flow
import core.data

import script.mainflow

#############################################################
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def interactive():
    return render_template('index.html')


@app.route('/nextflow')
def background_process():
    try:
        value = request.args.get('proglang', 0, type=str)
        io.setorder(value)
        jsonstr = io.get_json_flow()
        return jsonify(jsonstr)
    except Exception as e:
        return str(e)


@app.route('/run')
def background_process_run():
    try:
        jsonstr = io.run(core.flow.get_flow('open_flow'))
        return jsonify(jsonstr)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()
