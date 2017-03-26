# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.people
import script.world
import script.play_cfg
from script.mainflow import main_func

class Target_people():
    def __init__(self,people_data):
        self.data=people_data
        self.当前体力=self.data['属性']['体力上限']
        self.体力上限=self.data['属性']['体力上限']

class Target_world():
    def __init__(self,world_data):
        self.data=world_data
        self.当前进度=self.data['剧情容量']

def main():
    game.clr_cmd()
    if game.data['试炼设置']['试炼人物'] == None or game.data['试炼设置']['试炼世界'] == None:
        game.pl('没有指定[试炼人物]或[试炼世界]，请于[试炼设置]中选择', 'notice')
        main_func()
    tpeople=Target_people(game.data['试炼设置']['试炼人物'])
    tworld=Target_world(game.data['试炼设置']['试炼世界'])


    game.pline()
    game.pl('剧情容量：' + lib.value_bar(tworld.当前进度, tworld.data['剧情容量']))
    game.pl('人物体力：' + lib.value_bar(tpeople.当前体力, tpeople.体力上限))
    game.askfor_order()
