import core.io as io
import core.flow
import core.data

open_flow = core.flow.Flow('open_flow')


def open_func():
    io.printline()
    yield 'waitenter'
    io.printl('pyera 启动中，准备开始游戏')
    yield 'waitenter'
    io.print('{0}\n{1}'.format(open_flow.cmd(1, '[001] 开始游戏', 'newgame_flow'), open_flow.cmd(2, '[002] 加载游戏', None)))


open_flow.func = open_func

newgame_flow = core.flow.Flow('open_flow')


def newgame_func():
    io.printline()
    io.printl('请输入名字:')
    name = yield 'getint'
    io.printl('取名字为：' + str(name))


newgame_flow.func = newgame_func
