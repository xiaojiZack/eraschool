import erajs.api as a
from erb.系统相关.口上相关.口上调用 import markkojo
from ..人物相关.character_class import search_quaility as sq

def mark_get(c,memory):
    m = memory
    #反发刻印
    f = True
    l = ['相爱','亲爱','服从','隶属','烙印']
    for i in l:
        if sq(c,i):
            f = False
    if f:
        get_mark = 0
        if (m['反感']>4000 or c['调教记忆']['反感']>10000) and c['刻印']['反发刻印']<3 and c['刻印']['屈服刻印']<3:
            get_mark = 3
        elif (m['反感']>1000 or c['调教记忆']['反感']>5000) and c['刻印']['反发刻印']<2 and c['刻印']['屈服刻印']<2:
            get_mark = 2        
        elif (m['反感']>500 or c['调教记忆']['反感']>1000) and c['刻印']['反发刻印']<1 and c['刻印']['屈服刻印']<1:
            get_mark = 1         
        if get_mark:
            a.t('{}取得反发刻印Lv{}'.format(c['名字'],get_mark))
            a.t()
            c['刻印']['反发刻印'] = get_mark
            markkojo(person = c,information = {'反发刻印':get_mark})
    
    #苦痛刻印
    get_mark = 0
    if (m['苦痛']>1000 or c['调教记忆']['苦痛']>10000) and c['刻印']['苦痛刻印']<3:
        get_mark = 3
    elif (m['苦痛']>500 or c['调教记忆']['苦痛']>5000) and c['刻印']['苦痛刻印']<2:
        get_mark = 2
    elif (m['苦痛']>200 or c['调教记忆']['苦痛']>1000) and c['刻印']['苦痛刻印']<1:
        get_mark = 1
    if get_mark:
            a.t('{}取得苦痛刻印Lv{}'.format(c['名字'],get_mark))
            a.t()
            c['刻印']['苦痛刻印'] = get_mark
            markkojo(person = c,information = {'苦痛刻印':get_mark})
    
    #快乐刻印
    happy = 0
    get_mark = 0
    for i in ['快C','快B','快V','快A','快M','快W','快U']:
        happy += m[i]
        happy += c['调教记忆'][i]/100
    if (happy>50000) and c['刻印']['快乐刻印']<3:
        get_mark = 3
    elif (happy>10000) and c['刻印']['快乐刻印']<2:
        get_mark = 2
    elif (happy>5000) and c['刻印']['快乐刻印']<1:
        get_mark = 1
    if get_mark:
        a.t('{}取得快乐刻印Lv{}'.format(c['名字'],get_mark))
        a.t()
        c['刻印']['快乐刻印'] = get_mark
        markkojo(person = c,information = {'快乐刻印':get_mark})
    
    #屈服刻印
    get_mark = 0
    if (m['屈服']>10000 or c['调教记忆']['屈服']>50000) and c['刻印']['屈服刻印']<3:
        get_mark = 3
    elif (m['屈服']>5000 or c['调教记忆']['屈服']>20000) and c['刻印']['屈服刻印']<2:
        get_mark = 2
    elif (m['屈服']>1000 or c['调教记忆']['屈服']>5000) and c['刻印']['屈服刻印']<1:
        get_mark = 1
    if get_mark:
        a.t('{}取得屈服刻印Lv{}'.format(c['名字'],get_mark))
        a.t()
        c['刻印']['屈服刻印'] = get_mark
        markkojo(person = c,information = {'屈服刻印':get_mark})

    #药毒刻印
    get_mark = 0
    if (m['药毒']>10000 or c['调教记忆']['药毒']>20000) and c['刻印']['药毒刻印']<3:
        get_mark = 3
    elif (m['药毒']>5000 or c['调教记忆']['药毒']>10000) and c['刻印']['药毒刻印']<2:
        get_mark = 2
    elif (m['药毒']>1000 or c['调教记忆']['药毒']>5000) and c['刻印']['药毒刻印']<1:
        get_mark = 1
    if get_mark:
        a.t('{}取得药毒刻印Lv{}'.format(c['名字'],get_mark))
        a.t()
        c['刻印']['药毒刻印'] = get_mark
        markkojo(person = c,information = {'药毒刻印':get_mark})

    #羞耻刻印
    get_mark = 0
    if (m['羞耻']>10000 or c['调教记忆']['羞耻']>100000) and c['刻印']['羞耻刻印']<3:
        get_mark = 3
    elif (m['羞耻']>5000 or c['调教记忆']['羞耻']>10000) and c['刻印']['羞耻刻印']<2:
        get_mark = 2
    elif (m['羞耻']>1000 or c['调教记忆']['羞耻']>5000) and c['刻印']['羞耻刻印']<1:
        get_mark = 1
    if get_mark:
        a.t('{}取得羞耻刻印Lv{}'.format(c['名字'],get_mark))
        a.t()
        c['刻印']['羞耻刻印'] = get_mark
        markkojo(person = c,information = {'羞耻刻印':get_mark})
    
    #恐惧刻印
    f = True
    l = ['慕恋','相爱','亲爱']
    for i in l:
        if sq(c,i):
            f = False
    if f:
        get_mark = 0
        if (m['恐惧']>1000 or c['调教记忆']['恐惧']>10000) and c['刻印']['恐惧刻印']<3:
            get_mark = 3
        elif (m['恐惧']>500 or c['调教记忆']['恐惧']>5000) and c['刻印']['恐惧刻印']<2:
            get_mark = 2
        elif (m['恐惧']>200 or c['调教记忆']['恐惧']>1000) and c['刻印']['恐惧刻印']<1:
            get_mark = 1
        if get_mark:
            a.t('{}取得恐惧刻印Lv{}'.format(c['名字'],get_mark))
            a.t()
            c['刻印']['恐惧刻印'] = get_mark
            markkojo(person = c,information = {'恐惧刻印':get_mark})
    
    #同化刻印
    get_mark = 0
    if (m['同化']>1000 or c['调教记忆']['同化']>10000) and c['刻印']['同化刻印']<3:
        get_mark = 3
    elif (m['同化']>500 or c['调教记忆']['同化']>5000) and c['刻印']['同化刻印']<2:
        get_mark = 2
    elif (m['同化']>200 or c['调教记忆']['同化']>1000) and c['刻印']['同化刻印']<1:
        get_mark = 1
    if get_mark:
        a.t('{}取得同化刻印Lv{}'.format(c['名字'],get_mark))
        a.t()
        c['刻印']['同化刻印'] = get_mark
        markkojo(person = c,information = {'同化刻印':get_mark})