import copy
import time
import erajs.api as a
import math
from erb.系统相关.人物相关.character_class import search_quaility as sq
from erb.系统相关.调教相关.memory_cal import exp_cal, memory_cal
from erb.系统相关.调教相关.液体 import eject_liquid, inject_liquid

def check_orgasm(c):
    orgasm_level = ['绝顶','强绝顶','超强绝顶','超超强绝顶','超超超强绝顶','升天']
    eject_level = ['']
    orgasm_part = []
    d = {}
    orgasm_edge = 10000
    for i in ['V','A','M','B','C','W','U']:
        if c['调教记忆']['快{}'.format(i)] >=orgasm_edge:
            orgasm_part.append(i)
    for i in ['V','A','M','B','C','W','U']:
        count = 0
        count = int(c['调教记忆']['快{}'.format(i)]/orgasm_edge)
        if count >0:
            d[i] = count
    if c['其他参数']['射精数值']>c['身体信息']['阴茎']['忍耐极限']:
        count = c['其他参数']['射精数值']/c['身体信息']['阴茎']['忍耐极限']
        c['其他参数']['射精数值'] = 0
        d['射精'] = count
    if len(d)>0:
        a.tmp()['高潮名单'][c['CharacterId']] = d

    #所有角色高潮都通过高潮名单记录，方便后续进行bouns计算

#选择射精位置
def set_eject(c):
    def change_eject_place(p):
        if p == '':
            c['身体信息']['阴茎']['插入位置'] = {}
        else:
            who = c['身体信息']['阴茎']['插入位置'].keys()
            for i in who:
                c['身体信息']['阴茎']['插入位置'][i] = p
        eject_semen(c,a.tmp()['高潮名单'][c['CharacterId']]['射精'])
    if c['CharacterId'] == 0:
        a.divider()
        a.mode()
        a.h('你快要射了，这次要射在哪里?')
        a.t()
        a.b('就这样射精',eject_semen,c,a.tmp()['高潮名单'][c['CharacterId']]['射精'])
        a.t()
        a.b('纸巾上',change_eject_place,'')
        a.t()
    else:
        eject_semen(c)
    
def eject_semen(c,count):
    ae = {}
    times = count_level(count)
    ae['射精经验'] = 1
    for i in ae:
        if ae[i]>0:
            ae[i] = int(ae[i]*times)
        c['待处理经验'][i] += ae[i]
    eject_liquid_list = eject_liquid(c,'阴茎',count)
    if c['身体信息']['阴茎']['插入位置'] == {}:
        pass
    else:
        who = list(c['身体信息']['阴茎']['插入位置'].keys())
        who = who[0]    
        p = find_people(who)
        be_eject_semen(p,c['身体信息']['阴茎']['插入位置'][who],count_level(count),c['名字'])
        inject_liquid(p,c['身体信息']['阴茎']['插入位置'][who],eject_liquid_list)
    a.tmp()['射精处理中'] = False
#被射
def be_eject_semen(c,body_type,count,who_eject):
    l = {}
    e = {}
    if body_type == '阴道':
        l['欲情'] = 20
        l['恭顺'] = 20
        l['好感度'] = 2
        l['侍奉快乐'] = 1
        l['习得'] = 10
        l['反感'] = 50
        l['恐惧'] = 50
        l['屈服'] = 20
        l['快V'] = 10
        l['V润'] = 100
        e['腔射经验'] = 1
    if body_type == '子宫':
        l['欲情'] = 30
        l['恭顺'] = 30
        l['好感度'] = 1
        l['侍奉快乐'] = 1
        l['习得'] = 10
        l['反感'] = 100
        l['恐惧'] = 100
        l['屈服'] = 50
        l['快V'] = 10
        l['快W'] = 10
        l['V润'] = 100
        e['子宫被射经验'] = 1
    if body_type == '肛门':
        l['欲情'] = 10
        l['恭顺'] = 20
        l['好感度'] = 1
        l['侍奉快乐'] = 2
        l['习得'] = 20
        l['反感'] = 50
        l['恐惧'] = 50
        l['屈服'] = 50
        l['快A'] = 10
        l['A润'] = 100
        e['肛射经验'] = 1
    if body_type == '口':
        l['欲情'] = 30
        l['恭顺'] = 10
        l['好感度'] = 1
        l['侍奉快乐'] = 2
        l['习得'] = 30
        l['反感'] = 30
        l['恐惧'] = 20
        l['屈服'] = 80
        l['快M'] = 10
        e['饮精经验'] =1
    if body_type == '胸':
        l['欲情'] = 10
        l['恭顺'] = 10
        l['好感度'] = 1
        l['侍奉快乐'] = 2
        l['习得'] = 20
        l['反感'] = 20
        l['恐惧'] = 0
        l['屈服'] = 20
        l['快B'] = 5
    if body_type == '手':
        l['欲情'] = 5
        l['恭顺'] = 10
        l['好感度'] = 0
        l['侍奉快乐'] = 1
        l['习得'] = 20
        l['反感'] = 10
        l['恐惧'] = 0
        l['屈服'] = 5
        l['主导'] = 5
    if body_type == '脸':
        l['欲情'] = 10
        l['恭顺'] = 5
        l['好感度'] = 0
        l['侍奉快乐'] = 1
        l['习得'] = 0
        l['反感'] = 20
        l['恐惧'] = 10
        l['屈服'] = 5
    if body_type == '肚子':
        l['欲情'] = 10
        l['恭顺'] = 10
        l['好感度'] = 1
        l['侍奉快乐'] = 0
        l['习得'] = 0
        l['反感'] = 10
        l['恐惧'] = 10
        l['屈服'] = 5
    if body_type == '屁股':
        l['欲情'] = 5
        l['恭顺'] = 5
        l['好感度'] = 1
        l['侍奉快乐'] = 1
        l['习得'] = 0
        l['反感'] = 10
        l['恐惧'] = 0
        l['屈服'] = 5
    if body_type == '尿道':
        l['欲情'] = 10
        l['恭顺'] = 10
        l['好感度'] = 1
        l['侍奉快乐'] = 1
        l['习得'] = 10
        l['反感'] = 100
        l['恐惧'] = 100
        l['屈服'] = 30
        l['快U'] = 10
        e['尿道被射经验'] = 1
    if body_type == '乳内':
        l['欲情'] = 20
        l['恭顺'] = 20
        l['好感度'] = 1
        l['侍奉快乐'] = 1
        l['习得'] = 0
        l['反感'] = 100
        l['恐惧'] = 100
        l['屈服'] = 30
        l['快B'] = 10
        e['乳内被射经验'] = 1
    e['精液经验'] = 1
    
    for i in e:
        if e[i]>0:
            e[i] = int(e[i]*count)
        c['待处理经验'][i] += e[i]
    for i in l:
        if l[i]>0:
            l[i] = int(l[i]*count)
        c['待处理记忆'][i] += l[i]
    
    #淫纹反应空位
    #被射弱点反应空位

    if not c['CharacterId'] in a.tmp()['被射名单'].keys():
        a.tmp()['被射名单'][c['CharacterId']] = {body_type:[who_eject]}
    a.tmp()['被射名单'][c['CharacterId']][body_type].append(who_eject)

