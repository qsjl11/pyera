# -*- coding: UTF-8 -*-
import core.io as io
import threading
import time

# 管理flow
flow_map = {}


def create_flow(flow_name):
    def real_deco(func):
        if flow_name == None:
            theflow_name = func.__name__
        else:
            theflow_name = flow_name
        flow_map[theflow_name] = func
        return func

    return real_deco


def get_flow(flow_name):
    if flow_name in flow_map.keys():
        return flow_map[flow_name]
    else:
        io.warn(flow_name + ' :没有该流程，或该流程没有被加载')


# 管理命令
cmd_map = {}


def bind_cmd(cmd_number, cmd_func, arg=()):
    if not isinstance(arg, tuple):
        arg = (arg,)

    def run_func():
        cmd_func(*arg)

    cmd_map[cmd_number] = run_func


def print_cmd(cmd_str, cmd_number, cmd_func, arg=(), normal_style='standard', on_style='onbutton'):
    '''arg is tuple contain args which cmd_func could be used'''
    bind_cmd(cmd_number, cmd_func, arg)
    io.io_print_cmd(cmd_str, cmd_number, normal_style, on_style)
    return cmd_str


def cmd_clear(*number):
    if number:
        for num in number:
            cmd_map.pop(num)
            io.io_clear_cmd(num)
    else:
        cmd_map.clear()
        io.io_clear_cmd()


def _cmd_deal(order_number):
    cmd_map[int(order_number)]()


def _cmd_valid(order_number):
    return order_number in cmd_map.keys()


# 处理输入
def order_deal(flag='order', print_order=True):
    while True:
        io._get_input_event().clear()
        io._get_input_event().wait()
        order = io.getorder()
        if print_order == True:
            io.print(order+'\n')
        if flag == 'order':
            if order.isdigit() and _cmd_valid(int(order)):
                _cmd_deal(int(order))
                return

        if flag == 'str':
            return io.getorder()


def askfor_str(donot_return_null_str=True, print_order=False):
    while True:
        order = order_deal('str', print_order)
        if donot_return_null_str == True and order != '':
            return order
        elif donot_return_null_str == False:
            return order


def askfor_int(print_order=False):
    while True:
        order = order_deal('str', print_order)
        if order.isdigit():
            return int(order)
        else:
            io.print("不是有效数字")
