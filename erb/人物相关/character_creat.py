from pickle import TRUE
from tkinter import N

from scipy import rand

import erajs.api as a
from ..系统相关.页面.main_page import main_page
from ..人物相关.quaility_list import random_list
from ..人物相关.random_name import random_name
from erb.人物相关.character_class import new_character_dict
import random

def creat_leading_character():
    #创建主角
    def Basic():
        #口上设定部分未完成
        a.page()
        a.mode('line', 2)
        
        #基本信息
        def change_name(name):
            ec['名字'] = name
        a.t('名字')
        a.input(change_name, ec['名字'])
        a.t()

        def change_gender(gender):
            ec['性别'] = gender['value']
        a.t('性别')
        s = 1
        if ec['性别'] == '男性': s =1
        else: s =2
        a.dropdown(['男性','女性'], change_gender, s-1)
        a.t()

        a.t('点数:{}'.format(a.tmp()['talent_point']))
        a.t()
        a.mode('line',2)
        a.t('最大体力:')
        a.t(ec['最大体力值'])
        def decrease():
            ec['最大体力值'] -= 250
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['最大体力值'] += 250
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['最大体力值']>1500:
            a.b('-', decrease)
        if ec['最大体力值']<2500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        
        a.t('最大气力:')
        a.t(ec['最大气力值'])
        def decrease():
            ec['最大气力值'] -= 100
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['最大气力值'] += 100
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['最大气力值']>800:
            a.b('-', decrease)
        if ec['最大气力值']<1500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        ec['体力值'] = ec['最大体力值']
        ec['气力值'] = ec['最大气力值']
        
        a.b('下一步',a.goto, body, ec)

    def body(c):
        a.page()
        a.mode()
        a.b('返回', a.back)
        a.t()
        def length(i):
            if ('高大' in c['属性']['体质']):
                c['属性']['体质'].remove('高大')
            if ('小只' in c['属性']['体质']):
                c['属性']['体质'].remove('小只')
            if i['index'] == 0:
                pass
            else:
                c['属性']['体质'].append(i['value'])
        a.t('体型:')
        a.radio(['普通','高大','小只'], length, 0)
        a.t()

        def age(i): c['外表年龄'] = i['value']
        a.t('外表年龄:')
        a.radio(['儿童','少年','青年','大人'], age, 2)
        a.t()
        
        if (c['性别'] == '男性'):
            def dick_length(i):
                if ('小根' in c['属性']['体质']):
                    c['属性']['体质'].remove('小根')
                if ('巨根' in c['属性']['体质']):
                    c['属性']['体质'].remove('巨根')
                if ('普通根' in c['属性']['体质']):
                    c['属性']['体质'].remove('普通根')
                c['属性']['体质'].append(i['value'])
                c['身体信息']['阴茎']['尺寸'] = i['value']
            a.t('阴茎尺寸:')
            a.radio(['普通根','小根','巨根'], dick_length, 0)
            a.t()
            def endure(i):
                if ('早泄' in c['属性']['体质']):
                    c['属性']['体质'].remove('早泄')
                if ('迟泄' in c['属性']['体质']):
                    c['属性']['体质'].remove('迟泄')
                if i['index'] == 0:
                    pass
                else:
                    c['属性']['体质'].append(i['value'])
            a.t('忍耐程度')
            a.radio(['普通','早泄','迟泄'], endure, 0)
            a.t()
            def v_insert(i):
                l = [0, 5, 20]
                c['经验']['V插入经验'] = l[i['index']]
            a.t('V插入经验:')
            a.radio(['童贞','很少','很多'], v_insert, 0)
            a.t()
            def a_insert(i):
                l = [0, 5, 20]
                c['经验']['A插入经验'] = l[i['index']]
            a.t('A插入经验:')
            a.radio(['童贞','很少','很多'],a_insert,0)
            a.t()
            def A(i):
                l = [0, 5, 20]
                c['经验']['A经验'] = l[i['index']]
            a.t('A性交经验')
            a.radio(['无','很少','很多'], A, 0)
            a.t()
        if (c['性别'] == '女性'):
            def breast(i):
                if ('贫乳' in c['属性']['体质']):
                    c['属性']['体质'].remove('贫乳')
                if ('美乳' in c['属性']['体质']):
                    c['属性']['体质'].remove('美乳')
                if ('巨乳' in c['属性']['体质']):
                    c['属性']['体质'].remove('巨乳')
                c['属性']['体质'].append(i['value'])
            a.t('乳房尺寸:')
            a.radio(['贫乳','美乳','巨乳'], breast, 1)
            a.t()
            def V(i):
                l = [0, 5, 20]
                c['经验']['V经验'] = l[i['index']]
            a.t('V性交经验')
            a.radio(['处女','很少','很多'],V,0)
            a.t()
            def A(i):
                l = [0, 5, 20]
                c['经验']['A经验'] = l[i['index']]
            a.t('A性交经验')
            a.radio(['A处女','很少','很多'],A,0)
            a.t()
            def wet(i):
                if ('易湿' in c['属性']['体质']):
                    c['属性']['体质'].remove('易湿')
                if ('不易湿' in c['属性']['体质']):
                    c['属性']['体质'].remove('不易湿')
                c['属性']['体质'].append(i['value'])
            a.t('湿的程度')
            a.radio(['普通','易湿','不易湿'], wet, 0)
            a.t()
        
        def updata(c):
            if ((c['经验']['V经验'] != 0  or c['性别'] == '男性') and '处女'in c['属性']['体质']):
                c['属性']['体质'].remove('处女')
            elif((c['经验']['V经验'] == 0 and c['性别'] != '男性') and not('处女'in c['属性']['体质'])):
                c['属性']['体质'].append('处女')
            if (c['经验']['A经验'] != 0 and 'A处女'in c['属性']['体质']):
                c['属性']['体质'].remove('A处女')
            elif(c['经验']['A经验'] == 0 and not('A处女'in c['属性']['体质'])):
                c['属性']['体质'].append('A处女')
            if ((c['经验']['V插入经验'] != 0 or c['经验']['A插入经验'] != 0
                 or c['性别'] == '女性') and '童贞'in c['属性']['体质']):
                c['属性']['体质'].remove('童贞')
            elif((c['经验']['V插入经验'] == 0 and c['经验']['A插入经验'] == 0 
                 and c['性别'] != '女性') and not('童贞'in c['属性']['体质'])):
                c['属性']['体质'].append('童贞')
            body_type_creat(c)
            a.goto(talent_pick,c)

        a.b('下一步',updata,c)
    
    def talent_pick(c):
        def add(i):
            if (i != '扶持政策' and i != '快速回复'):
                c['属性']['技能'].append(i)
            elif(i == '扶持政策'):
                a.sav()['resource']['money'] += 20000
            elif(i == '快速回复'):
                c['属性']['体质'].append(i)
            a.goto(leading_character_show, c)
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider()
        a.t('选择特典')
        a.t()
        l = ['好为人师','爱抚知识','扩张知识','SM才能','快速回复','魅惑', '扶持政策']
        for i in l:
            a.b(i, add, i)
            a.t()
        a.divider()
        a.t('说明:')
        a.t('好为人师:在指导中略微提升所有在场者的经验获取，仅对低于自身的项目有效')
        a.t()
        a.t('爱抚知识:提升爱抚系调教、授课的效果')
        a.t()
        a.t('扩张知识:提高扩张系调教、授课的效果')
        a.t()
        a.t('SM才能:提高SM系调教、授课的效果')
        a.t()
        a.t('快速回复:提高每日体力气力的回复量')
        a.t()
        a.t('魅惑:使有关命令更容易执行')
        a.t()
        a.t('扶持政策:初始获得20,000启动资金')

    ec = new_character_dict()
    ec['最大体力值'] = 2000
    ec['最大气力值'] = 1200
    ec['体力值'] = ec['最大体力值']
    ec['气力值'] = ec['最大气力值']
    ec['种族'] = '人类'
    #talent_point = a.sav()['achievement']['achievement_point']+1
    talent_point = 10
    a.tmp()['talent_point'] = talent_point
    a.goto(Basic)
  
