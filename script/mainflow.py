# -*- coding: UTF-8 -*-
import core.game as game
import script.saveload as saveload
import random

def open_func(*args):
    game.pline()
    game.pl('pyera 启动中，准备游戏')
    game.pl('pyera 启动中，准备完成')
    game.pl(str(random.randint(1,10)))
    open_menu()


def open_menu():
    game.pline()
    game.pcmd('[001]  开始游戏', 1, newgame_func)
    game.pl()
    game.pcmd('[002]  读取游戏', 2, saveload.load_func,arg=(open_menu,))
    game.askfor_order()

def newgame_func():
    game.pline()
    game.pl('请输入名字:')
    name = game.askfor_str()
    game.data['player_name']=name
    game.plwait('取名字为：' + str(name))
    main_func()

def main_func():
    game.clr_cmd()
    game.pline()
    game.pl('玩家姓名：'+game.data['player_name'])
    game.pline()
    game.pcmd('[001]  保存游戏', 1, saveload.save_func)
    game.pl()
    game.pcmd('[002]  读取游戏', 2, saveload.load_func)
    game.askfor_order()

def len_test(*args):
    game.pline()
    game.pl('01234567890123456789012345678901234567890')
    outstring = game.align('字符串', 20, 'left')
    outstring = outstring + game.align('字数', 15, 'right')
    game.pl(outstring)
    for string in args:
        outstring=game.align(string,20,'left')
        outstring=outstring+game.align(str(game.display_len(string)),15,'right')
        game.pl(outstring)
    game.plwait('字数分析完成')