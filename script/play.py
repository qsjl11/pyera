# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.people
import script.world
import script.play_cfg
from script.mainflow import main_func


class Target_group():
    def __init__(self, group_data):
        self.data = group_data

        def deal_people(p):
            if p == {}:
                return None
            else:
                return Target_people(p)

        self.p1 = deal_people(group_data['队伍队员'][0])
        self.p2 = deal_people(group_data['队伍队员'][1])
        self.p3 = deal_people(group_data['队伍队员'][2])
        self.p4 = deal_people(group_data['队伍队员'][3])
        self.p5 = deal_people(group_data['队伍队员'][4])
        self.p6 = deal_people(group_data['队伍队员'][5])
        self.peoplelist = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]


class Target_people():
    # def __str__(self):
    #     return self.姓名 + ' ' + str(self.当前体力) + ' ' + str(self.体力上限) + ' '

    def __init__(self, people_data):
        self.data = people_data
        self.姓名 = self.data['姓名']
        self.当前体力 = self.data['属性']['体力上限']
        self.体力上限 = self.data['属性']['体力上限']

    def 近战鉴定(self, difficult):
        here = self.data['经验']['近战经验'] * 5 + self.data['能力']['近战'] * 10
        game.pl('近战经验*5+近战*10=' + str(here) + '  难度:' + str(difficult))
        if difficult < here:
            return True
        else:
            return False


class Target_world():
    def __init__(self, world_data):
        self.data = world_data
        self.当前进度 = 1
        self.当前剧情 = world_data['剧情列表'][self.当前进度]


class Target_scene():
    def __init__(self, scene_data):
        self.data = scene_data
        self.名称 = self.data['名称']
        self.难度 = self.data['难度']


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
    string = '剧情容量：' + lib.value_bar(tworld.当前进度, tworld.data['剧情容量'])
    string += game.align('  下一剧情：' + tscene.名称, 40, 'right')
    game.pl(string)
    for p in tgroup.peoplelist:
        prefix = '人物体力(' + p.姓名 + ')：'
        prefix = game.align(prefix, 20)
        game.pl(prefix + lib.value_bar(p.当前体力, p.体力上限))
    game.pline('--', 'notice')

    def begin_scene():
        game.call_event('进行剧情_' + tworld.当前剧情['名称'], arg=(tgroup, tworld, tscene))
        main_play()

    game.pcmd('[100] 开始剧情', 100, begin_scene)
    game.pl()
    game.pcmd('[101] 调整剧情', 101, lambda: "break")
    game.pl()
    game.pcmd('[999] 结束试炼', 999, main_func)
    game.askfor_order()
