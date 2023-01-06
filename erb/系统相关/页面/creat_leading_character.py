import erajs.api as a
from erb.系统相关.事件.event_0_开幕 import event0
from .main_page import main_page
from erb.系统相关.人物相关.character_creat import new_character_dict, body_type_creat

def creat_leading_character():
    #创建主角
    def Basic():
        #口上设定部分未完成
        a.cls()
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
                a.sav()['资源']['金钱'] += 20000
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
        a.t('好为人师:在指导中略微提升所有在场者的经验获取，仅对低于自身的项目有效,未实装')
        a.t()
        a.t('爱抚知识:提升爱抚系调教、授课的效果,未实装')
        a.t()
        a.t('扩张知识:提高扩张系调教、授课的效果,未实装')
        a.t()
        a.t('SM才能:提高SM系调教、授课的效果,未实装')
        a.t()
        a.t('快速回复:提高每日体力气力的回复量')
        a.t()
        a.t('魅惑:使命令更容易执行')
        a.t()
        a.t('扶持政策:初始获得20,000启动资金')

    ec = new_character_dict()
    ec['CharacterId'] = 0
    ec['最大体力值'] = 2000
    ec['最大气力值'] = 1200
    ec['体力值'] = ec['最大体力值']
    ec['气力值'] = ec['最大气力值']
    ec['种族'] = '人类'
    #talent_point = a.sav()['achievement']['achievement_point']+1
    talent_point = 10
    a.tmp()['talent_point'] = talent_point
    a.goto(Basic)

def leading_character_show(c):
    def addcharacter(c):
        a.sav()['character_list']['主角'] = c
        a.clear()
        a.goto(event0)
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

