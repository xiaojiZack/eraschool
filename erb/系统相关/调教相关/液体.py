import random
import erajs.api as a
import math

from erb.系统相关.调教相关.药液.药液 import update_drug

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
        save_body_type = '子宫'
    elif body_type == '肛门':
        save_body_type = '肠道'
    else:
        save_body_type = body_type
    liquid_list = c['身体信息'][save_body_type]['内容液体']
    liquid_sum = c['身体信息'][save_body_type]['内容总量']
    liquid_limit = c['身体信息'][save_body_type]['容量']
    for i in eject_liquid_list:
        eject_liquid_list[i] = math.ceil(eject_liquid_list[i]*inject_leak(c,body_type))
        add_dict(liquid_list,i,eject_liquid_list[i])
        liquid_sum += eject_liquid_list[i]
    if liquid_sum>liquid_limit:
        overinject(c,save_body_type)
    c['身体信息'][save_body_type]['内容总量'] = liquid_sum
    c['身体信息'][save_body_type]['内容液体'] = liquid_list
    liquid_updata(c,save_body_type)

#过度注入
#考虑是溢出多余液体还是暂时扩张容量
#溢出液体应当去除较旧的液体
def overinject(c,body_type):
    max_volum = c['身体信息'][body_type]['容量']
    now_volum = c['身体信息'][body_type]['内容总量']
    liquid_list = c['身体信息'][body_type]['内容液体']
    new_volume = 0
    for d in liquid_list:
        liquid_list[d] = math.ceil(liquid_list[d]*now_volum/max_volum)
        new_volume += liquid_list[d]

    #大部分去除后仍超过最大容量
    while new_volume>max_volum:
        random_liquid = random.choice(liquid_list.keys())
        liquid_list[random_liquid] -= min(new_volume - max_volum, liquid_list[random_liquid])
    
    for d in liquid_list:
        new_volume += liquid_list[d]
        if liquid_list[d] <=0:
            liquid_list.pop(d)
    now_volum = new_volume

#泄露
#详见药液文件
def leak(c,body_type):
    pass

#药液吸收
#详见药液文件
def liquid_updata(c,body_type):
    update_drug(c)
    liquid_list = c['身体信息'][body_type]['内容液体']
    new_volume = 0
    for d in liquid_list:
        new_volume += liquid_list[d]
        if liquid_list[d] <=0:
            liquid_list.pop(d)
    c['身体信息'][body_type]['内容总量'] = new_volume

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