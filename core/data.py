# -*- coding: UTF-8 -*-
import json
import os

_gamedata = {}


def gamedata():
    return _gamedata


def _loadjson(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            jsondata = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print(filepath + '  无法读取，文件可能不符合json格式')
            jsondata = []
    return jsondata


def _loaddir(datapath):
    for dirpath, dirnames, filenames in os.walk(datapath):
        for name in filenames:
            thefilepath = dirpath + '\\' + name
            prefix = dirpath.replace(datapath, '').replace('\\', '.') + '.'
            if prefix == '.':
                prefix = ''
            _gamedata[prefix + name.split('.')[0]] = _loadjson(thefilepath)


def init():
    gamepath = os.path.split(os.path.realpath(__file__))[0][:-5]
    datapath = gamepath + '\\data'
    _loaddir(datapath)



def _get_savefilename_path(filename):
    gamepath = os.path.split(os.path.realpath(__file__))[0][:-5]
    savepath = gamepath + '\\save'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    filepath = savepath + '\\' + filename + '.json'
    return filepath


def save(filename):
    filepath=_get_savefilename_path(filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(_gamedata, f, ensure_ascii=False)


def load(filename):
    filepath = _get_savefilename_path(filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
                _gamedata.update(json.load(f))
    except FileNotFoundError:
        print(filepath+'  没有该存档文件')

