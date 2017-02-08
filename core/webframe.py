# -*- coding: UTF-8 -*-

import json

binding_return_func = None
flowjson = {}
order = 0


# #######################################################################
# json 构建函数

def init_flowjson():
    global flowjson
    flowjson = {}
    flowjson.clear()
    flowjson['content'] = []


def text_json(string):
    re = {}
    re['type'] = 'text'
    re['text'] = string.replace('\n', '<br/>')
    return re


# #######################################################################
# 运行逻辑

def run(flow):
    global flowjson
    init_flowjson()
    flow.run()
    return json.dumps(flowjson, ensure_ascii=False)


def get_json_flow():
    global flowjson
    global binding_return_func
    init_flowjson()
    binding_return_func()
    flowstr = json.dumps(flowjson, ensure_ascii=False)
    return flowstr


# ######################################################################
# ######################################################################
# ######################################################################
# 双框架公共函数

def bind_return(func):
    global binding_return_func
    binding_return_func = func
    return


# #######################################################################
# 输出格式化


def print(string, style='standard'):
    global flowjson
    flowjson['content'].append(text_json(string))


def clear():
    pass
    # textbox.delete('1.0', END)


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
    pass
    # order.set('')
