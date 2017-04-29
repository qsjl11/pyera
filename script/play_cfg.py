# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.group
import script.world
from script.mainflow import main_func


def init():
    if not '试炼设置' in game.data:
        game.data['试炼设置'] = {}
    game.data['试炼设置']['试炼队伍'] = None
    game.data['试炼设置']['试炼世界'] = None


def play_config():
    game.clr_cmd()
    game.pline()
    display_traget()
    game.pline('--')

    game.pcmd('[001]  改变试炼队伍', 1, change_target_group)
    game.p('    ')
    game.pcmd('[002]  改变试炼世界', 2, change_target_world)
    game.pl()
    game.pcmd('[099]  退出管理', 99, main_func)
    game.askfor_order()

def display_traget():
    target_group = game.data['试炼设置']['试炼队伍']
    target_world = game.data['试炼设置']['试炼世界']
    string = '试炼队伍：'
    if target_group == None:
        string = string + game.align('未设定', 12)
    else:
        string = string + game.align(target_group['队伍名称']+ '(编号：{})'.format(target_group['ID']), 30)
    string = string + '试炼世界：'
    if target_world == None:
        string = string + game.align('未设定', 12)
    else:
        string = string + target_world['世界名称'] + '(编号：{})'.format(target_world['ID'])

    game.pl(string)

def change_target_group():
    def change_group(group):
        game.data['试炼设置']['试炼队伍'] = group
        game.pl('试炼队伍已改为：' + group['队伍名称'])
        play_config()

    game.clr_cmd()
    game.pl('请选择试炼队伍：')
    script.group.display_group_list(change_group)
    game.pcmd('[001] 取消', 1, play_config)
    game.askfor_order()


def change_target_world():
    def change_world(world):
        game.data['试炼设置']['试炼世界'] = world
        game.pl('试炼世界已改为：' + world['世界名称'])
        play_config()

    game.clr_cmd()
    game.pl('请选择试炼世界：')
    script.world.display_world_list(change_world)
    game.pcmd('[001] 取消', 1, play_config)
    game.askfor_order()
