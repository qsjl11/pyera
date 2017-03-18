# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import random


def summon_student():
    tpl = game.data['人物']['普通人']
    for attr in ['属性', '经验', '能力', '刻印']:
        for k, v in tpl[attr].items():
            if type(v) == list:
                tpl[attr][k] = random.randint(v[0], v[1])
        game.pl(tpl[attr])

    for k, v in tpl['素质'].items():
        num = random.randint(v['数量'][0], v['数量'][1])
        if num > len(v['内容']):
            num = len(v['内容'])
        tpl['素质'][k] = random.sample(v['内容'], num)

        for nn in range(len(tpl['素质'][k])):
            if type(tpl['素质'][k][nn]) == list:
                tpl['素质'][k][nn] = tpl['素质'][k][nn][random.randint(0, len(tpl['素质'][k][nn]) - 1)]
    game.pl(tpl['素质'])

    for k, v in tpl['装备'].items():
        tpl['装备'][k] = random.choice(v)
    game.pl(tpl['装备'])
    for k, v in tpl['背景'].items():
        tpl['背景'][k] = random.choice(v)
    game.pl(tpl['背景'])
