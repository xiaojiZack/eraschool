import erajs.api as a
from .building0_测试 import exec0
building_dict = {
    '测试':{
        '简介':'测试简介',
        '占用空间':1,
        '建筑费用':{'金钱':10},
        '维护费用':{'金钱':1},
        '可执行':True,
        '执行函数':0,
    },
}

def exec_building():
    bl = a.sav()['校内建筑列表']
    for i in bl:
        if (building_dict[i]['可执行']):
            exec('exec{}()'.format(building_dict[i]['执行函数']))
    cost = a.sav()['维护总费用']
    flag = True
    for i in cost:
        if a.sav()['资源'][i]<cost[i]:
            flag = False
            a.sav()['资源'][i] = 0
            a.msg('{}不足'.format(i))
        else:
            a.sav()['资源'][i] -= cost[i]
    a.tmp()['资源短缺flag'] = flag