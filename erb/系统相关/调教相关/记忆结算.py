from math import pow
import erajs.api as a
from erb.系统相关.页面.character_upgrade import character_upgrade_page
from funcs import unwait, wait

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
            m[i] = int(int(m[i]/(pow(10,l-1)))*pow(10,l-2))
        for i in m:
            if i in ['V润','A润']:
                continue
            if m[i]>0:
                a.t('{}:{}+{} = {}'.format(i,c['记忆'][i+'记忆'],m[i],c['记忆'][i+'记忆']+m[i]))
                a.t()
                c['记忆'][i+'记忆'] += m[i]
            m[i] = 0

        a.divider('由高潮产生的额外记忆')
        #高潮产生的补正
        wm = c['待处理记忆']
        for i in wm:
            if '高潮' in i:
                if wm[i]>0:
                    item_name = i
                    item_name = item_name.replace('高潮','')
                    a.t('{}:{}+{} = {}'.format(item_name,c['记忆'][item_name+'记忆'],wm[i],c['记忆'][item_name+'记忆']+wm[i]))
                    a.t()
                    c['记忆'][item_name+'记忆'] += wm[i]
                    wm[i] = 0

    e = c['待处理经验']
    for i in e:
        if e[i]>0:
            a.t('{}:{}+{} = {}'.format(i,c['经验'][i],e[i],c['经验'][i]+e[i]))
            a.t()
            c['经验'][i] += e[i]
        e[i] = 0
    

    if c['CharacterId'] != 0:
        #开发提升页面
        a.goto(character_upgrade_page, c, enter_mode='after train')
    else:
        a.b('继续', unwait)
        
