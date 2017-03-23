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
    if not 'next_id' in game.data:
        game.data['next_id'] = 0
    game.data['next_id'] += 1
    return game.data['next_id'] - 1
