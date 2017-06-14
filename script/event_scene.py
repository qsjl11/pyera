# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import random


@game.bind_event_deco('生成剧情_赤手蠢贼')
def 生成剧情_赤手蠢贼():
    tpl={}
    tpl['名称'] = '赤手蠢贼'
    tpl['难度'] = random.choice([1,3,5,7,9])
    return tpl

@game.bind_event_deco('设置剧情_赤手蠢贼')
def 设置剧情_赤手蠢贼(tpl):
    game.p('难度设置：')
    def set(x):
        tpl['难度']=x
    lib.list_nums([1,3,5,7,9],set , tpl['难度'])

@game.bind_event_deco('调整剧情_赤手蠢贼')
def 调整剧情_赤手蠢贼(tpl):
    def set(x):
        tpl['难度']=x
    lib.list_nums([1,3,5,7,9],set , tpl['难度'])

@game.bind_event_deco('进行剧情_赤手蠢贼')
def 进行剧情_赤手蠢贼(tgroup, tworld, tscene):
    game.pl('草丛里蹦出三个蠢贼，赤手空拳的奔向' + tgroup.data['队伍名称'])
    target=tgroup.随机一人
    game.plwait(target.姓名 + '还击')
    re = target.近战鉴定(tscene.难度 * 10)
    if re == True:
        game.pl('三个贼徒被打跑了')
        target.当前体力 -= 10
    if re == False:
        game.pl(target.姓名 + '被打的鼻青脸肿')
        target.当前体力 -= 50