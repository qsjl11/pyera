# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
from script.mainflow import main_func
import script.people

def group_manager():
    game.clr_cmd()
    game.pline()
    display_group_list()
    game.pcmd('[001]  新建队伍', 1, create_group)
    game.pl()
    game.pcmd('[099]  退出管理', 99, main_func)
    game.askfor_order()


def display_group_list(func=None):
    if func==None:
        func=group_control
    string = '----------------------------------' + '队伍列表' + '---------------------------------------------'
    game.pl(string, style='title')
    string = game.align('队伍编号', 15) + game.align('队伍名称', 15) + game.align('队伍队员', 15)
    game.pl(string)

    def display_memebr_of_groups(agroup):
        string = ''
        for i in range(0, 6):
            if agroup['队伍队员'][i] != {}:
                string = string + agroup['队伍队员'][i]['姓名'] + '|'
        if string == '':
            string = '暂无队员'
        return string

    numid = 101
    for g in game.data['队伍列表']:
        id = '[{:0>3}]'.format(numid)
        string = game.align(id, 15) + game.align(g['队伍名称'], 15) + display_memebr_of_groups(g)
        game.pcmd(string + '\n', numid, func, arg=(g,))
        numid += 1

    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')


def group_control(g):
    import script.people
    game.clr_cmd()
    game.pline()
    string = '----------------------------------' + '队伍配置' + '---------------------------------------------'
    game.pl(string, style='title')
    string = '队伍名称：  ' + g['队伍名称']
    game.pl(string)
    for i in range(0, 6):

        def add_people_here(people, i=i):
            clean_people(people)
            add_people_to_group(g, people, i)
            group_control(g)

        def cancel_people_here(i=i):
            g['队伍队员'][i] = {}
            group_control(g)

        num_cmd = (i + 1) * 10

        game.pcmd('[0' + str(i + 1) + '1]设置', num_cmd + 1, script.people.dispaly_people_list, arg=add_people_here)
        game.p('   ')
        game.pcmd('[0' + str(i + 1) + '2]清空', num_cmd + 2, cancel_people_here)
        string = '     队员 ' + str(i + 1) + '：  '
        if g['队伍队员'][i] == {}:
            string += '无'
        else:
            string += g['队伍队员'][i]['姓名']
        game.p(string + '\n')
    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')

    def add_people(people):
        clean_people(people)
        add_people_to_group(g, people)
        group_control(g)

    game.pcmd('[001]  添加队员', 1, script.people.dispaly_people_list, arg=add_people)
    game.pl()
    game.pcmd('[099]  返回列表', 99, group_manager)
    game.askfor_order()


def create_group():
    tpl = {}
    game.p('请输入队伍名称：', style='notice')
    name = game.askfor_str()
    tpl['队伍名称'] = name
    tpl['ID'] = lib.get_id()
    tpl['队伍队员'] = []
    for i in range(0, 6):
        tpl['队伍队员'].append({})
    game.data['队伍列表'].append(tpl)
    group_manager()


def add_people_to_group(g, people, place=-1):
    if place == -1:
        for i in range(0, 6):
            if g['队伍队员'][i] == {}:
                g['队伍队员'][i] = people
                return True
    if place >= 0 and place <= 5:
        g['队伍队员'][place] = people
        return True
    return False

def which_group(people_or_id):
    if type(people_or_id)==int:
        people_or_id=lib.getbyID(people_or_id)
    for g in game.data['队伍列表']:
        if people_or_id in g['队伍队员']:
            return g

def clean_people(people_or_id):
    if type(people_or_id)==int:
        people_or_id = lib.getbyID(people_or_id)
    for g in game.data['队伍列表']:
         for p in range(len(g['队伍队员'])):
             if people_or_id == g['队伍队员'][p]:
                 g['队伍队员'][p]={}