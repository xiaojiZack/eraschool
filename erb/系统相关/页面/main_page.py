import erajs.api as a
def main_page():
#主页面显示
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
    a.mode('grid',2)
    lc = a.sav()['character_list']['主角']
    a.t(lc['基本信息']['名字'])
    a.t()
    a.t('体力:')
    a.progress(lc['基本信息']['体力值'],lc['基本信息']['最大体力值'], [{'width': '200px'}, {}])
    a.t('({}/{}'.format(lc['基本信息']['体力值'],lc['基本信息']['最大体力值']))
    a.t()
    a.t('气力:')
    a.progress(lc['基本信息']['气力值'],lc['基本信息']['最大气力值'], [{'width': '200px'}, {}])
    a.t('({}/{}'.format(lc['基本信息']['气力值'],lc['基本信息']['最大气力值']))
    a.t()

    a.divider()
    a.mode('grid', 4)
    a.b('安排教学')
    a.t()
    a.b('查看角色')
    a.t()
    a.b('校区规划')
    a.t()
    a.t('研发计划')
    a.t()
    a.t('采购物品')
    a.t()
    a.t('制定校规')

    a.divider()
    a.t('设置')
    a.t()
    a.t('存档')
    a.t()
    a.t('读档')

