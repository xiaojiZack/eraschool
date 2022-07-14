import erajs.api as a
from erb.系统相关.事件.event_1_入学 import event1
from erb.系统相关.页面.main_page import main_page

def event0():
    def opening():
        a.cls()
        a.page()
        a.mode()
        time = a.sav()['日期']
        season = ['春','夏','秋','冬']
        week = ['上','下']
        a.h('《惊天怪谈！神秘学园现身！》'.format(season[time['季']],week[time['旬']],time['周']),style={'font-style':'italic'})
        a.t('',True)
        a.t('时值樱春，在这各地学院陆续招募新生的时节，一座全新而神秘的学园也将落成。',True)
        a.t('\"为了应对当今持续低迷的生育现状，这所学院便是为此存在的\"谜一般的学园长的声音在磁带中如此说道。',True)
        a.t('除了这盘突然出现在本社办公室包裹里的磁带之外，我们仅能得知这所名为[{}]的学园似乎由多股神秘势力支持'.format(a.sav()['学院名']),True)
        a.t('另外据传，整所学园只有一名受聘教师，而这所学院将实行怎么样的教学方针，电话地址、招生方式及包括学园长本人在内的工作人员信息皆隐于迷雾之中。',True)
        a.t('呼呼呼，如此都市传说般的怪谈已在各个论坛引起激烈讨论，而本社也将继续跟进调查。')
        a.t()
        a.t('(胡言乱语报)',True)
        a.t()
        event1()
        a.clear()
        a.goto(main_page)
    def passopening():
        event1()
        a.clear()
        a.goto(main_page)

    a.cls()
    a.page()
    a.t('要观看开幕吗？')
    a.t()
    a.b('是',opening)
    a.t()
    a.b('否',passopening)