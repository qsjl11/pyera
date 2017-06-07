# -*- coding: UTF-8 -*-

import core.game as game


def yes_or_no():
    game.pcmd('[0] 是  ', 0, None)
    game.pcmd('[1] 否  ', 1, None)
    while True:
        ans = game.askfor_int()
        if ans == 0:
            return True
        if ans == 1:
            return False

def list_cmd( print_list, func_list ,first_cmd_num=None, spilt_mark=' / '):
    if len(print_list)!=len(func_list):
        game.pwarn("list_choice调用,print_list和func_list不匹配")
    for n in range(len(print_list)):
        if first_cmd_num==None:
            cmd_num=game.get_unused_cmd_num()
        else:
            cmd_num=first_cmd_num+n
        cmd_str='['+str(cmd_num)+'] '+str(print_list[n]) +spilt_mark
        game.pcmd(cmd_str, cmd_num, func_list[n])

def list_nums( num_list, deal_func, first_cmd_num=None, split_mark=' / '):
    def create_func(n):
        def _func():
            deal_func(n)
        return _func
    func_list=[]
    for nn in num_list:
        func_list.append(create_func(nn))
    list_cmd(num_list,func_list, first_cmd_num, split_mark)


def get_id():
    if not 'last_id' in game.data:
        game.data['last_id'] = 100
    game.data['last_id'] += 1
    return game.data['last_id']


def value_bar(vnow, vmax, length=30):
    if length < 3:
        length = 30
    show_sample = int(vnow / vmax * length)
    if show_sample > length:
        show_sample = length
    if show_sample < 0:
        show_sample = 0
    string = '[{0}{1}] ({2}/{3})'.format('*' * show_sample, '-' * (length - show_sample), vnow, vmax)
    return string


def get_e_by_ID(id_num, list):
    for p in list:
        if p['ID'] == id_num:
            return p
    return None


class IterExceptNoneInList():
    def __init__(self, list):
        self.l = iter(list)

    def __iter__(self):
        return self

    def __next__(self):
        nextpeople = None
        try:
            while nextpeople == None:
                nextpeople = next(self.l)
            return nextpeople
        except StopIteration:
            raise StopIteration
