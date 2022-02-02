from scipy import rand

import erajs.api as a
from ..人物相关.quaility_list import random_list
from ..人物相关.random_name import random_name
from ..人物相关.character_class import new_character_dict
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
    c['CharacterId'] = a.sav()['character_list']['character_number']+1
    if c['名字'] == '主人公':
        #if c['性别'] != '男性':
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