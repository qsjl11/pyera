# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk

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
textbox = Text(mainframe, wrap='none', width='150', height='60')
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
menuedit = Menu(menubar)
menuabout = Menu(menubar)
menubar.add_cascade(menu=menufile, label=' 文件')
menubar.add_cascade(menu=menuedit, label=' 设置')
menubar.add_cascade(menu=menuabout, label=' 关于')

menufile.add_command(label='重新开始')
menufile.add_command(label='退出', command=lambda: None)

root.mainloop()
