import erajs.api as a
from ..建筑相关.building import destory_building, setting_building, structure_building

def arrange_building():
    #建筑管理主页面

    #更新可建筑页面
    update_allowed_building()
    building_dict = a.dat()['building_item']

    a.cls()
    a.page()
    a.mode()
    a.divider('校内设施一览')
    bl = a.sav()['校内建筑列表']
    limit = a.sav()['校区建筑最大空间']
    temp = limit
    for i in bl:
        a.b('[{}]'.format(i['名称']),a.goto,existing_building,i)
        temp -= i['占用空间']
    a.t()

    a.divider('维护费用')
    cost = a.sav()['维护总费用']
    for i in cost:
        a.t('{}:'.format(i))
        a.t(cost[i])
        a.t()
    
    a.divider('可用建筑')
    a.t('剩余建筑空间:{}'.format(temp))
    a.tmp()['剩余空间'] = temp
    a.divider()
    a.mode('grid',4)
    cbl = a.sav()['可建设建筑列表']
    for i in cbl:
        a.b('[{}]'.format(i),add_building_page,i)
        a.t()
    for i in range(0, 4-len(cbl)%4):
        a.t()

    a.divider()
    a.b('返回',a.back)

def add_building_page(bname):
    #新增建筑页面
    building_dict = a.dat()['building_item']
    def check_fee(b):
        fee = a.sav()['资源']
        cost = b['建筑费用']
        space = b['占用空间']
        remain_space = a.tmp()['剩余空间']
        for i in cost:
            if fee[i]<cost[i]:
                a.msg('{}不足'.format(i))
                return False
        if space > remain_space:
            a.msg('校区空间不足')
            return False
        return True
    
    def add_building(bname):
        if check_fee(building_dict[bname]):
            fee = a.sav()['资源']
            cost = building_dict[bname]['建筑费用']
            for i in cost:
                fee[i]-=cost[i]
            space = building_dict[bname]['占用空间']
            remain_space = a.tmp()['剩余空间']
            remain_space -= space
            new_building = building_dict[bname].copy()
            new_building['名称'] = bname
            a.sav()['校内建筑列表'].append(new_building)
            structure_building(new_building)
            update_building_cost()
            a.msg('[{}]新建成功'.format(bname))
            a.repeat()

    a.page()
    a.mode()
    a.h(bname)
    a.t()
    a.t('简介:{}'.format(building_dict[bname]['简介']))
    a.t()
    a.t('占用空间:{}'.format(building_dict[bname]['占用空间']))
    a.t()
    a.t('最多所有数:{}'.format(building_dict[bname]['最多所有数']))
    a.t()
    a.t('建筑费用:')
    for i in building_dict[bname]['建筑费用']:
        a.t('[{}:{}]'.format(i,building_dict[bname]['建筑费用'][i]))
    a.t()
    a.t('维护费用:')
    for i in building_dict[bname]['维护费用']:
        a.t('[{}:{}]'.format(i,building_dict[bname]['维护费用'][i]))
    a.divider()
    a.b('新建建筑',add_building, bname)
    a.t()
    a.b('放弃',a.repeat)

def existing_building(building):
    building_dict = a.dat()['building_item']
    bname = building['名称']
    def destory(building):
        if destory_building(building):
            a.sav()['校内建筑列表'].remove(building)
            space = building_dict[bname]['占用空间']
            remain_space = a.tmp()['剩余空间']
            remain_space += space
            update_building_cost()
            a.msg('[{}]已经拆除'.format(bname))
            a.back()
        else:
            a.msg('取消[{}]拆除'.format(bname))
            a.repeat()
    a.page()
    a.mode()
    a.h(bname)
    a.t()
    a.t('简介:{}'.format(building['简介']))
    a.t()
    a.t('占用空间:{}'.format(building['占用空间']))
    a.t()
    a.t('建筑费用:')
    for i in building['建筑费用']:
        a.t('[{}:{}]'.format(i,building['建筑费用'][i]))
    a.t()
    a.t('维护费用:')
    for i in building['维护费用']:
        a.t('[{}:{}]'.format(i,building['维护费用'][i]))
    a.divider()
    if building['可设置']:
        a.b('进入{}'.format(building['名称']), setting_building, building)
        a.t()
    a.b('拆除建筑',destory,building, style={'color': '#f00'})
    a.t()
    a.b('返回',a.back)

def update_building_cost():
    bl = a.sav()['校内建筑列表']
    cost = {}
    for i in bl:
        for j in i['维护费用']:
            if not (j in cost.keys()):
                cost[j] = i['维护费用'][j]
            else:
                cost[j] += i['维护费用'][j]
    a.sav()['维护总费用'] = cost

def update_allowed_building():
    #更新可建筑列表
    def check_allow(bname):
        #检查是否符合前置需求
        f = True
        tech = a.dat()['building_item'][bname]['科技需求']
        t = a.sav()['科技']
        for i in tech:
            if i=='无': f = True
            elif not i in a.sav()['科技']: 
                f= False
        bl = a.sav()['校内建筑列表']
        count = 0
        for i in bl:
            if i['名称'] == bname:
                count = count +1
        if count >= a.dat()['building_item'][bname]['最多所有数']: 
            f = False
        return f
    
    cbl = a.sav()['可建设建筑列表']
    building_dict = a.dat()['building_item']
    for i in building_dict:
        if i in cbl:
            if not check_allow(i):
                cbl.remove(i)
                #已不再满足前置需求
        else:
            if check_allow(i):
                cbl.append(i)
                #新增建筑项
