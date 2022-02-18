from math import pow
import erajs.api as a

def end_cal(c):
    a.divider('{}本次所得记忆和经验'.format(c['名字']))

    if c['CharacterId'] != 0:
        m = c['调教记忆']
        for i in m:
            temp = m[i]
            l = 0
            if temp == 0:
                l = 1
            while temp>1:
                temp = temp/10
                l += 1
            m[i] = int(m[i]/(pow(10,l-1))*pow(10,l-1))
        for i in m:
            if i in ['V润','A润']:
                continue
            if m[i]>0:
                a.t('{}:{}+{} = {}'.format(i,c['记忆'][i+'记忆'],m[i],c['记忆'][i+'记忆']+m[i]))
                a.t()
                c['记忆'][i+'记忆'] += m[i]
            m[i] = 0
    e = c['待处理经验']
    for i in e:
        if e[i]>0:
            a.t('{}:{}+{} = {}'.format(i,c['经验'][i],e[i],c['经验'][i]+e[i]))
            a.t()
            c['经验'][i] += e[i]
        e[i] = 0
    a.t('',True)
