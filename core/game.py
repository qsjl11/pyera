# -*- coding: UTF-8 -*-
import core.io as io
import core.flow
import core.data


# 系统函数#############################################################
# 初始化函数
_main_flow=None

def init(main_flow):
    global def_style
    io.clear_screen()
    io.clearorder()
    core.flow.cmd_clear()
    # 载入数据库数据
    core.data.init()
    # 设置背景颜色
    core.data._get_savefilename_path('')
    io.set_background(core.data.gamedata()['core_cfg']['background_color'])
    foreground_c = core.data.gamedata()['core_cfg']['font_color']
    background_c = core.data.gamedata()['core_cfg']['background_color']
    onbutton_color = core.data.gamedata()['core_cfg']['onbutton_color']
    font = core.data.gamedata()['core_cfg']['font']
    fontsize = core.data.gamedata()['core_cfg']['font_size']
    io.init_style(foreground_c, background_c, onbutton_color, font, fontsize)
    io.style_def('warning', foreground='red', underline=True)
    def_style = io.style_def
    core.flow.reset_func=reset
    global _main_flow
    _main_flow=main_flow
    main_flow()


def run(main_func):
    """运行函数"""

    def _init():
        init(main_func)

    core.io.run(_init)


def console_log(string):
    """向控制台输入信息"""
    print('game log:')
    print(string + '\n')

def reset():
    global _main_flow
    clr_cmd()
    clr_screen()
    clr_order()
    init(_main_flow)

# 输入处理函数 #################################################################

# 请求输入命令
askfor_order = core.flow.order_deal

# 请求输入一个字符串
askfor_str = core.flow.askfor_str

# 请求输入一个数字
askfor_int = core.flow.askfor_int

# 清空输入栏
clr_order = io.clearorder


# 暂停一下
def wait():
    core.flow.askfor_wait()


# 输出相关函数#############################################################
last_char = '\n'


def p(string, style=('standard',)):
    global last_char
    if len(string) > 0:
        last_char = string[-1:]
    io.print(string, style)


# 输出一行
def pl(string='', style='standard'):
    """输出一行"""
    global last_char
    if not last_char=='\n':
        p('\n')
    p(str(string), style)
    if not last_char=='\n':
        p('\n')


def pline(sample='▃'):
    """输出一条横线"""
    pl(sample * 45)


def pwarn(string, style='warning'):
    """输出警告"""
    pl(string, style)


def pwait(string, style='standard'):
    """输出并等待"""
    p(string, style)
    wait()


def plwait(string='', style='standard'):
    """输出一行并等待"""
    pl(string, style)
    wait()


clr_screen = io.clear_screen

# 格式化输出函数 ##############################################################

def_style = io.style_def


def _is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def display_len(text):
    """计算字符串显示长度，中文长度2，英文长度1"""
    stext = str(text)
    # utext = stext.encode("utf-8")  # 对字符串进行转码
    cn_count = 0
    for u in stext:
        if _is_chinese(u):
            cn_count += 2  # 计算中文字符占用的宽度
        else:
            cn_count += 1  # 计算英文字符占用的宽度
    return cn_count


def align(text, width, just='left'):
    """返回对齐的字符串函数，默认左对齐，左：left，右：right"""
    text = str(text)
    count = display_len(text)
    if just == "right":
        return " " * (width - count) + text
    elif just == "left":
        return text + " " * (width - count)


# 命令相关函数#################################################################

# 输出命令
def pcmd(cmd_str, cmd_number, cmd_func, arg=(), normal_style='standard', on_style='onbutton'):
    global last_char
    if len(cmd_str) > 0:
        last_char = cmd_str[-1:]
    core.flow.print_cmd(cmd_str, cmd_number, cmd_func, arg, normal_style, on_style)


# 清除命令，没有参数则清除所有命令
clr_cmd = core.flow.cmd_clear

# 绑定或重新绑定一个命令
bind_cmd = core.flow.bind_cmd

# 数据处理相关函数 ###############################################################

# 返回主数据集合
data = core.data.gamedata()

# 获得存档目录
savedir = core.data._get_savefilename_path('')[:-6]

# 保存数据集合到文件, 也可将可以json序列化的data保存到某个文件中
save = core.data.save

# 从文件中加载数据集合, selfdata为True时，只返回反序列化之后的数据，不会将数据加载到gamedata
load = core.data.load
