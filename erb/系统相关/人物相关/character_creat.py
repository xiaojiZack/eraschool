
import erajs.api as a
from erb.系统相关.调教相关.服装.服装 import creat_normal_cloth
from ..人物相关.quaility_list import random_list
from ..人物相关.random_name import random_name
from ..人物相关.character_class import new_character_dict, search_quaility
import random

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

    organ_updata(c)

#器官数据生成
def organ_updata(c):
    o = c['身体信息']
    size_describ = ['紧闭','闭合','微闭','名器','普通','微张','略张','张开','扩张','崩坏']

    V = o['阴道']
    V['尺寸'] = size_describ[c['开发']['V扩张度'] - c['开发']['V名器度']]


    s = o['肠道']
    standard = 3000 #标准值 3000ml
    standard = int(standard*((o['具体身高']*1.0)/170))
    #改造判断 (预留)
    s['容量'] = standard

    s = o['胃']
    standard = 2000 #标准值 2000ml
    standard = int(standard*((o['具体身高']*1.0)/170))
    #改造判断 (预留)
    s['容量'] = standard

    A = o['肛门']
    A['尺寸'] = size_describ[c['开发']['A扩张度'] - c['开发']['A名器度']]

    u = o['尿道']
    standard = 1000 #标准值 1000ml
    standard = int(standard*((o['具体身高']*1.0)/170))
    #改造判断 (预留)
    u['容量'] = standard
    u['尺寸'] = size_describ[c['开发']['尿道扩张度'] - c['开发']['尿道名器度']]

    w = o['子宫']
    standard = 100
    standard = int(standard*((o['具体身高']*1.0)/170))
    #改造判断 (预留)
    w['容量'] = standard

    B = o['乳房']
    standard = 800
    if search_quaility(c,'贫乳'):
            standard = 400
    elif search_quaility(c,'巨乳'):
        standard = 1500
    elif search_quaility(c,'超乳'):
        standard = 3000
    elif search_quaility(c,'魔乳'):
        standard = 5000
    standard = int(standard*((o['具体身高']*1.0)/170))
    produce = int(standard*0.5)#生产速度
    ejct = 0.2#表示为内部所有液体的比值
    #改造判断 (预留)
    B['容量'] = standard
    if search_quaility(c,'母乳体质'):
        B['生产速度'] = produce
        B['标准射出量'] = ejct

    p = o['阴茎']
    standard = 50
    standard_length = 10.0
    standard_diameter = 3.0
    standard = int(standard*((o['具体身高']*1.0)/170))
    produce = int(standard*0.25)#生产速度
    ejct = 0.5#表示为内部所有液体的比值
    endure = 10000#忍耐极限
    #改造判断 (预留)
    p['容量'] = standard
    p['生产速度'] = produce
    p['标准射出量'] = ejct
    p['尺寸'] = '普通根'
    p['忍耐极限'] = endure
    if search_quaility(c,'巨根'):
        standard_length = 15.0
        standard_diameter = 4.5
        p['尺寸'] = '巨根'
    elif search_quaility(c,'小根'):
        standard_length = 7.0
        standard_diameter = 2.0
        p['尺寸'] = '小根'
    elif search_quaility(c,'迷你根'):
        standard_length = 4.0
        standard_diameter = 1.0
        p['尺寸'] = '迷你根'
    elif search_quaility(c,'马根'):
        standard_length = 25.0
        standard_diameter = 6.0
        p['尺寸'] = '马根'
    elif search_quaility(c,'龙根'):
        standard_length = 40.0
        standard_diameter = 10.0
        p['尺寸'] = '龙根'
    error = random.randint(-10,10)*0.1
    standard_length = standard_length +error
    error = random.randint(-10,10)*0.05
    standard_diameter = standard_diameter + error

def creat_normal_character(character=None):
    c = character
    if c == None:
        c = new_character_dict()
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
    #c['CharacterId'] = a.sav()['character_list']['character_number']+1
    if c['名字'] == '主人公':
        #if c['性别'] != '男性':
        s = random.randint(0,len(random_name['女性'])-1)
        c['名字'] = random_name['女性'][s]
    
    body_type_creat(c)
    updata_exp(c)
    #衣物生成
    creat_normal_cloth(c)

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
        c['经验']['v性交经验'] = random.randint(1,10)
        c['经验']['腔射经验'] = random.randint(0,1)
    if not('A处女' in c['属性']['体质']):
        c['经验']['A经验'] = random.randint(1,10)
        c['经验']['A性交经验'] = random.randint(1,10)
        c['经验']['肛射经验'] = random.randint(0,1)
    if (not('童贞' in c['属性']['体质']) and c['性别'] != '女性'):
        c['经验']['V插入经验'] = random.randint(1,10)
        c['经验']['射精经验'] = 1