# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.people
import script.world
import script.play_cfg
from script.mainflow import main_func


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


tpeople = None
tworld = None
tscene = None


def init_play():
    global tpeople, tworld, tscene
    if game.data['试炼设置']['试炼人物'] == None or game.data['试炼设置']['试炼世界'] == None:
        game.pl('没有指定[试炼人物]或[试炼世界]，请于[试炼设置]中选择', 'notice')
        main_func()
    tpeople = Target_people(game.data['试炼设置']['试炼人物'])
    tworld = Target_world(game.data['试炼设置']['试炼世界'])
    tscene = Target_scene(tworld.当前剧情)
    main_play()


def main_play():
    global tpeople, tworld, tscene
    game.clr_cmd()
    game.pline()
    string = '剧情容量：' + lib.value_bar(tworld.当前进度, tworld.data['剧情容量'])
    string += game.align('  下一剧情：' + tscene.名称, 40, 'right')
    game.pl(string)
    game.pl('人物体力：' + lib.value_bar(tpeople.当前体力, tpeople.体力上限))
    game.pline('--', 'notice')

    def begin_scene():
        game.call_event('进行剧情_' + tworld.当前剧情['名称'], arg=(tpeople, tworld, tscene))
        main_play()

    game.pcmd('[100] 开始剧情', 100, begin_scene)
    game.pl()
    game.pcmd('[101] 调整剧情', 101, lambda: "break")
    game.pl()
    game.pcmd('[999] 结束试炼', 999, main_func)
    game.askfor_order()
