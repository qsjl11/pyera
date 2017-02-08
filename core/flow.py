# -*- coding: UTF-8 -*-
import core.io as io

# 管理所有flow的变量
flow_control = []


def get_flow(flow_name):
    for f in flow_control:
        if f.name == flow_name:
            return f
    io.warn('没有名为' + flow_name + '的flow，所有已注册的flow如下：')
    for f in flow_control:
        io.printl(f.name)
    io.warn('显示完毕')
    return None


def reg_flow(the_flow):
    if not the_flow.name in [x.name for x in flow_control]:
        flow_control.append(the_flow)
        return
    io.warn(the_flow.name + '不能被注册，因为已有同名flow存在')


def del_flow(flow_name):
    f = get_flow(flow_name)
    if f == None:
        io.warn(flow_name + '没有找到，无法删除')

    flow_control.remove(f)


# 绑定执行flow的方法


class Flow:
    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name  # flow_name
        reg_flow(self)
        # self.next_flow = None  # flow_name
        self.cmd_dic = {}
        self.runable = True
        self.sendmsg = None
        return

    # 该流程显示的内容
    def func(self):
        pass

    def run(self):
        self.cmd_dic = {}
        self.bind()
        self.func_generator = self.func()
        if str(self.func_generator.__class__) == "<class 'generator'>":
            self.core()

    def core(self):
        try:
            request = self.func_generator.send(self.sendmsg)
            if request == 'str':
                io.bind_return(self.getstr)

        except StopIteration:
            pass

    def getstr(self, *args):
        self.sendmsg = io.getorder()
        self.bind()
        self.core()

    # 添加命令的方法
    def cmd(self, order_number, cmd_str, flow_name):
        if order_number in self.cmd_dic.keys():
            io.warn('命令冲突：' + str(order_number) + '已被使用' + cmd_str)
        self.cmd_dic[order_number] = flow_name
        return cmd_str

    def bind(self):
        io.bind_return(self.goto_flow)

    def goto_flow(self, *args):
        order = io.getorder()
        if order == '':
            io.clearorder()
            self.enter_default()
        if order.isdigit() and (int(order) in self.cmd_dic.keys()):
            io.clearorder()
            next_flow = get_flow(self.cmd_dic[int(order)])
            next_flow.run()

    # 当按下回车时且没有命令时，所执行的函数
    def enter_default(self):
        pass
