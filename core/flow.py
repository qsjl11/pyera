# -*- coding: UTF-8 -*-
import core.io as io
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
        io.print(flow_name + ' :没有该流程，或该流程没有被加载')


# 管理命令
cmd_map = {}


def default_tail_deal_cmd_func(order):
    return


tail_deal_cmd_func = default_tail_deal_cmd_func


def set_tail_deal_cmd_func(func):
    global tail_deal_cmd_func
    tail_deal_cmd_func = func

def deco_set_tail_deal_cmd_func(func):
    set_tail_deal_cmd_func(func)
    return func

def bind_cmd(cmd_number, cmd_func, arg=(), kw={}):
    if not isinstance(arg, tuple):
        arg = (arg,)
    if cmd_func==null_func:
        cmd_map[cmd_number] = null_func
        return

    def run_func():
        cmd_func(*arg, **kw)
    cmd_map[cmd_number] = run_func


def null_func():
    return


def print_cmd(cmd_str, cmd_number, cmd_func=null_func, arg=(), kw={}, normal_style='standard', on_style='onbutton'):
    '''arg is tuple contain args which cmd_func could be used'''
    bind_cmd(cmd_number, cmd_func, arg, kw)
    io.io_print_cmd(cmd_str, cmd_number, normal_style, on_style)
    return cmd_str


def cmd_clear(*number):
    set_tail_deal_cmd_func(default_tail_deal_cmd_func)
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
    re=(order_number in cmd_map.keys()) and (cmd_map[int(order_number)] != null_func)
    return re


__skip_flag__ = False
reset_func = None


# 处理输入
def order_deal(flag='order', print_order=True):
    global __skip_flag__
    __skip_flag__ = False
    while True:
        time.sleep(0.01)
        order = io.getorder()
        if order == '_reset_this_game_':
            reset_func()
        if print_order == True and order != '' and order != 'skip_all_wait':
            io.print('\n' + order + '\n')

        if flag == 'str':
            return order

        if flag == 'console':
            # TODO add_console_method
            exec(order)

        if flag == 'order' and order.isdigit():
            if _cmd_valid(int(order)):
                _cmd_deal(int(order))
                return
            else:
                global tail_deal_cmd_func
                tail_deal_cmd_func(int(order))
                return


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
            if order == '':
                continue
            io.print('\n' + "不是有效数字" + '\n')


def askfor_wait():
    global __skip_flag__
    if __skip_flag__ == False:
        re = askfor_str(donot_return_null_str=False)
        if re == 'skip_all_wait':
            __skip_flag__ = True
