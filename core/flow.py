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
cmd_clear_callback_func = None


def cmd(cmd_str, cmd_number, cmd_func, *args, **kw):
    def run_func():
        cmd_func(*args, **kw)

    cmd_map[cmd_number] = run_func
    return cmd_str


def cmd_gotoflowbyname(cmd_str, cmd_number, cmd_flowname, *args, **kw):
    if not isinstance(cmd_flowname, str):
        io.warn(cmd_flowname + ' :不是有效的flow名称，flowname应为字符串')
        return

    def gotoflow(*_args, **_kw):
        flow_func = get_flow(cmd_flowname)
        flow_func(*_args, **_kw)

    cmd(cmd_str, cmd_number, gotoflow, *args, *kw)


def cmd_clear():
    global cmd_clear_callback_func
    cmd_map.clear()
    cmd_clear_callback_func()


def _cmd_clear_callback(func):
    global cmd_clear_callback_func
    cmd_clear_callback_func = func


def _cmd_deal(order_number):
    cmd_map[int(order_number)]()


def _cmd_valid(order_number):
    return order_number in cmd_map.keys()


# 处理输入
def order_deal(flag='order'):
    while True:
        io._get_input_event().clear()
        io._get_input_event().wait()
        order = io.getorder()
        if flag == 'order':
            if order.isdigit() and _cmd_valid(int(order)):
                _cmd_deal(int(order))
                return

        if flag == 'str':
            return io.getorder()


def askfor_str(unnull_str_flag=True):
    while True:
        order = order_deal('str')
        if unnull_str_flag == True and order != '':
            return order
        elif unnull_str_flag == False:
            return order


def askfor_int():
    while True:
        order = order_deal('str')
        if order.isdigit():
            return int(order)
