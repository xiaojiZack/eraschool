from  ....erajs import api as a
from .... import funcs as f
from ...人物相关.character_creat import creat_leading_character
import main_page

def game_start():
     
    a.page()
    a.mode('grid')
    a.t('game_start')
    a.t()
    a.b('开始',a.goto, game_init)

def game_init():
    save = a.sav()
    save = {}

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
        '金钱':5000,  'jy':0,
        '魅魔水滴':0, '生质':0,
    }

    save['achievement'] = {
        "achievement_point":0,
    }
    save['item'] = {}
    save['building'] = {}
    save['tech'] = {}

    a.goto(creat_leading_character)
