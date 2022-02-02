import erajs.api as a
from ..人物相关.character_creat import creat_normal_character
from ..人物相关.character_class import new_character_dict
from erb.系统相关.页面.check_character import *
#未完成
def event1():
    a.page()
    a.mode()
    a.t('本次入学2人')
    a.t()
    for i in range(0,2):
        c = new_character_dict()
        c['性别'] = '女性'
        c = creat_normal_character(c)
        a.sav()['character_list']['学生'][c['CharacterId']] = c
        a.sav()['character_list']['character_number'] +=1
    a.goto(check_character)

