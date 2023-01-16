import random
import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal

def structure10():
    return True

def exec10():
    #食堂效果，加快回复
    a.t('食堂帮助体力的回复')
    a.t()
    character_recover()

def destory10():
    return True

def character_recover():
    #回复角色体力、气力
    cl = a.sav()['character_list']
    l = cl['学生']
    for j in l:
        i = l[j]
        recover_rate = [0.3,0.1,0.1]
        if search_quaility(i,'快速回复'):
            recover_rate[0] = 0.75
            recover_rate[1] = 0.5
        elif search_quaility(i,'病弱'):
            recover_rate[0] = 0.25
            recover_rate[1] = 0.2
        if search_quaility(i,'忧郁'):
            recover_rate[2] = 0.15
        if search_quaility(i,'悲观'):
            recover_rate[2] = 0.1
        if search_quaility(i,'刚强'):
            recover_rate[2] = 0.25
        if search_quaility(i,'乐观'):
            recover_rate[2] = 0.3
        i['体力值'] += int(i['最大体力值'] * recover_rate[0])
        if i['体力值']>i['最大体力值']:i['体力值'] = i['最大体力值']
        i['气力值'] += int(i['最大气力值'] * recover_rate[1])
        if i['气力值']>i['最大气力值']:i['气力值'] = i['最大气力值']
        i['理智值'] += int(i['最大理智值'] * recover_rate[2])
        if i['理智值']>i['最大理智值']:i['理智值'] = i['最大理智值']
        
        
def search_quaility(c,target):
    for i in c['属性']:
        for j in c['属性'][i]:
            if j == target:
                return True
    return False