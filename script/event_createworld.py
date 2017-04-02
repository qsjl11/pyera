# -*- coding: UTF-8 -*-
import core.game as game

@game.bind_event_deco('生成世界_基础世界')
def event_func_生成世界_基础世界(tpl):
    game.pl('生成世界_基础世界:'+tpl['世界名称'], style='notice')
    tpl['剧情列表']=[]
    tpl['剧情配置']=[]
    for i in range(0,tpl['剧情容量']):
        tpl['剧情列表'].append(game.call_event('生成剧情_赤手蠢贼'))
    game.pl('剧情列表：','notice')
    game.pl(tpl['剧情列表'])
    return tpl

