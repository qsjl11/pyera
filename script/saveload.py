# -*- coding: UTF-8 -*-
import core.game as game
import os
import script.mainflow


def load_func(return_func=None):
    game.clr_cmd()
    if return_func == None:
        return_func = script.mainflow.main_func
    game.pl('读取游戏：' + game.savedir)
    game.pline()

    def loadhere(load_file_name):
        game.pl('load: ' + load_file_name)
        game.load(load_file_name)
        script.mainflow.main_func()

    def loadnodata(load_file_name):
        game.pl(load_file_name + ": 没有数据")
        game.askfor_order(print_order=False)

    for i in range(0, 11):
        load_file_name = 'save' + str(i)
        load_file_path = game.savedir + '\\' + load_file_name + '.save'

        # 此处修改显示信息
        if os.path.exists(load_file_path):
            file_str = '[{:0>2}]'.format(i) + "  " + load_file_path
            game.pcmd(file_str, i, loadhere, arg=(load_file_name,))
        else:
            file_str = '[{:0>2}]'.format(i) + "  ----"
            game.pcmd(file_str, i, loadnodata, arg=(load_file_name,))
        game.pl()
    game.pl()
    game.pcmd('[99] 返回', 99, return_func)
    game.askfor_order()


def save_func(return_func=None):
    game.clr_cmd()
    if return_func == None:
        return_func = script.mainflow.main_func
    game.pline()
    game.pl('游戏存储目录：' + game.savedir)
    game.pl()

    def savehere(save_file_name):
        game.pl('save: ' + save_file_path)
        game.save(save_file_name)
        save_func(return_func)

    for i in range(0, 11):
        save_file_name = 'save' + str(i)
        save_file_path = game.savedir + '\\' + save_file_name + '.save'

        # 此处修改显示信息
        if os.path.exists(save_file_path):
            file_str = '[{:0>2}]'.format(i) + "  " + save_file_path
        else:
            file_str = '[{:0>2}]'.format(i) + "  ----"
        game.pcmd(file_str, i, savehere, arg=(save_file_name,))
        game.pl()
    game.pl()
    game.pcmd('[99] 返回', 99, return_func)
    game.askfor_order()
