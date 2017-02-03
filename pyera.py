# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk


def _test_(*args):
    textbox.tag_configure('normalsize', font='微软雅黑 14')
    textbox.tag_configure('smallsize', font='微软雅黑 10')
    textbox.tag_configure('bigsize', font='微软雅黑 20')
    textbox.tag_configure('bluebg',background='blue')
    textbox.tag_configure('yellowbg', background='yellow')
    textbox.insert('end', '显示测试\n', ('smallsize'))
    textbox.insert('end', '显示测试\n', ('normalsize'))
    textbox.insert('end', '显示测试\n', ('bigsize'))
    textbox.insert('end', '显示测试\n', ('smallsize','bluebg'))
    textbox.insert('end', '显示测试\n', ('normalsize', 'bluebg'))
    textbox.insert('end', '显示测试\n', ('bigsize', 'bluebg'))
    textbox.insert('end', '显示测试\n', ('smallsize', 'yellowbg'))
    textbox.insert('end', '显示测试\n', ('normalsize', 'yellowbg'))
    textbox.insert('end', '显示测试\n', ('bigsize', 'yellowbg'))
    return


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
menufile.add_command(label='退出', command=lambda: None)

menuother.add_command(label='设置')
menuother.add_command(label='关于')
menuother.add_command(label='测试')

# 功能绑定
root.bind('<Return>', _test_)

root.mainloop()
