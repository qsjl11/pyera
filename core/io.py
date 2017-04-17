# -*- coding: UTF-8 -*-

import core.cfg

sys_print = print

if core.cfg.platform == 'web':
    str = 'from core.webframe import *'
    exec(str)

if core.cfg.platform == 'win':
    from core.winframe import *

import threading

import sys
sys.setrecursionlimit(100000)

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


# style设置
_foreground = '#C8C8C8'
_background = '#2C4A69'
_font = '微软雅黑'
_fontsize = '14'


def style_def(style_name, foreground=_foreground, background=_background, font=_font, fontsize=_fontsize, bold=False,
              underline=False, italic=False):
    pass


def init_style(foreground_c, background_c, onbutton_c, font, font_size):
    global style_def

    def new_style_def(style_name, foreground=foreground_c, background=background_c, font=font, fontsize=font_size,
                      bold=False, underline=False, italic=False):
        frame_style_def(style_name, foreground, background, font, fontsize, bold, underline, italic)

    style_def = new_style_def
    style_def('standard')
    style_def('onbutton', foreground=onbutton_c)
