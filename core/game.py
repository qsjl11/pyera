# -*- coding: UTF-8 -*-
import core.io as io
import core.flow
import core.data

def init(main_flow):
    io.clear_screen()
    io.clearorder()
    core.flow.cmd_clear()
    # 载入数据库数据
    core.data.init()
    # 设置背景颜色
    io.set_background(core.data.gamedata()['core_cfg']['background_color'])
    foreground_c=core.data.gamedata()['core_cfg']['font_color']
    background_c=core.data.gamedata()['core_cfg']['background_color']
    onbutton_color=core.data.gamedata()['core_cfg']['onbutton_color']
    font=core.data.gamedata()['core_cfg']['font']
    fontsize=core.data.gamedata()['core_cfg']['font_size']
    io.init_style(foreground_c,background_c,onbutton_color,font,fontsize)
    main_flow()

def run(main_func):
    def _init():
        init(main_func)
    core.io.run(_init)