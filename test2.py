

# # 管理所有flow的变量
# flow_control = []
#
#
# def get_flow(flow_name):
#     for f in flow_control:
#         if f.name == flow_name:
#             return f
#     io.warn('没有名为' + flow_name + '的flow，所有已注册的flow如下：')
#     for f in flow_control:
#         io.printl(f.name)
#     io.warn('显示完毕')
#     return None
#
#
# def reg_flow(the_flow):
#     if not the_flow.name in [x.name for x in flow_control]:
#         flow_control.append(the_flow)
#         return
#     io.warn(the_flow.name + '不能被注册，因为已有同名flow存在')
#
#
# def del_flow(flow_name):
#     f = get_flow(flow_name)
#     if f == None:
#         io.warn(flow_name + '没有找到，无法删除')
#
#     flow_control.remove(f)
#
#
# # 绑定执行flow的方法
#
#
# class Flow:
#     def __str__(self):
#         return self.name
#
#     def __init__(self, name):
#         self.name = name  # flow_name
#         reg_flow(self)
#         # self.next_flow = None  # flow_name
#         self.cmd_dic = {}
#         self.runable = True
#         self.sendmsg = None
#         self.innerflow_map = {}
#
#         # 预定innerflow内容
#         # 获得字符串
#         def getstr():
#             self.sendmsg = io.getorder()
#
#         self.create_innerflow('getstr', getstr)
#
#         # 获得数字
#         def getint():
#             number = io.getorder()
#             if number.isdigit():
#                 self.sendmsg = int(io.getorder())
#                 self.run_generator()  # 需要程序自己设定返回条件，否则无线循环这一段程序
#             else:
#                 io.printl('输入不是有效数字')
#
#         self.create_innerflow('getint', getint)
#
#         # 等待一个回车输入
#         def waitenter():
#             return
#
#         self.create_innerflow('waitenter', waitenter)
#
#         return
#
#     # 该流程显示的内容
#     def func(self):
#         pass
#
#     def run(self):
#         self.cmd_dic = {}
#         self.bind()
#         self.func_generator = self.func()
#         if str(self.func_generator.__class__) == "<class 'generator'>":
#             self.run_generator()
#
#     def run_generator(self):
#         self.bind()
#         try:
#             request = self.func_generator.send(self.sendmsg)
#             called_func = self.innerflow_map[request]
#             io.bind_return(called_func)
#
#         except StopIteration:
#             pass
#
#     def create_innerflow(self, name, func, auto_reture=True):
#         def innerflow(*args):
#             func()
#             if auto_reture == True:
#                 self.run_generator()
#
#         self.innerflow_map[name] = innerflow
#
#     # 添加命令的方法
#     def cmd(self, order_number, cmd_str, flow_name):
#         if order_number in self.cmd_dic.keys():
#             io.warn('命令冲突：' + str(order_number) + '已被使用' + cmd_str)
#         self.cmd_dic[order_number] = flow_name
#         return cmd_str
#
#     def bind(self):
#         io.bind_return(self.goto_flow)
#
#     def goto_flow(self, *args):
#         order = io.getorder()
#         if order == '':
#             io.clearorder()
#             self.enter_default()
#         if order.isdigit() and (int(order) in self.cmd_dic.keys()):
#             io.clearorder()
#             next_flow = get_flow(self.cmd_dic[int(order)])
#             next_flow.run()
#
#     # 当按下回车时且没有命令时，所执行的函数
#     def enter_default(self):
#         pass