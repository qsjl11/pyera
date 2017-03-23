# -*- coding: UTF-8 -*-
import core.game as game
import script.saveload as saveload
import script.lib as lib
import random


def test():
    import script.student
    script.student.summon_student()
    # script.student.display_sutdent(student)


def open_func(*args):
    game.pline()
    game.pl('pyera 启动中，准备游戏')
    game.def_style('notice', foreground='#DCE441')
    game.def_style('title', foreground='#E1FFFF')
    if not '人物列表' in game.data:
        game.data['人物列表'] = []
    game.pl('pyera 启动中，准备完成')
    # test()
    open_menu()


def open_menu():
    game.pline()
    game.pcmd('[001]  开始游戏', 1, newgame_func)
    game.pl()
    game.pcmd('[002]  读取游戏', 2, saveload.load_func, arg=(open_menu,))
    game.askfor_order()


def newgame_func():
    game.pl()
    game.pline()
    game.pl('请输入学院名称:')
    name = game.askfor_str()
    game.data['学校名称'] = name
    game.pl('学院名称为：' + str(name))
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
    game.pl('玩家姓名：' + game.data['学校名称'])
    game.p('学生名称：')
    for stu in game.data['人物列表']:
        game.p(stu['属性']['姓名']+' ')
    game.pl()
    game.pline('--')
    import script.student
    game.pcmd('[001]  学生管理', 1, script.student.student_manager)
    game.pl()
    game.pcmd('[100]  保存游戏', 100, saveload.save_func)
    game.p('    ')
    game.pcmd('[101]  读取游戏', 101, saveload.load_func)
    game.askfor_order()
