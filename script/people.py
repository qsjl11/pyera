# -*- coding: UTF-8 -*-
import core.game as game
import script.lib as lib
import script.mainflow
import copy
import random


def people_manager():
    game.clr_cmd()
    game.pline()
    dispaly_people_list()
    game.pcmd('[001]  召唤人物', 1, summon_people)
    game.pl()
    game.pcmd('[099]  退出管理', 99, script.mainflow.main_func)
    game.askfor_order()


def dispaly_people_list(func=None):
    def display_people_here(people):
        display_people(people)
        game.plwait()
        people_manager()

    if func == None:
        func = display_people_here

    string = '----------------------------------' + '人物列表' + '---------------------------------------------'
    game.pl(string, style='title')
    string = game.align('ID', 4) + game.align('姓名', 15) + game.align('体力上限', 8) + '/  ' + \
             game.align('物资补给', 8) + '/  ' + game.align('神秘能源', 8)
    game.pl(string)

    for stu in game.data['人物列表']:
        string = game.align('[' + str(stu['ID']) + ']', 4) + game.align(stu['姓名'], 15) + \
                 game.align(stu['属性']['体力上限'], 8, just='right') + '/  ' + \
                 game.align(stu['属性']['物资补给'], 8, just='right') + '/  ' + \
                 game.align(stu['属性']['神秘能源'], 8, just='right') + '\n'
        game.pcmd(string, stu['ID'], func, arg=(stu,))

    string = '---------------------------------------------------------------------------------------'
    game.pl(string, style='title')


def summon_people(people_type='普通人'):
    if not '人物列表' in game.data:
        game.data['人物列表'] = []

    temp_student = _summon_people(people_type)
    display_people(temp_student)
    game.pl('是否接受这个人物？', style='notice')
    ans = lib.yes_or_no()
    game.pl()
    if ans == True:
        game.data['人物列表'].append(temp_student)
    people_manager()


def _summon_people(people_type='普通人'):
    tpl = copy.deepcopy(game.data['人物'][people_type])
    for attr in ['属性', '经验', '能力', '刻印']:
        for k, v in tpl[attr].items():
            if type(v) == list:
                tpl[attr][k] = random.randint(v[0], v[1])

    for k, v in tpl['素质'].items():
        num = random.randint(v['数量'][0], v['数量'][1])
        if num > len(v['内容']):
            num = len(v['内容'])
        tpl['素质'][k] = random.sample(v['内容'], num)

        for nn in range(len(tpl['素质'][k])):
            if type(tpl['素质'][k][nn]) == list:
                tpl['素质'][k][nn] = random.choice(tpl['素质'][k][nn])

    for k, v in tpl['装备'].items():
        tpl['装备'][k] = random.choice(v)
    for k, v in tpl['背景'].items():
        tpl['背景'][k] = random.sample(v, 1)

    # 随机取名字
    if tpl['姓名'] == "未命名":
        tpl['姓名'] = get_name(random.choice(tpl['素质']['性征']))
    tpl['ID'] = lib.get_id()

    # 调用事件
    tpl=game.call_event_as_tube('生成人物', tpl)
    return tpl


def display_people(people):
    def print_title(title):
        string = '□' + title + '□' + '-------------------------------------------------------------------------------'
        game.pl(string, style='title')

    def print_numattr(node, attrs, display_room, pre_fix=' '):
        string = ''
        for attr in attrs:
            temp = attr + ':' + pre_fix + str(node[attr]) + '  '
            string += game.align(temp, display_room)
        game.pl(string)

    def print_talent(node, attrs, pre_fix=' '):
        for attr in attrs:
            temp_value = ['[' + iter_var + ']' for iter_var in node[attr]]
            temp = attr + ':' + pre_fix + ''.join(temp_value)
            game.pl(temp)

    game.pline()
    game.pl('姓名：' + people['姓名'])

    print_title('属性')
    attrs = ["体力上限", "物资补给", "神秘能源", "认同程度", "因果点数", "因果碎片"]
    print_numattr(people['属性'], attrs, 15)

    print_title('经验')
    attrs = ["近战经验", "远战经验", "科技经验", "神秘经验"]
    print_numattr(people['经验'], attrs, 15)

    print_title('能力')
    attrs = ['见闻', '社交', '科技', '神秘']
    print_numattr(people['能力'], attrs, 15)
    attrs = ['近战', '远战', '基因锁']
    print_numattr(people['能力'], attrs, 15)

    print_title('刻印')
    attrs = people['刻印'].keys()
    print_numattr(people['刻印'], attrs, 15, ' LV')

    print_title('素质')
    attrs = ['性征', '性格', '倾向', '技能', '体质', '天赋']
    print_talent(people['素质'], attrs)

    print_title('背景')
    attrs = ['职业']
    print_talent(people['背景'], attrs)

    print_title('装备')
    attrs = ['装备一', '装备二']
    print_numattr(people['装备'], attrs, 30)
    attrs = ['装备三', '装备四']
    print_numattr(people['装备'], attrs, 30)


def get_name(xingbie='男'):
    xing = random.choice(game.data['姓名']['姓'])
    if xingbie in ('男', '可爱的男孩子'):
        ming = random.choice(game.data['姓名']['男名'])
    elif xingbie == '女':
        ming = random.choice(game.data['姓名']['女名'])
    else:
        ming = ''
    return xing + ming
