import imp
import erajs.api as a
from ..建筑相关.building import building_dict

def arrange_building():
    a.page()
    a.mode()
    a.divider('校内设施一览')
    bl = a.sav()['校内建筑列表']
    limit = a.sav()['校区建筑最大空间']
    temp = limit
    for i in bl:
        a.b('[{}]'.format(i),existing_building,i)
        temp -= building_dict[i]['占用空间']
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
    def check_fee(b):
        fee = a.sav()['资源']
        cost = b['建筑费用']
        space = b['占用空间']
        remain_space = a.tmp()['剩余空间']
        for i in cost:
            if fee[i]<cost[i]:
                a.msg('{}不足'.format(i))
                return False
        if space >= remain_space:
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
            a.sav()['校内建筑列表'].append(bname)
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
    a.b('放弃',a.back)

def existing_building(bname):
    def destory(bname):
        a.sav()['校内建筑列表'].remove(bname)
        space = building_dict[bname]['占用空间']
        remain_space = a.tmp()['剩余空间']
        remain_space += space
        update_building_cost()
        a.msg('[{}]已经拆除'.format(bname))
        a.repeat()
    a.page()
    a.mode()
    a.h(bname)
    a.t('简介:{}'.format(building_dict[bname]['简介']))
    a.t()
    a.t('占用空间:{}'.format(building_dict[bname]['占用空间']))
    a.t()
    a.t('建筑费用:')
    for i in building_dict[bname]['建筑费用']:
        a.t('[{}:{}]'.format(i,building_dict[bname]['建筑费用'][i]))
    a.t()
    a.t('维护费用:')
    for i in building_dict[bname]['维护费用']:
        a.t('[{}:{}]'.format(i,building_dict[bname]['维护费用'][i]))
    a.divider()
    a.b('拆除建筑',destory,bname)
    a.t()
    a.b('放弃',a.back)

def update_building_cost():
    bl = a.sav()['校内建筑列表']
    cost = {}
    for i in bl:
        for j in building_dict[i]['维护费用']:
            if not (j in cost.keys()):
                cost[j] = building_dict[i]['维护费用'][j]
            else:
                cost[j] += building_dict[i]['维护费用'][j]
    a.sav()['维护总费用'] = cost