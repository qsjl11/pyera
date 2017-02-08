# -*- coding: UTF-8 -*-

import core.cfg

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
    printl('')
    printl(string, style='warning')
