# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
from script.mainflow import main_func


def group_manager():
    game.clr_cmd()
    game.pline()
    display_group_list()
    game.pcmd('[001]  新建队伍', 1, create_group)
    game.pl()
    game.pcmd('[099]  退出管理', 99, main_func)
    game.askfor_order()


def display_group_list():
    string = '----------------------------------' + '队伍配置' + '---------------------------------------------'
    game.pl(string, style='title')
    string = game.align('队伍编号', 15) + game.align('队伍名称', 15) + game.align('队伍队员', 15)
    game.pl(string)

    def display_memebr_of_groups(agroup):
        string = ''
        for i in range(0, 6):
            if agroup['队伍队员'][i] != {}:
                string = string + agroup['队伍队员'][i] + '|'
        if string == '':
            string = '暂无队员'
        return string

    numid = 0
    for w in game.data['队伍列表']:
        id = '[{:0>3}]'.format(numid)
        string = game.align(id, 15) + game.align(w['队伍名称'], 15) + display_memebr_of_groups(w)
        game.pcmd(string + '\n', numid, lambda: None, arg=(numid,))
        numid += 1

    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')


def create_group():
    tpl = {}
    game.p('请输入队伍名称：', style='notice')
    name = game.askfor_str()
    tpl['队伍名称'] = name
    tpl['队伍队员'] = []
    for i in range(0, 6):
        tpl['队伍队员'].append({})
    game.data['队伍列表'].append(tpl)
    group_manager()
