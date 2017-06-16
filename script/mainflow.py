# -*- coding: UTF-8 -*-
import core.game as game
import script.saveload as saveload
import script.lib as lib
import random


def test():
    import math
    game.p(math.exp(3))
    return



def open_func(*args):
    game.pline()
    game.pl('pyera 启动中，准备游戏')
    game.def_style('notice', foreground='#DCE441')
    game.def_style('title', foreground='#E1FFFF')
    if not '人物列表' in game.data:
        game.data['人物列表'] = []
    if not '世界列表' in game.data:
        game.data['世界列表'] = []
    if not '队伍列表' in game.data:
        game.data['队伍列表'] = []
    import script.play_cfg
    script.play_cfg.init()
    game.pl(f'pyera 启动中，准备完成')
    test()
    open_menu()


def open_menu():
    # game.pline()
    # game.pcmd('[001]  开始游戏', 1, newgame_func)
    # game.pl()
    # game.pcmd('[002]  读取游戏', 2, saveload.load_func, arg=(open_menu,))
    # game.askfor_order()
    game.clr_cmd()
    game.pline()
    game.pcmd('[001]  开始游戏', 1)
    game.pl()
    game.pcmd('[002]  读取游戏', 2)

    @game.set_deal_cmd_func_deco
    def deal_func(order):
        if order==1:
            newgame_func()
        if order==2:
            saveload.load_func(open_menu)


def newgame_func():
    game.pl()
    game.pline()
    game.pl('请输入主神名称:')
    name = game.askfor_str()
    game.data['主神名称'] = name
    game.pl('主神名称为：' + str(name))
    game.pl('是否接受?')
    ans = lib.yes_or_no()
    if ans == True:
        main_func()
    if ans == False:
        newgame_func()


def main_func():
    game.clr_cmd()
    game.pl()
    game.pline()
    game.pl('主神名称：' + game.data['主神名称'])
    import script.play_cfg
    script.play_cfg.display_traget()
    game.pline('--')

    import script.play
    game.pcmd('[101]  开始试炼', 101, script.play.init_play)
    game.p('    ')
    import script.play_cfg
    game.pcmd('[102]  试炼设置', 102, script.play_cfg.play_config)
    game.pl()
    import script.people
    game.pcmd('[103]  人物管理', 103, script.people.people_manager)
    game.p('    ')
    import script.group
    game.pcmd('[104]  队伍管理', 104, script.group.group_manager)
    game.p('    ')
    import script.world
    game.pcmd('[105]  世界管理', 105, script.world.world_manager)
    game.pl()
    game.pcmd('[111]  保存游戏', 111, saveload.save_func)
    game.p('    ')
    game.pcmd('[112]  读取游戏', 112, saveload.load_func)