def body_type_creat(c):
    gender = c['性别']
    age = c['外表年龄']
    length = '普通'
    if ('高大' in c['属性']['体质']):
        length = '高大'
    if ('小只' in c['属性']['体质']):
        length = '小只'
    if ('小孩体型' in c['属性']['体质']):
        length = '小孩体型'
    if ('幼儿体型' in c['属性']['体质']):
        length = '幼儿体型'
    if (gender == '男性'): 
        l = random.randint(165,185)
        w = random.randint(55,70)
        if (age == '少年'):
            l -= 30
            w -= 10
        elif (age == '儿童'):
            l -= 70
            w -= 20
        if (length == '高大'):
            l += 20
            w += 10
        elif (length == '小只'):
            l -= 10
            w -= 10
        elif (length == '小孩体型'):
            l = random.randint(80,130)
            w = random.randint(30,40)
        elif (length == '幼儿体型'):
            l = random.randint(30,80)
            w = random.randint(15,30)
        c['身体信息']['具体身高'] = l
        c['身体信息']['具体体重'] = w    
    if (gender == '女性'):
        l = random.randint(155,170)
        w = random.randint(50,60)
        if (age == '少年'):
            l -= 30
            w -= 10
        elif (age == '儿童'):
            l -= 70
            w -= 20
        if (length == '高大'):
            l += 20
            w += 10
        elif (length == '小只'):
            l -= 20
            w -= 15
        elif (length == '小孩体型'):
            l = random.randint(70,110)
            w = random.randint(25,30)
        elif (length == '幼儿体型'):
            l = random.randint(30,70)
            w = random.randint(15,25)
        c['身体信息']['具体身高'] = l
        c['身体信息']['具体体重'] = w
    
    if (gender != '男性'):
        B = 80 
        H = 65
        W = 80
        s = 'C'
        if '贫乳' in c['属性']['体质']:
            B -= random.randint(8,12)
            l = ['A', 'B']
            s = l[random.randint(0,1)]
        if '巨乳' in c['属性']['体质']:
            B += random.randint(5,10)
            s = 'D'
        if '超乳' in c['属性']['体质']:
            B += random.randint(10,15)
            s = 'E'
        if '魔乳' in c['属性']['体质']:
            B += random.randint(15,20)
            s = 'f'
        c['身体信息']['三围']['B'] = str(B)+'cm'+'({}杯罩)'.format(s)
        if '小尻' in c['属性']['体质']:
            W -= random.randint(5,10)
        if '桃尻' in c['属性']['体质']:
            W += random.randint(5,10)
        if '巨尻' in c['属性']['体质']:
            W += random.randint(10,15)
        l = c['身体信息']['具体身高']
        ratio = float(l)/float(170)
        B = B*ratio
        H = H*ratio
        W = W*ratio
        c['身体信息']['三围']['B'] = str(int(B))+'cm'+'({}杯罩)'.format(s)
        c['身体信息']['三围']['H'] = str(int(H))+'cm'
        c['身体信息']['三围']['W'] = str(int(W))+'cm'
    
