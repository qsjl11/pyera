# -*- coding: UTF-8 -*-
import core.game as game


@game.bind_event_deco('生成剧情_赤手蠢贼')
def 生成剧情_赤手蠢贼():
    tpl = {}
    tpl['名称'] = '赤手蠢贼'
    tpl['难度'] = 1
    return tpl


@game.bind_event_deco('进行剧情_赤手蠢贼')
def 进行剧情_赤手蠢贼(tpeople, tworld, tscene):
    game.pl('草丛里蹦出三个蠢贼，赤手空拳的向' + tpeople.姓名)
    game.pl(tpeople.姓名 + '还击')
    re = tpeople.近战鉴定(tscene.难度 * 10)
    if re == True:
        game.pl('三个贼徒被打跑了')
        tpeople.当前体力 -= 10
    if re == False:
        game.pl(tpeople.姓名 + '被打的鼻青脸肿')
        tpeople.当前体力 -= 50