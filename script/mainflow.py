# -*- coding: UTF-8 -*-
import core.game as game


def open_func(*args):
    game.pline()
    game.pl('pyera 启动中，准备开始游戏')
    game.pcmd('[001]   开始游戏', 1, newgame_func)
    game.pl('')
    game.pcmd('[002] 字符串测试', 2, len_test,arg=('[001]   开始游戏','pyera 启动中'))
    game.p('\n')
    game.askfor_order()


def newgame_func():
    game.clr_cmd(1)
    game.pline()
    game.pl('请输入名字:')
    name = game.askfor_str()
    game.plwait('取名字为：' + str(name))
    game.clr_screen()

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