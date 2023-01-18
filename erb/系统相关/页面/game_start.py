from  erajs import api as a
from erb.系统相关.页面.main_page import main_page
import funcs as f
from .creat_leading_character import creat_leading_character
from erb.系统相关.事件.event_1_入学 import *
def game_start():
    a.cls()
    a.page()
    a.mode('grid',1)
    a.h('ERAfacility')
    a.t()
    a.t('0.1')
    a.divider()
    a.img('image.titile',inline=False, style={'width':'100px','height':'100px'})
    a.mode('grid',1)
    a.t("本游戏尚在开发中，许多功能尚未实装，尽情期待！")
    a.t()
    a.t("目前框架尚不稳定，有各种bug和版本更新导致的坏档风险。")
    a.divider()
    a.b('开始',a.goto, game_init)
    a.t()
    a.b('继续',a.goto, load_save)

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
    save['科技'] = []
    save['正在研发'] = {}

    a.sav()['学院名'] = '肉便器学院'
    a.sav()['学院评级'] = 'D'
    a.sav()['学院名气度'] = 0
    a.sav()['可用教案'] = ['自由活动','单独授课',]
    a.sav()['校内建筑列表']=[]
    a.sav()['校区建筑最大空间'] = 5
    a.sav()['维护总费用'] = {}
    a.sav()['可建设建筑列表'] = ['测试']
    a.sav()['每周最大行动次数'] = 1
    a.sav()['学生上限人数'] = 2
    a.sav()['教职上限人数'] = 1
    a.sav()['历史毕业人数'] = 0

    a.sav()['调教中'] = False

    def input_school_name(name):
            a.sav()['学院名'] = name
    a.page()
    a.t('学院名为:')
    a.input(input_school_name,'肉便器学院')
    a.t()
    a.b('[决定]',creat_leading_character,style = {'color':'#ff0'})

def load_save():
    a.page()
    def load_file(i, filename_without_ext):
        a.load(filename_without_ext)
        a.clear()
        a.goto(main_page)
    a.mode()
    for i, each in enumerate(a.scan_save_file()):
        a.b('{}. {}'.format(i, each[0]), load_file, i, each[0])
        a.t()
    a.divider()
    a.b('返回',a.back)