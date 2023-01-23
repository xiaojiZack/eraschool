import erajs.api as a
from erb.系统相关.建筑相关.building20_咖啡厅 import exec20, setting20
from erb.系统相关.建筑相关.building4_操场 import exec4
from .building10_食堂 import exec10
from .building9_游泳池 import exec9
from .building3_宿舍楼 import exec3,destory3, structure3
from .building2_影视厅 import exec2,destory2,structure2
from .building0_测试 import exec0,destory0
from .building7_动物小屋 import exec7
from .building21_图书馆 import exec21
def exec_building():
    exec_func = {0:exec0, 2:exec2, 3:exec3, 4:exec4, 7:exec7, 9:exec9, 10:exec10, 20:exec20, 21:exec21}
    building_dict = a.dat()['building_item']
    bl = a.sav()['校内建筑列表']
    for b in bl:
        bname = b['名称']
        if (building_dict[bname]['可执行']):
            if building_dict[bname]['执行函数'] in exec_func.keys():
                exec_func[building_dict[bname]['执行函数']](b)
    cost = a.sav()['维护总费用']
    flag = False
    for i in cost:
        if a.sav()['资源'][i]<cost[i]:
            flag = True
            a.sav()['资源'][i] = 0
            a.msg('{}不足'.format(i), style={'color':'#f00'})
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

def setting_building(building):
    setting_func = {20:setting20}
    a.goto(setting_func[building['执行函数']],building)