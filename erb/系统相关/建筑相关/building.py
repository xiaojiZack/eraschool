import erajs.api as a
from .building3_宿舍楼 import exec3,destory3, structure3
from .building2_影视厅 import exec2,destory2,structure2
from .building0_测试 import exec0,destory0

def exec_building():
    exec_func = {0:exec0, 2:exec2, 3:exec3}
    building_dict = a.dat()['building_item']
    bl = a.sav()['校内建筑列表']
    for b in bl:
        bname = b['名称']
        if (building_dict[bname]['可执行']):
            if building_dict[bname]['执行函数'] in exec_func.keys():
                exec_func[building_dict[bname]['执行函数']](b)
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

def destory_building(building):
    #执行建筑拆除函数
    destory_func = {0:destory0,3:destory3}
    building_dict = a.dat()['building_item']
    bname = building['名称']
    if building_dict[bname]['执行函数'] in destory_func.keys():
        return destory_func[building_dict[bname]['执行函数']](building)
    else:
        return True

def structure_building(building):
    structure_func = {3:structure3}
    building_dict = a.dat()['building_item']
    bname = building['名称']
    if building_dict[bname]['执行函数'] in structure_func.keys():
        return structure_func[building_dict[bname]['执行函数']](building)
    else:
        return True