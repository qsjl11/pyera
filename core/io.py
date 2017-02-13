# -*- coding: UTF-8 -*-

import core.cfg

sys_print=print

if core.cfg.platform == 'web':
    from core.webframe import *

if core.cfg.platform == 'win':
    from core.winframe import *


# 输出一行，next：在新的一行输出文字
def printl(string, style='standard'):
    global flowjson
    print(string, style)
    print('\n')


def printline():
    printl('\n--------------------------------------------------------------------------------------------------------')


def warn(string):
    if core.cfg.platform == 'win':
        printl('')
        printl(string, style='warning')
    if core.cfg.platform == 'web':
        sys_print\
            ('\n'+string+'\n')
