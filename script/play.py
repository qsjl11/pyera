# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.people
import script.world
import script.play_cfg
from script.mainflow import main_func
from script.target_class import *

tgroup = None
tworld = None
tscene = None


def init_play():
    global tgroup, tworld, tscene
    if game.data['试炼设置']['试炼队伍'] == None or game.data['试炼设置']['试炼世界'] == None:
        game.pl('没有指定[试炼队伍]或[试炼世界]，请于[试炼设置]中选择', 'notice')
        main_func()
    tgroup = Target_group(game.data['试炼设置']['试炼队伍'])
    tworld = Target_world(game.data['试炼设置']['试炼世界'])
    tscene = Target_scene(tworld.当前剧情)
    main_play()


def main_play():
    global tgroup, tworld, tscene
    game.clr_cmd()
    game.pline()
    string = game.align('剧情进度:', 14) + lib.value_bar(tworld.当前进度, tworld.data['剧情容量'])
    string += game.align('下一剧情:' + tscene.名称, 30, 'right')
    game.pl(string)
    for p in tgroup.所有人物:
        prefix = p.姓名 + '|体力:'
        prefix = game.align(prefix, 14)
        game.pl(prefix + lib.value_bar(p.当前体力, p.体力上限))

    string = '----------------------------------' + '设置剧情 ' + ': ' + tscene.名称 + ' --------------------------------'
    game.pl(string, style='title')
    game.call_event('设置剧情_' + tscene.名称, arg=(tscene.data,))
    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')

    def begin_scene():
        global tscene
        game.call_event('进行剧情_' + tworld.当前剧情['名称'], arg=(tgroup, tworld, tscene))
        tworld.下一剧情()
        if tworld.当前进度 <= tworld.data['剧情容量']:
            tscene=Target_scene(tworld.当前剧情)
        main_play()

    if tworld.当前进度<=tworld.data['剧情容量']:
        game.pcmd('[100] 开始剧情', 100, begin_scene)
    else:
        game.p('[100] 开始剧情', style='grey')
    game.pl()
    game.pcmd('[999] 结束试炼', 999, main_func)
