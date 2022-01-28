import erajs.api as a

def init_plan():
    a.sav()['剩余规划时间'] = a.sav()['每周最大行动次数']
    a.tmp()['计划'] = []
    a.tmp()['选择计划位置'] = -1
    for i in range(0,a.sav()['每周最大行动次数']):
        a.tmp()['计划'].append('自由活动')
    arrange_plan()

def arrange_plan():
    def undo_plan(id):
        if a.tmp()['计划'][id] == '自由活动':
            a.tmp()['选择计划位置'] = id
        else:
            a.msg('{}已从计划中取消'.format(a.tmp()['计划'][id].pop(id)))
            a.tmp()['计划'][id] = '自由活动'
            a.sav()['剩余规划时间'] += 1
            a.repeat()
    def add_plan(name):
        if a.tmp()['选择计划位置'] == -1:
            a.msg('请先选择时间')
        else:
            a.tmp()['计划'][a.tmp()['选择计划位置']] = name
            a.tmp()['选择计划位置'] = -1
            a.sav()['剩余规划时间'] -= 1
    a.page()
    a.divider()
    a.mode('grid', 5)
    #日期
    season = ['春','夏','秋','冬']
    week = ['上','下']
    date = a.sav()['日期']
    a.t('{}年{}季{}第{}周'.format(
        date['年'],season[date['季']-1],
        week[date['旬']-1],date['周']))
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
    a.t('还可以添加{}项计划'.format(a.tmp()['剩余规划时间']))
    a.divider('计划')
    a.mode('grid',5)
    for i in range(0,len(a.tmp()['计划'])):
        a.b(a.tmp()['计划'][i],undo_plan, i)
        a.t()
    a.divider()
    #可用计划列表
    available_plan = a.sav()['可用教案']
    for i in available_plan:
        a.b(i,add_plan,i)
        a.t()
    
    a.divider()
    a.mode('grid',2)
    a.b('执行')
    a.t()
    a.b('返回',a.back)
