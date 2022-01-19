from statistics import quantiles
import sys
sys.path.append("C:\\Users\\Zack\\Desktop\\develop\\eraschool\\src")
import erajs.api as a
import funcs as f
import character_class as cc
import random

def character_creat(gender):
    #创建新角色，首先需要输入默认性别
    #可以自定义的部分
    data = {"BasicProperty":{
        "CharacterId":0,
        "gender":gender,
        }}
    creat_leading_character(cc.new_character_dict())




def creat_leading_character(empty_character):
    #创建主角
    ec = empty_character
    ec['BasicProperty']["MAXPhysicalPower"] = 2000
    ec['BasicProperty']['MAXEnergyPower'] = 1200
    ec['BasicProperty']["PhysicalPower"] = ec['BasicProperty']["MAXPhysicalPower"]
    ec['BasicProperty']['EnergyPower'] = ec['BasicProperty']['MAXEnergyPower']
    ec['BasicProperty']['race'] = 'human'
    talent_point = a.sav()['achievement']['achievement_point']+1
    a.tmp()['talent_point'] = talent_point
    
    def BasicProperty():
        #口上设定部分未完成
        a.page()
        a.mode('line', 2)
        
        #BasicProperty
        def change_name(name):
            ec['BasicProperty']['name'] = name
        a.t('名字')
        a.input(change_name, ec['BasicProperty']['name'])
        a.t()

        def change_gender(gender):
            l = ['male','female']
            ec['BasicProperty']['gender'] = l[gender['index']-1]
        a.t('性别')
        s = 1
        if ec['BasicProperty']['gender'] == "male": s =1
        else: s =2
        a.dropdown(['男','女'], change_gender, s)
        a.t()

        a.t('点数:{}'.format(a.tmp()['talent_point']))
        a.t()
        a.mode('line',2)
        a.t('最大体力:')
        a.t(ec['BasicProperty']["MAXPhysicalPower"])
        def decrease():
            ec['BasicProperty']["MAXPhysicalPower"] -= 250
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['BasicProperty']["MAXPhysicalPower"] += 250
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['BasicProperty']["MAXPhysicalPower"]>1500:
            a.b('-', decrease)
        if ec['BasicProperty']["MAXPhysicalPower"]<2500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        
        a.t('最大气力:')
        a.t(ec['BasicProperty']["MAXEnergyPower"])
        def decrease():
            ec['BasicProperty']["MAXEnergyPower"] -= 100
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['BasicProperty']["MAXEnergyPower"] += 100
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['BasicProperty']["MAXEnergyPower"]>800:
            a.b('-', decrease)
        if ec['BasicProperty']["MAXEnergyPower"]<1500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        ec['BasicProperty']["PhysicalPower"] = ec['BasicProperty']["MAXPhysicalPower"]
        ec['BasicProperty']['EnergyPower'] = ec['BasicProperty']['MAXEnergyPower']
        
        a.b('下一步',a.goto, body, ec)

    def body(c):
        a.page()
        a.mode()
        a.b('返回', a.back)
        a.t()
        def length(i):
            if ('高大' in c['Quaility']['body_trait']):
                c['Quaility']['body_trait'].remove('高大')
            if ('小只' in c['Quaility']['body_trait']):
                c['Quaility']['body_trait'].remove('小只')
            if i['index'] == 1:
                pass
            else:
                c['Quaility']['body_trait'].append(i['value'])
        a.t('体型:')
        a.radio(['普通','高大','小只'], length, 1)
        a.t()

        def age(i): c['BasicProperty']['age'] = i['value']
        a.t('外表年龄:')
        a.radio(['儿童','少年','青年','大人'], age, 3)
        a.t()
        
        if (c['BasicProperty']['gender'] == "male"):
            def dick_length(i):
                if ('小根' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('小根')
                if ('巨根' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('巨根')
                if ('普通根' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('普通根')
                c['Quaility']['body_trait'].append(i['value'])
            a.t('阴茎尺寸:')
            a.radio(['普通根','小根','巨根'], dick_length, 1)
            a.t()
            def endure(i):
                if ('早泄' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('早泄')
                if ('迟泄' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('迟泄')
                if i['index'] == 1:
                    pass
                else:
                    c['Quaility']['body_trait'].append(i['value'])
            a.t('忍耐程度')
            a.radio(['普通','早泄','迟泄'], endure, 1)
            a.t()
            def v_insert(i):
                l = [0, 5, 20]
                c['SexExp']['vinsert'] = l[i['index']]
            a.t('V插入经验:')
            a.radio(['童贞','很少','很多'], v_insert, 1)
            a.t()
            def a_insert(i):
                l = [0, 5, 20]
                c['SexExp']['ainsert'] = l[i['index']]
            a.t('A插入经验:')
            a.radio(['童贞','很少','很多'],a_insert,1)
            a.t()
            def A(i):
                l = [0, 5, 20]
                c['SexExp']['a'] = l[i['index']]
            a.t('A性交经验')
            a.radio(['无','很少','很多'], A, 1)
            a.t()
        if (c['BasicProperty']['gender'] == "female"):
            def breast(i):
                if ('贫乳' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('贫乳')
                if ('美乳' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('美乳')
                if ('巨乳' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('巨乳')
                c['Quaility']['body_trait'].append(i['value'])
            a.t('乳房尺寸:')
            a.radio(['贫乳','美乳','巨乳'], breast, 2)
            a.t()
            def V(i):
                l = [0, 5, 20]
                c['SexExp']['v'] = l[i['index']]
            a.t('V性交经验')
            a.radio(['处女','很少','很多'],V,1)
            a.t()
            def A(i):
                l = [0, 5, 20]
                c['SexExp']['v'] = l[i['index']]
            a.t('A性交经验')
            a.radio(['A处女','很少','很多'],A,1)
            a.t()
            def wet(i):
                if ('易湿' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('易湿')
                if ('不易湿' in c['Quaility']['body_trait']):
                    c['Quaility']['body_trait'].remove('不易湿')
                c['Quaility']['body_trait'].append(i['value'])
            a.t('湿的程度')
            a.radio(['普通','易湿','不易湿'], wet, 1)
            a.t()
        
        def updata():
            if (c['SexExp']['v'] != 0 and '处女'in c['Quaility']['body_trait']):
                c['Quaility']['body_trait'].remove('处女')
            elif(c['SexExp']['v'] == 0 and not('处女'in c['Quaility']['body_trait'])):
                c['Quaility']['body_trait'].append('处女')
            if (c['SexExp']['a'] != 0 and 'A处女'in c['Quaility']['body_trait']):
                c['Quaility']['body_trait'].remove('处女')
            elif(c['SexExp']['a'] == 0 and not('A处女'in c['Quaility']['body_trait'])):
                c['Quaility']['body_trait'].append('A处女')
            if (c['SexExp']['vinsert'] != 0 or c['SexExp']['ainsert'] != 0
                and '童贞'in c['Quaility']['body_trait']):
                c['Quaility']['body_trait'].remove('童贞')
            elif(c['SexExp']['vinsert'] == 0 and c['SexExp']['ainsert'] == 0 
                and not('童贞'in c['Quaility']['body_trait'])):
                c['Quaility']['body_trait'].append('童贞')
            a.goto(character_show,c)

        a.b('下一步',a.goto,updata)
    
    def character_show(c):
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.t()

    
    def talent_pick(c):
        def add(i):
            if (i != '扶持政策' and i != '快速回复'):
                c["Quaility"]['speciality'].append(i)
            elif(i == '扶持政策'):
                a.sav()['resource']['money'] += 20000
            elif(i == '快速回复'):
                c["Quaility"]['body_trait'].append(i)
        a.page()
        a.mode()
        a.t('选择特典')
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
        
def body_type_creat(c):
    gender = c['BasicProperty']['gender']
    age = c['BasicProperty']['age']
    length = '普通'
    if ('高大' in c['Quaility']['body_trait']):
        length = '高大'
    if ('小只' in c['Quaility']['body_trait']):
        length = '小只'
    if (gender == 'male'): 
        l = random.randint(165,185)
        w = random.randint(60,75)
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
        c['BodyProperty']['real_length'] = l
        c['BodyProperty']['real_weight'] = w
    if (gender == 'female'):
        c['BasicProperty']['real_length'] 
        l = random.randint(155,175)
        w = random.randint(50,65)
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
        c['BodyProperty']['real_length'] = l
        c['BodyProperty']['real_weight'] = w
    
