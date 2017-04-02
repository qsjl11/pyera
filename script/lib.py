# -*- coding: UTF-8 -*-

import core.game as game


def yes_or_no():
    game.pcmd('[0] 是  ', 0, None)
    game.pcmd('[1] 否  ', 1, None)
    while True:
        ans = game.askfor_int()
        if ans == 0:
            return True
        if ans == 1:
            return False


def get_id():
    if not 'last_id' in game.data:
        game.data['last_id'] = 100
    game.data['last_id'] += 1
    return game.data['last_id']


def value_bar(vnow, vmax, length=30):
    if length < 3:
        length = 30
    show_sample = int(vnow / vmax * length)
    if show_sample > length:
        show_sample = length
    if show_sample < 0:
        show_sample = 0
    string = '[{0}{1}] ({2}/{3})'.format('*' * show_sample, '-' * (length - show_sample), vnow, vmax)
    return string
