import erajs.api as a
import math

def count_level(count):
    if count == 1:
        return 1
    elif count >1 and count <=5:
        return 2
    elif count >5 and count <=10:
        return 3
    elif count >10 and count <= 20:
        return 4
    elif count >20 and count <= 40:
        return 5
    else:
        return 6

#射出液体计算，返回射液列表,body_type = '阴茎’、‘乳房’
def eject_liquid(c,body_type,count):
    times = count_level(count)
    eject_liquid_list = {}
    for j in range(0,times):
        eject_rate = c['身体信息'][body_type]['标准射出量']
        liquid_list = c['身体信息'][body_type]['内容液体']
        liquid_sum = c['身体信息'][body_type]['内容总量']
        for i in liquid_list:
            temp = math.ceil((liquid_list[i]*1.0/liquid_sum)*eject_rate)
            if not i in eject_liquid_list.keys():
                eject_liquid_list[i] = temp
            else:
                eject_liquid_list[i] += temp
            liquid_list[i] -= temp
            liquid_sum -= temp
        c['身体信息'][body_type]['内容液体'] = liquid_list
        c['身体信息'][body_type]['内容总量'] = liquid_sum
    return eject_liquid_list

#注入液体
def inject_liquid(c,body_type,eject_liquid_list):
    def add_dict(d,key,value):
        if key in d.keys():
            d[key] += value
        else:
            d[key] = value
    if body_type == '阴道':
        body_type = '子宫'
    liquid_list = c['身体信息'][body_type]['内容液体']
    liquid_sum = c['身体信息'][body_type]['内容总量']
    liquid_limit = c['身体信息'][body_type]['容量']
    for i in eject_liquid_list:
        eject_liquid_list[i] = math.ceil(eject_liquid_list[i]*inject_leak(c,body_type))
        add_dict(liquid_list,i,eject_liquid_list[i])
        liquid_sum += eject_liquid_list[i]
    if liquid_sum>liquid_limit:
        overinject(c,body_type)
    c['身体信息'][body_type]['内容总量'] = liquid_sum
    c['身体信息'][body_type]['内容液体'] = liquid_list

#过度注入
def overinject(c,body_type):
    pass

#泄露
def leak(c,body_type):
    pass

#药液吸收
def absorb(c,body_type):
    pass

#注入泄露系数
def inject_leak(c,body_type):
    if body_type == '阴道':
        return 0.25
    elif body_type == '子宫':
        return 0.8
    elif body_type == '肛门':
        return 0.8
    elif body_type == '口':
        return 0.75
    elif body_type == '尿道':
        return 0.5