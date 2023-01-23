import math
import erajs.api as a
from erb.系统相关.人物相关.character_class import search_quaility
from erb.系统相关.调教相关.药液.药液 import drain_drugs
from ..建筑相关.building import exec_building
from ..事件.daily_event import daily_event
from ..system_time import date_count
from ..事件.event import event_check

def day_pass():
    character_recover()
    tech_research()
    a.divider('建筑事件',style={'color':'#f00','size':20})
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
    a.save('自动存档')
    a.back(2)

def character_recover():
    #回复角色体力、气力，仅有空闲状态才可回复
    cl = a.sav()['character_list']
    l = cl['学生']
    for j in l:
        i = l[j]
        if not i['工作状态'] == '空闲':
            continue
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
        i['体力值'] += int(i['最大体力值'] * recover_rate[0])
        if i['体力值']>i['最大体力值']:i['体力值'] = i['最大体力值']
        i['气力值'] += int(i['最大气力值'] * recover_rate[1])
        if i['气力值']>i['最大气力值']:i['气力值'] = i['最大气力值']
        i['理智值'] += int(i['最大理智值'] * recover_rate[2])
        if i['理智值']>i['最大理智值']:i['理智值'] = i['最大理智值']
        #液体流失
        drain_drugs(i)
        #体液回复
        character_liquid_produce(i)
        #催眠回复，随时间流逝催眠接触
        if i['催眠']>0:
            i['催眠'] -= max(1,math.ceil(0.5*i['催眠']*i['理智值']/i['最大理智值']))
        
        
    
    lr = cl['主角']
    lr['体力值'] = lr['最大体力值']
    lr['气力值'] = lr['最大气力值']
    lr['理智值'] = lr['最大理智值']
    character_liquid_produce(lr)
    
           
def character_liquid_produce(c):
    #角色回复体液存量
    def sign_semen(c,semen_type):
        #精液署名，返回名字
        return  semen_type+'_{}'.format(c['CharacterId'])
    
    b = c['身体信息']
    if c['性别'] != '女性':
        semen1 = sign_semen(c,'精液')
        semen2 = sign_semen(c,'浓厚精液')
        semen3 = sign_semen(c,'凝块精液')
        plimit = b['阴茎']['容量']
        pliquid = b['阴茎']['内容液体']
        pin = b['阴茎']['内容总量']
        pproduce = b['阴茎']['生产速度']
        if semen1 in pliquid:
            pliquid[semen1]+= pproduce
        else:
            pliquid[semen1] = pproduce
        pin +=  pproduce
        if pin >plimit:
            #过满，则浓缩精液
            pliquid[semen1] -= pin-plimit
            pin = plimit
            b['阴茎']['积攒计数器'] += 1
        if b['阴茎']['积攒计数器'] == 2:
            pliquid[semen2] = pliquid[semen1]
            pliquid[semen1] = 0
        elif b['阴茎']['积攒计数器'] > 2:
            #遗精事件，待做
            #TODO
            pass
        elif b['阴茎']['积攒计数器'] == 4:
            pliquid[semen3] = pliquid[semen2]
            pliquid[semen2] = 0
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
            #TODO
            pass
        elif b['乳房']['积攒计数器'] == 4:
            pliquid['粘稠母乳'] = pliquid['浓厚母乳']
            pliquid['浓厚母乳'] = 0
            
def tech_research():
    #研发科技推进
    l = a.sav()['正在研发']
    finish = []
    for i in l:
        l[i] -= 1
        if l[i] == 0:
            a.msg('[{}]研发完成'.format(i), style={'color':'#ff0'})
            a.sav()['科技'].append('{}'.format(i))
            finish.append(i)
            #课程类科技加入课程选单
            if '课程:' in i:
                    temp = i.replace('课程:','')
                    a.sav()['可用教案'].append(temp)
    for i in finish:
        del a.sav()['正在研发'][i]
