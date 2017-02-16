# -*- coding: UTF-8 -*-

import core.cfg

sys_print = print

if core.cfg.platform == 'web':
    from core.webframe import *

if core.cfg.platform == 'win':
    from core.winframe import *

import threading

input_evnet = threading.Event()

order_swap = None


def _input_evnet_set(order):
    global order_swap
    order_swap = order
    input_evnet.set()


def getorder():
    return order_swap


bind_return(_input_evnet_set)


def _get_input_event():
    return input_evnet


# 输出一行，next：在新的一行输出文字
def printl(string, style='standard'):
    print(string, style)
    print('\n')


def printline():
    printl('\n--------------------------------------------------------------------------------------------------------')


def warn(string):
    sys_print('')
    sys_print(string)




