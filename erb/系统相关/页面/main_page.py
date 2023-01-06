import erajs.api as a
from erb.系统相关.页面.research import check_free_tech, research_page
from erb.系统相关.页面.school_information import school_information
from funcs import debug
from .shop import shop_page
from .arrange_plan import init_plan
from .check_character import check_character
from .arrange_building import arrange_building
from ..事件.event import next_event

def main_page():
#主界面
    init_main_page()
#主页面显示
    a.cls()
    a.page()
    a.divider()
    a.mode('grid', 5)
    #日期
    a.b(a.sav()['学院名'], a.goto, school_information)
    a.t()
    season = ['春','夏','秋','冬']
    week = ['上','下']
    date = a.sav()['日期']
    a.t('{}年{}季{}第{}周'.format(
        date['年'],season[date['季']-1],
        week[date['旬']-1],date['周']))
    a.t()
    nt = next_event()
    a.t('[{}]将于{}周后举办'.format(nt[0],nt[1]))
    a.t()
    a.t('{}G'.format(a.sav()['资源']['金钱']))
    a.t()
    #jy
    a.t()
    #魅魔水滴
    a.t()
    #生质
    a.t()

    a.divider()
    a.mode('grid',2)
    lc = a.sav()['character_list']['主角']
    a.t(lc['名字'])
    a.t()
    if (lc['性别'] != '女性'):
            a.t('精液存量:')
            a.progress(lc['身体信息']['阴茎']['内容总量'],lc['身体信息']['阴茎']['容量'])
            #a.t('({}ml)'.format(lc['身体信息']['阴茎']['内容总量']))
            if lc['身体信息']['阴茎']['内容总量'] == lc['身体信息']['阴茎']['容量']:
                a.t('[满溢]', style=['color','#ff0'])
            a.t()

    a.divider()
    a.mode()
    a.t('维护费用:')
    for i in a.sav()['维护总费用']:
        a.t('[{}:{}]'.format(i,a.sav()['维护总费用'][i]))
    a.divider()
    a.t('持有物品:')
    for i in a.sav()['物品']:
        if a.sav()['物品'][i]>1:
            a.t('[{}]*{}'.format(i,a.sav()['物品'][i]))
        else:
            a.t('[{}]'.format(i))
    a.divider()
    a.mode('grid', 4)
    a.b('安排教学', init_plan)
    a.t()
    a.b('查看角色',a.goto,check_character)
    a.t()
    a.b('设施规划',a.goto,arrange_building)
    a.t()
    a.b('研发计划',a.goto,research_page)
    a.t()
    a.b('采购物品',a.goto,shop_page)
    a.t()
    #a.b('制定校规')

    a.divider()
    a.t('设置')
    a.t()
    a.b('存档', a.goto, a.ui_save)
    a.t()
    a.b('读档',a.goto, a.ui_load)
    a.t()
    a.cfg()['debug'] = True
    debug()


def init_main_page():
    #在载入主页面之前的一些工作
    check_free_tech()