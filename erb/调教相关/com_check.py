import erajs.api as a
from ..人物相关.character_class import search_quaility as sq

#还需添加：h氛围，淫纹，相性
def obey_check(difficulty,active,passive,com_trait):
    al = {}
    pl = {}
    al_check_list = {
        '人气':5,'魅惑':10,'倾国':15,
        '诱惑':10,'煽动':10,
    }
    for i in al_check_list:
        if sq(active,i):
            al[i] = al_check_list[i]
    

    pl_check_list = {
        '反抗':-15,'坦率':5,'顺从':10,'幼稚':10,'高傲':-10,
        '自卑':5,'自制':-10,'纵欲':2*passive['开发']['欲望'],
        '好奇心':5,'保守':-10,'倒错':int(0.1*difficulty),
        '献身':5,'难以逾越的底线':int(-0.1*difficulty),
        '不知耻':5,'怕羞':-5,'纯情':-5,'好色':10,
        '忧郁':-5,'狂乱':-999,'崩坏':999,'幼儿退化':999,
        '欲望压抑':-5,'欲望解放':2*passive['开发']['欲望'],
        '淫乱':10,
    }
    for i in al_check_list:
        if sq(passive,i):
            pl[i] = pl_check_list[i]
    
    if '处女破坏' in com_trait:
        if sq(passive,'处女'):
            pl['处女'] = -15
    if 'V插入' in com_trait:
        if sq(passive,'重视贞操'):
            pl['重视贞操'] = -10
        if sq(passive,'无节操'):
            pl['无节操'] = 5
    if 'V' in com_trait:
        if passive['开发']['V感觉']>0:
            pl['V感觉Lv{}'.format(passive['开发']['V感觉'])] = passive['开发']['V感觉']*passive['开发']['欲望']
        if sq(passive,'淫壶'):
            pl['淫壶'] = 10
    if 'A' in com_trait:
        if passive['开发']['A感觉']>0:
            pl['A感觉Lv{}'.format(passive['开发']['A感觉'])] = passive['开发']['A感觉']*passive['开发']['欲望']
        if sq(passive,'淫尻'):
            pl['淫尻'] = 10
    if 'B' in com_trait:
        if passive['开发']['B感觉']>0:
            pl['B感觉Lv{}'.format(passive['开发']['B感觉'])] = passive['开发']['B感觉']*passive['开发']['欲望']
        if sq(passive,'淫乳'):
            pl['淫乳'] = 10
    if 'M' in com_trait:
        if passive['开发']['M感觉']>0:
            pl['M感觉Lv{}'.format(passive['开发']['M感觉'])] = passive['开发']['M感觉']*passive['开发']['欲望']
        if sq(passive,'淫唇'):
            pl['淫唇'] = 10
    if 'C' in com_trait:
        if passive['开发']['C感觉']>0:
            pl['C感觉Lv{}'.format(passive['开发']['C感觉'])] = passive['开发']['C感觉']*passive['开发']['欲望']
        if sq(passive,'淫核'):
            pl['淫核'] = 10
    if 'P' in com_trait:
        if passive['开发']['P感觉']>0:
            pl['P感觉Lv{}'.format(passive['开发']['P感觉'])] = passive['开发']['P感觉']*passive['开发']['欲望']
        if sq(passive,'淫靡尿道'):
            pl['淫靡尿道'] = 10
    if 'W' in com_trait:
        if passive['开发']['W感觉']>0:
            pl['W感觉Lv{}'.format(passive['开发']['W感觉'])] = passive['开发']['W感觉']*passive['开发']['欲望']
        if sq(passive,'淫靡子宫'):
            pl['淫靡子宫'] = 10

    if '疼痛' in com_trait:
        if sq(passive,'怕痛'):
            pl['怕痛'] = -10
        if sq(passive,'耐痛'):
            pl['耐痛'] = 5
        if passive['开发']['M属性']>0:
            pl['M属性Lv{}'.format(passive['开发']['M属性'])] = 2*passive['开发']['M属性']
    if '饮精' in com_trait:
        if sq(passive, '精爱味觉'):
            pl['精爱味觉'] = 20
    if '精液' in com_trait:
        if passive['开发']['精液成瘾']>0:
            pl['精液成瘾Lv{}'.format(passive['开发']['精液成瘾'])] = passive['开发']['精液成瘾']*passive['开发']['欲望']
    if '自慰' in com_trait:
        if passive['开发']['自慰成瘾']>0:
            pl['自慰成瘾Lv{}'.format(passive['开发']['自慰成瘾'])] = passive['开发']['自慰成瘾']*passive['开发']['欲望']
    if '污臭' in com_trait:
        if sq(passive,'污臭敏感'):
            pl['污臭敏感'] = -10
        if sq(passive,'污臭钝感'):
            pl['污臭钝感'] = 5
    if '药物' in com_trait:
        if passive['刻印']['药毒刻印']>0:
            pl['药毒刻印'] = 5*passive['刻印']['药毒刻印']
    if '露出' in com_trait:
        if sq(passive,'不知耻'):
            pl['不知耻'] = 5
        if sq(passive, '怕羞'):
            pl['怕羞'] = -10
        if sq(passive,'喜欢受人注目'):
            pl['喜欢受人注目'] = 10
        if passive['开发']['露出癖']>0:
            pl['露出癖Lv{}'.format(passive['开发']['露出癖'])] = passive['开发']['露出癖']*passive['开发']['欲望']
    if '中出' in com_trait:
        if sq(passive,'被射成瘾'):
            pl['被射成瘾'] = 10
        if passive['开发']['被射中毒']>0:
            pl['被射中毒Lv{}'.format(passive['开发']['被射中毒'])] = passive['开发']['被射中毒']*passive['开发']['欲望']
    if '触手' in com_trait:
        if passive['开发']['触手适性']>0:
            pl['触手适性Lv{}'.format(passive['开发']['触手适性'])] = passive['开发']['触手适性']*passive['开发']['欲望']
    if '兽交' in com_trait:
        if passive['开发']['兽交中毒']>0:
            pl['兽交中毒Lv{}'.format(passive['开发']['兽交中毒'])] = passive['开发']['兽交中毒']*passive['开发']['欲望']
    if '主导' in com_trait:
        if passive['开发']['侍奉欲望']>0:
            pl['侍奉欲望Lv{}'.format(passive['开发']['侍奉欲望'])] = passive['开发']['侍奉欲望']*passive['开发']['欲望']
        if sq(passive,'献身'):
            pl['献身'] = 5
        if sq(passive,'小恶魔'):
            pl['小恶魔'] = 5
        if passive['开发']['S属性']>0:
            pl['S属性Lv{}'.format(passive['开发']['S属性'])] = passive['开发']['S属性']*passive['开发']['欲望']
    if '排泄' in com_trait:
        if passive['开发']['排泄成瘾']>0:
            pl['排泄成瘾Lv{}'.format(passive['开发']['排泄成瘾'])] = passive['开发']['排泄成瘾']*passive['开发']['欲望']

    if active['性别'] == '男性':
        if sq(passive,'厌男'):
            pl['厌男'] = -10
        if passive['性别'] == '男性':
            if passive['开发']['男同中毒']>0:
                pl['男同中毒Lv{}'.format(passive['开发']['男同中毒'])] = passive['开发']['男同中毒']*passive['开发']['欲望']
    if active['性别'] == '女性':
        if sq(passive,'厌女'):
            pl['厌女'] = -10
        if passive['性别'] == '女性':
            if passive['开发']['百合中毒']>0:
                pl['百合中毒Lv{}'.format(passive['开发']['百合中毒'])] = passive['开发']['百合中毒']*passive['开发']['欲望']


    l = {'苦痛刻印':3,'快乐刻印':3,'屈服刻印':3,'药毒刻印':3,'羞耻刻印':3,'恐惧刻印':3,'反发刻印':-10}
    for i in l:
        if passive['刻印'][i]>0:
            pl['{}}Lv{}'.format(i,passive['开发'][i])] = passive['开发'][i]*3*l[i]
    
    l = {'慕恋':10,'亲爱':20,'相爱':30,'服从':10,'隶属':30,'烙印':20,'妄信':30,'淫乱':15}
    for i in l:
        if sq(passive,i):
            pl[i] = pl_check_list[i]
    
    if passive['开发']['服从']>0:
            pl['服从Lv{}'.format(passive['开发']['服从'])] = passive['开发']['服从']*5
    
    text = ''
    count = 0
    for i in pl:
        text = text + '{}({})+'.format(i,pl[i])
        count = count +pl[i] 
    for i in al:
        text = text + '{}({})+'.format(i,al[i])
        count = count +pl[i] 
    text = text+'...={}'.format(count)
    if count > difficulty:
        text = text+'>{}(难度) 成功'.format(difficulty)
        a.t(text,True,style = {'color':'#0f0'})
        a.t()
        return True
    elif count <= difficulty:
        text = text+'<={}(难度) 失败'.format(difficulty)
        a.t(text,True,style = {'color':'#f00'})
        a.t()
        return False
    
