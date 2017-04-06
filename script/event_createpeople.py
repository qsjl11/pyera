# -*- coding: UTF-8 -*-
import core.game as game

@game.bind_event_deco('生成人物', event_mark='倾向处理')
def event_func_生成世界_基础世界(tpl):
    game.pl('倾向处理','notice')
    return tpl

@game.bind_event_deco('生成人物', event_mark='职业处理')
def event_func_生成世界_基础世界(tpl):
    game.pl('职业处理','notice')
    return tpl