def orgasm_bouns():
    orgasm_level = ['绝顶','强绝顶','超强绝顶','极强绝顶','超超超强绝顶','最强绝顶']
    eject_semen_level = ['射精','大量射精','超大量射精','极大量射精','超超超大量射精','最强射精']
    ol = a.tmp()['高潮名单']
    text_list = []
    
    for i in ol:
        p = find_people(i)
        for j in ol[i]:
            if j == '射精':
                a.tmp()['射精处理中'] = True
                set_eject(p)
                while a.tmp()['射精处理中']:
                    time.sleep(0.1)
    
    #高潮记忆补正处理
    for i in ol:
        p = find_people(i)
        for j in ol[i]:
            if j in ['V','A','M','B','C','W','U']:
                p['调教记忆']['快{}'.format(j)] = p['调教记忆']['快{}'.format(j)] - 10000*ol[i][j]
                p['待处理记忆']['恭顺'] += 10
                p['待处理记忆']['欲情'] += 10
                p['待处理记忆']['V润'] += 50
                p['待处理记忆']['A润'] += 50
    
    #多重绝顶bouns
    for i in ol:
        p = find_people(i)
        temp_text = '{}:'.format(p['名字'])
        for j in ol[i]:
            if j in ['V','A','M','B','C','W','U']:
                temp_text = temp_text+'[{}{}]'.format(j,orgasm_level[count_level(ol[i][j])-1])
            if j == '射精':
                temp_text = temp_text+'[{}]'.format(eject_semen_level[count_level(ol[i][j])-1])
        number = len(ol[i])
        for j in p['待处理记忆']:
            p['待处理记忆'][j] = p['待处理记忆'][j]*number
        text_list.append(temp_text)

    #同时绝顶bouns
    number = len(ol.keys())
    if number >1:
        temp_text = '同时绝顶:'
        for i in ol:
            p = find_people(i)
            for j in p['待处理记忆']:
                p['待处理记忆'][j] = p['待处理记忆'][j]*number
            temp_text = temp_text+'[{}]'.format(p['名字'])
        text_list.append(temp_text)

    for i in text_list:
        a.t(i,style={'color':'#FFC1C1'})
        a.t()
    return text_list

def find_people(CharacterId):
    for i in a.tmp()['调教数据']['参与者']:
        if i['CharacterId'] == CharacterId:
            return i
    return False

def count_level(count):
    if count == 0:
        return False
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

#被射高潮处理
def chain_orgasm():
    trans_dict = {'V':'阴道','A':'肛门','M':'口','B':'乳房','W':'子宫'}
    orgasm_list = a.tmp()['高潮名单']
    for cid in orgasm_list:
        if cid in a.tmp()['被射名单']:
            if trans_dict[orgasm_list[cid]] in a.tmp()['被射名单'][cid].keys():
                a.t('{}的{}在'.format(find_people(cid)['名字'],trans_dict[orgasm_list[cid]]),style={'color':'#FFC1C1'})
                for i in a.tmp()['被射名单'][cid][trans_dict[orgasm_list[cid]]]:
                    a.t('[{}]'.format(i),style={'color':'#FFC1C1'})
                a.t('的射精冲击下达到了高潮',style={'color':'#FFC1C1'})
                a.t()
    orgasm_bouns()

#高潮处理主函数,输入参与者名单
def main_orgasm(cl):
    a.tmp()['被射名单'] = {}
    a.tmp()['高潮名单'] = {}
    for c in cl:
        check_orgasm(c)
    t = a.tmp()['高潮名单']
    orgasm_bouns()
    for c in cl:
        memory_cal(c)
        exp_cal(c)
    a.tmp()['高潮名单'] = {}
    for cid in a.tmp()['被射名单']:
        check_orgasm(find_people(cid))
    if len(a.tmp()['高潮名单']) >0:
        chain_orgasm()


