
from ..人物相关.character_creat import creat_normal_character
from ..人物相关.character_class import new_character_dict
from ..系统相关.页面.check_character import *

def event():
    a.page()
    a.mode()
    a.t('本次入学1人')
    a.t()
    c = new_character_dict()
    c['基本信息']['性别'] = '女性'
    c = creat_normal_character(c)
    a.sav()['character_list']['学生'][c['基本信息']['CharacterId']] = c
    a.sav()['character_list']['character_number'] +=1
    a.goto(check_character)
