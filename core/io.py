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
    print(str(string), style)
    print('\n')


def printline():
    printl('\n--------------------------------------------------------------------------------------------------------')


def warn(string):
    sys_print('')
    sys_print(string)


# style设置
_foreground = '#C8C8C8'
_background = '#2C4A69'
_font = '微软雅黑'
_fontsize = '14'


def style_def(style_name, foreground=_foreground, background=_background, font=_font, fontsize=_fontsize, bold=False,
              underline=False, slant=False):
    # include foreground, background, font, size, bold, underline, slant
    frame_style_def(style_name, foreground, background, font, fontsize, bold, underline, slant)


def init_style(foreground_c, background_c, button_c, font, font_size):
    global style_def
    def new_style_def(style_name, foreground=foreground_c, background=background_c, font=font, fontsize=font_size,
                      bold=False, underline=False, slant=False):
        frame_style_def(style_name, foreground, background, font, fontsize, bold, underline, slant)
    style_def=new_style_def
    style_def('standard')
