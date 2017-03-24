# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
from script.mainflow import main_func
import copy
import random


def world_manager():
    game.clr_cmd()
    game.pline()
    # dispaly_student_list()
    game.pcmd('[101]  创造世界', 101, create_world)
    game.pl()
    game.pcmd('[999]  退出管理', 999, main_func)
    game.askfor_order()


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
        game.pcmd(string+'\n', numid, _create_world, arg=(numid,))
        numid += 1
    game.askfor_order()

def _create_world(type_id):
    game.pl(type_id)


