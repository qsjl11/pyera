# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
from script.mainflow import main_func
import copy
import random


def world_manager():
    game.clr_cmd()
    game.pline()
    display_world_list()
    game.pcmd('[001]  创造世界', 1, create_world)
    game.pl()
    game.pcmd('[099]  退出管理', 99, main_func)
    game.askfor_order()


def display_world_list(func=None):
    string = '----------------------------------' + '现有世界' + '---------------------------------------------'
    game.pl(string, style='title')
    string = game.align('ID', 4) + game.align('世界类型', 15) + game.align('剧情容量', 15) + game.align('构建点数', 15)
    game.pl(string)
    for w in game.data['世界列表']:
        string = game.align(w['ID'], 4) + game.align(w['世界名称'], 15) \
                 + game.align(w['剧情容量'], 15) + game.align(w['构建点数'], 15)
        if func==None:
            game.pl(string)
        else:
            game.pcmd(string+'\n',w['ID'],func,arg=(w,))
    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')


def create_world():
    game.clr_cmd()
    string = '----------------------------------' + '可选世界' + '---------------------------------------------'
    game.pl(string, style='title')
    string = game.align('创造编号', 15) + game.align('世界类型', 15) + game.align('剧情容量', 15) + game.align('构建点数', 15)
    game.pl(string)

    numid = 0
    for w in game.data['世界']:
        id = '[{:0>3}]'.format(numid)
        string = game.align(id, 15) + game.align(w['世界名称'], 15) + game.align(w['剧情容量'], 15) + game.align(w['构建点数'], 15)
        game.pcmd(string + '\n', numid, _create_world, arg=(numid,))
        numid += 1
    game.askfor_order()


def _create_world(type_id):
    tpl = copy.deepcopy(game.data['世界'][type_id])
    game.pl("生成新世界：" + tpl['世界名称'] + "?")
    game.call_event('生成世界_'+tpl['世界名称'])
    #是否创建世界
    ans = lib.yes_or_no()
    game.pl()
    if ans == True:
        tpl['ID'] = lib.get_id()
        game.data['世界列表'].append(tpl)
    world_manager()