def leading_character_show(c):
    def addcharacter(c):
        a.sav()['character_list']['主角'] = c
        a.clear()
        a.goto(main_page)
    a.page()
    a.mode()
    a.divider('基本信息')
    a.mode('grid',4)
    a.t('姓名:')
    a.t(c['名字'])
    a.t()
    a.t('{}'.format(c['性别']))
    a.t()
    a.t(' 种族:{}'.format(c['种族']))
    a.t()
    a.t(' 外表年龄:{}'.format(c['外表年龄']))
    a.t()
    a.t('最大体力值:{}'.format(c['最大体力值']))
    a.t()
    a.t(' 最大气力值:{}'.format(c['最大气力值']))
    a.divider('身材尺寸')
    a.mode('grid', 5)
    body = c['身体信息']
    a.t('身高:{}cm'.format(body['具体身高']))
    a.t()
    a.t('体重:{}kg'.format(body['具体体重']))
    if c['性别'] == '女性':
        a.t()
        a.t('胸部:'+body['三围']['B'])
        a.t()
        a.t('腰部:'+body['三围']['H'])
        a.t()
        a.t('臀部:'+body['三围']['W'])
    a.divider('属性')
    a.mode('grid',1)
    q = c['属性']
    for i in q:
        if (len(q[i]) != 0):
            a.t('{}:'.format(i))
            for j in q[i]:
                a.t('[{}]'.format(j))
            a.t()
    a.divider('经验')
    q = c['经验']
    a.mode('grid', 6)
    for i in q:
        if q[i] != 0:
            a.t('{}:{}'.format(i, q[i]))
            a.t()
    a.mode()
    a.divider()
    a.b('决定', addcharacter, c)
        

def creat_normal_character(character):
    c = character
    #随机属性
    for i in c['属性']:
        for k in random_list[i]:
            f = True
            if (c['性别'] == '男性'):
                if i=='体质' and k in [1,3,4,7,9,14,17,22,26]:
                    continue;
            if (c['性别'] == '女性'):
                if i =='体质' and k in [11,13,21]:
                    continue;
            for j in c['属性'][i]:
                if not(check_conflict(random_list[i][k],j)):
                    f = False
            if (f):
                get = quaility_random(random_list[i][k])
                if get != None:
                    c['属性'][i].append(get)
    
    #体力值
    pp = random.randint(1000,2000)
    #气力值
    ep = random.randint(1500,2500)
    #理智值
    mp = random.randint(1500,2500)

    c['最大体力值'] = pp
    c['最大气力值'] = ep
    c['最大理智值'] = mp
    c['体力值'] = c['最大体力值']
    c['气力值'] = c['最大气力值']
    c['理智值'] = c['最大理智值']
    c['CharacterId'] = a.sav()['character_list']['character_number']
    if c['名字'] == '主人公':
        if c['性别'] != '男性':
            s = random.randint(0,len(random_name['女性'])-1)
            c['名字'] = random_name['女性'][s]
    
    body_type_creat(c)
    updata_exp(c)

    return c

def quaility_random(d):
    sum = 0
    for i in d:
        sum += d[i]
    empty = 100 - sum
    select = random.randint(1,100)
    select -= empty
    if (select<0): return None
    else:
        for i in d:
            if select<d[i]:
                return i
                break
            select -= d[i]

def check_conflict(d,q):
    #输出冲突列表d.待测项目q
    for i in d:
        if i==q:
            return False
    return True

def updata_exp(c):
    if (not('处女' in c['属性']['体质']) and c['性别'] != '男性'):
        c['经验']['v经验'] = random.randint(1,10)
        c['经验']['腔射经验'] = random.randint(0,1)
    if not('A处女' in c['属性']['体质']):
        c['经验']['A经验'] = random.randint(1,10)
        c['经验']['肛射经验'] = random.randint(0,1)
    if (not('童贞' in c['属性']['体质']) and c['性别'] != '女性'):
        c['经验']['V插入经验'] = random.randint(1,10)
        c['经验']['射精经验'] = 1