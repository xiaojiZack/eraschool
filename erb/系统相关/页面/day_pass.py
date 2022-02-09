import erajs.api as a
from erb.系统相关.人物相关.character_class import search_quaility
from ..建筑相关.building import exec_building
from ..事件.daily_event import daily_event
from ..system_time import date_count
from ..事件.event import event_check

def day_pass():
    character_recover()
    tech_research()
    a.divider('建筑事件')
    exec_building()
    a.t('',True)
    a.divider('日常事件')
    a.t('',True)
    daily_event()
    a.divider('大型事件')
    a.t('',True)
    date_count()
    event_check()
    a.t('',True)
    a.back(2)

def character_recover():
    cl = a.sav()['character_list']
    l = cl['学生']
    for j in l:
        i = l[j]
        recover_rate = [0.5,0.35,0.2]
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
        i['体力值'] += int(i['体力值'] * recover_rate[0])
        if i['体力值']>i['最大体力值']:i['体力值'] = i['最大体力值']
        i['气力值'] += int(i['气力值'] * recover_rate[1])
        if i['气力值']>i['最大气力值']:i['气力值'] = i['最大气力值']
        i['理智值'] += int(i['理智值'] * recover_rate[2])
        if i['理智值']>i['最大理智值']:i['理智值'] = i['最大理智值']
        liquid_produce(i)
    lr = cl['主角']
    lr['体力值'] = lr['最大体力值']
    lr['气力值'] = lr['最大气力值']
    lr['理智值'] = lr['最大理智值']
    liquid_produce(lr)
           
def liquid_produce(c):
    b = c['身体信息']
    if c['性别'] != '女性':
        plimit = b['阴茎']['容量']
        pliquid = b['阴茎']['内容液体']
        pin = b['阴茎']['内容总量']
        pproduce = b['阴茎']['生产速度']
        if '精液' in pliquid:
            pliquid['精液']+= pproduce
        else:
            pliquid['精液'] = pproduce
        pin +=  pproduce
        if pin >plimit:
            #过满，则浓缩精液
            pliquid['精液'] -= pin-plimit
            pin = plimit
            b['阴茎']['积攒计数器'] += 1
        if b['阴茎']['积攒计数器'] == 2:
            pliquid['浓厚精液'] = pliquid['精液']
            pliquid['精液'] = 0
        elif b['阴茎']['积攒计数器'] > 2:
            #遗精事件，待做
            pass
        elif b['阴茎']['积攒计数器'] == 4:
            pliquid['凝块精液'] = pliquid['浓厚精液']
            pliquid['浓厚精液'] = 0
        b['阴茎']['内容总量'] = pin
        b['阴茎']['内容液体'] = pliquid

    if c['性别'] != '男性':
        plimit = b['乳房']['容量']
        pliquid = b['乳房']['内容液体']
        pin = b['乳房']['内容总量']
        pproduce = b['乳房']['生产速度']
        if '母乳' in pliquid:
            pliquid['母乳']+= pproduce
        else:
            pliquid['母乳'] = pproduce
        pin +=  pproduce
        if pin >plimit:
            #过满，则浓缩母乳
            pliquid['母乳'] -= pin-plimit
            pin = plimit
            b['乳房']['积攒计数器'] += 1
        if b['乳房']['积攒计数器'] == 2:
            pliquid['浓厚母乳'] = pliquid['母乳']
            pliquid['母乳'] = 0
        elif b['乳房']['积攒计数器'] > 2:
            #漏乳事件，待做
            pass
        elif b['乳房']['积攒计数器'] == 4:
            pliquid['粘稠母乳'] = pliquid['浓厚母乳']
            pliquid['浓厚母乳'] = 0
            
def tech_research():
    l = a.sav()['正在研发']
    for i in l:
        l[i] -= 1
        if l[i] == 0:
            a.msg('[{}]研发完成'.format(i))
            a.tech.append('{}'.format(i))


