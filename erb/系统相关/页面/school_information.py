import erajs.api as a

def school_information():
    a.page()
    a.mode()
    a.h(a.sav()['学院名'])
    a.divider()
    a.t('学院名气度:{}'.format(a.sav()['学院评级']))
    a.t()
    a.t('学生上限人数:{}人'.format(a.sav()['学生上限人数']))
    a.t()
    a.t('目前学生人数:{}人'.format(len(a.sav()['character_list']['学生'])))
    a.t()
    a.t('教职上限人数:{}人'.format(a.sav()['教职上限人数']))
    a.t()
    a.t('历史毕业人数:{}人'.format(a.sav()['历史毕业人数']))
    a.t()

    a.divider()
    a.b('返回',a.back)