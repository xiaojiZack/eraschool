from math import pow
import erajs.api as a
from erb.系统相关.页面.character_upgrade import character_upgrade_page
from funcs import unwait, wait

def end_cal(c):
    a.divider('{}本次所得记忆和经验'.format(c['名字']))

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
    
    #调教结束后射精槽位设为0
    if c['性别'] != '女性':
        try:
            c['其他参数']['射精数值'] = 0
        except:
            pass
    

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
    
    init_character(c)
        

def init_character(c):
    #调教结束后重置角色状态
    c['身体信息']['阴茎']['插入位置'] = {}
    c['待处理体力变化'] = [0,0,0]
    c['标志']['手占用'] = 0
    c['标志']['口占用'] = 0
    c['标志']['胸占用'] = 0
    c['标志']['阴茎占用'] = 0
    c['标志']['受缚类型'] = 0
    c['标志']['口枷'] = False
    c['调教状态'] = []