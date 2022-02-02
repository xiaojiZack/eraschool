from  erajs import api as a
import funcs as f
from .creat_leading_character import creat_leading_character
from erb.系统相关.事件.event_1_入学 import *
def game_start():
     
    a.page()
    a.mode('grid',1)
    a.t('game_start')
    a.t()
    a.b('开始',a.goto, game_init)

def game_init():
    save = a.sav()

    save['日期'] = {
        '年':1, '季':1,
        '旬':1, '周':1,
        '总日数':1
    }
    save['character_list'] = {
        "character_number":0,
        '学生':{}
    }

    save['资源'] = {
        '金钱':5000,  '精液':0,
        '魅魔水滴':0, '生质':0,
    }

    save['achievement'] = {
        "achievement_point":0,
    }
    save['物品'] = {}
    save['tech'] = {}

    a.sav()['学院名'] = '测试学院名'

    a.sav()['校内建筑列表']=[]
    a.sav()['校区建筑最大空间'] = 5
    a.sav()['维护总费用'] = {}
    a.sav()['可建设建筑列表'] = ['测试']
    a.sav()['每周最大行动次数'] = 4
    event1()
    a.goto(creat_leading_character)
