# -*- coding: UTF-8 -*-
import core.io as io
import core.flow as flow
from core.data import gamedata


@flow.create_flow(flow_name='open_flow')
def open_func():
    io.printline()
    io.print('pyera 启动中，准备开始游戏')
    io.printl('pyera 启动中，准备开始游戏')
    flow.print_cmd('[001] 开始游戏', 1, newgame_func)
    io.print('\n')
    io.printl('pyera 启动中，准备开始游戏')
    io.printl(gamedata()['test']['firstName'])
    io.printl(str(gamedata()))

    flow.order_deal()



def newgame_func():
    flow.cmd_clear()
    io.printline()
    io.printl('请输入名字:')
    name = flow.askfor_str()
    io.printl('取名字为：' + str(name))
    io.clear_screen()

