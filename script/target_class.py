import core.game as game
import script.lib as lib
import copy
import random
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

    @property
    def 所有人物(self):
        people_iter = lib.IterExceptNoneInList(self.peoplelist)
        return people_iter

    @property
    def 随机一人(self):
        people_list = copy.copy(self.peoplelist)
        while None in people_list:
            people_list.remove(None)
        return random.choice(people_list)


class Target_people():
    # def __str__(self):
    #     return self.姓名 + ' ' + str(self.当前体力) + ' ' + str(self.体力上限) + ' '

    def __init__(self, people_data):
        self.data = people_data
        self._current_hp = self.data['属性']['体力上限']

    def 近战鉴定(self, difficult):
        here = self.data['经验']['近战经验'] * 5 + self.data['能力']['近战'] * 10
        game.pl('近战经验*5+近战*10=' + str(here) + '  难度:' + str(difficult))
        if difficult < here:
            return True
        else:
            return False

    @property
    def 姓名(self):
        return self.data['姓名']

    @property
    def 当前体力(self):
        return self._current_hp

    @当前体力.setter
    def 当前体力(self, value):
        self._current_hp = value

    @property
    def 体力上限(self):
        return self.data['属性']['体力上限']


class Target_world():
    def __init__(self, world_data):
        self.data = world_data
        self._current_process = 1

    @property
    def 当前进度(self):
        return self._current_process

    @property
    def 当前剧情(self):
        return self.data['剧情列表'][self.当前进度]


class Target_scene():
    def __init__(self, scene_data):
        self.data = scene_data

    @property
    def 名称(self):
        return self.data['名称']

    @property
    def 难度(self):
        return self.data['难度']
