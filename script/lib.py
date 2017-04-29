# -*- coding: UTF-8 -*-

from script.base_lib import *

def get_people_byID(id):
    return get_e_by_ID(id,game.data['人物列表'])

def getbyID(id):
    for t in game.data['script_cfg']['id_search_range']:
        re=get_e_by_ID(id,game.data[t])
        if re!=None:
            return re