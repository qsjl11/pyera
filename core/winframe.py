# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk
import sys
import threading
import uuid

# 显示主框架
root = Tk()
root.title("pyera")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding='3 3 3 3')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# 缩放角标
ttk.Sizegrip(root).grid(column=0, row=0, sticky=(S, E))
# 显示窗口
textbox = Text(mainframe, width='150', height='60')
textbox.grid(column=0, row=0, sticky=(N, W, E, S))

# 垂直滚动条
s_vertical = ttk.Scrollbar(mainframe, orient=VERTICAL, command=textbox.yview)
textbox.configure(yscrollcommand=s_vertical.set)
s_vertical.grid(column=1, row=0, sticky=(N, E, S))

# 水平滚动条
# s_horizontal = ttk.Scrollbar(mainframe, orient=HORIZONTAL, command=textbox.xview)
# textbox.configure(xscrollcommand=s_horizontal.set)
# s_horizontal.grid(column=0, row=2, sticky=(W, E, S))

# 输入栏
order = StringVar()
inputbox = ttk.Entry(mainframe, textvariable=order)
inputbox.grid(column=0, row=1, sticky=(W, E, S))

# 构建菜单栏
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar
menufile = Menu(menubar)
menuother = Menu(menubar)
menubar.add_cascade(menu=menufile, label=' 文件')
menubar.add_cascade(menu=menuother, label=' 其他')

menufile.add_command(label='重新开始')
menufile.add_command(label='退出', command=lambda: sys.exit())

menuother.add_command(label='设置')
menuother.add_command(label='关于')
menuother.add_command(label='测试')

input_event_func = None


def send_input(*args):
    global input_event_func
    order = _getorder()
    input_event_func(order)
    clearorder()


textbox.bind("<Key>", lambda e: "break")
root.bind('<Return>', send_input)


# #######################################################################
# 运行函数
def run(open_func):
    flowthread = threading.Thread(target=open_func, name='flowthread')
    flowthread.start()
    root.mainloop()


def seeend():
    textbox.see(END)


# ######################################################################
# ######################################################################
# ######################################################################
# 双框架公共函数

def bind_return(func):
    global input_event_func
    input_event_func = func


# #######################################################################
# 输出格式化
textbox.tag_configure('standard', font='微软雅黑 14')
textbox.tag_configure('bold', font='微软雅黑 14 bold')
textbox.tag_configure('warning', font='微软雅黑 14', background='yellow')


def print(string, style='standard'):
    textbox.insert('end', string, style)
    seeend()


def clear_screen():
    io_clear_cmd()
    textbox.delete('1.0', END)


def style_def(style_name, **style_para):
    textbox.tag_configure(style_name, **style_para)


# #########################################################3
# 输入处理函数

def _getorder():
    return order.get()


def setorder(orderstr):
    order.set(orderstr)


def clearorder():
    order.set('')


# ############################################################

cmd_tag_map = {}


# 命令生成函数
def io_print_cmd(cmd_str, cmd_number):
    global cmd_tag_map
    cmd_tagname = str(uuid.uuid1())
    textbox.tag_configure(cmd_tagname, font='微软雅黑 14', foreground='#001466')
    if cmd_number in cmd_tag_map:
        io_clear_cmd(cmd_number)
    cmd_tag_map[cmd_number] = cmd_tagname

    def send_cmd(*args):
        order.set(cmd_number)
        send_input()

    def enter_func(*args):
        textbox.tag_configure(cmd_tagname, font='微软雅黑 14', foreground='#CC0029')

    def leave_func(*args):
        textbox.tag_configure(cmd_tagname, font='微软雅黑 14', foreground='#001466')

    textbox.tag_bind(cmd_tagname, '<1>', send_cmd)
    textbox.tag_bind(cmd_tagname, '<Enter>', enter_func)
    textbox.tag_bind(cmd_tagname, '<Leave>', leave_func)
    print(cmd_str, style=cmd_tagname)


# 清除命令函数
def io_clear_cmd(*cmd_numbers):
    global cmd_tag_map
    if cmd_numbers:
        for num in cmd_numbers:
            if cmd_numbers in cmd_tag_map:
                textbox.tag_add('standard',cmd_tag_map[num]+'.first',cmd_tag_map[num]+'.last')
                textbox.tag_delete(cmd_tag_map[num])
                cmd_tag_map.pop(num)
    else:
        for num in cmd_tag_map.keys():
            textbox.tag_add('standard', cmd_tag_map[num] + '.first', cmd_tag_map[num] + '.last')
            textbox.tag_delete(cmd_tag_map[num])
        cmd_tag_map.clear()
