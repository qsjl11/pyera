# -*- coding: UTF-8 -*-

import json

binding_return_func = None
flowjson = {}
linenumber = 0
openflow = None


# #######################################################################
# json 构建函数

def init_flowjson():
    global flowjson
    flowjson = {}
    flowjson.clear()
    linenumber = 0
    flowjson['content'] = [[]]

def text_json(string):
    re = {}
    re['type'] = 'text'
    re['text'] = string
    return re


# #######################################################################
# 输出格式化

def run(flow):
    global flowjson
    init_flowjson()
    flow.run()
    return json.dumps(flowjson, ensure_ascii=False)


def get_json_flow():
    global flowjson
    init_flowjson()
    binding_return_func()
    flowstr = json.dumps(flowjson, ensure_ascii=False)
    return flowstr


def bind_return(func):
    global binding_return_func
    binding_return_func = func


# #######################################################################
# 输出格式化


def print(string, style='standard'):
    global flowjson
    flowjson['content'][-1].append(text_json(string))


# 输出一行，next：在新的一行输出文字
def printl(string, style='standard'):
    global flowjson
    print(string, style)
    flowjson['content'].append([])



def printline():
    printl('\n--------------------------------------------------------------------------------------------------------')


def clear():
    pass
    # textbox.delete('1.0', END)


def style_def(style_name, **style_para):
    pass
    # textbox.tag_configure(style_name, **style_para)


def warn(string):
    printl('')
    printl(string, style='warning')


# #########################################################3
# 输入处理函数

def getorder():
    return 0


def clearorder():
    pass
    # order.set('')
