import erajs.api as a
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

def com2(active,passive):
    a.page()
    a.divider()
    a.mode()

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['B']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False#记录本指令是否执行成功

    if check_doing_list(active,passive,2):
        pm['快B'] += 20 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 20 * (1+active['开发']['指技']*1)
        pm['欲情'] += 10 * (1+active['开发']['指技']*1)
        pm['习得'] += 5 * (1+active['开发']['指技']*1)
        am['习得'] += 5
        pm['反感'] += 10
        pe['B经验'] += 1
        if sq(passive, '巨乳'):
            a.t('{}的手在{}那巨大的乳房上抓揉抚摸'.format(aname,pname),True)
        elif sq(passive,'贫乳'):
            a.t('{}的手在{}平坦的胸部上轻柔抚摸'.format(aname,pname),True)
        else:
            a.t('{}的手在{}的胸部上抚摸'.format(aname,pname),True)
        a.t()
        pm['好感度'] = 1
        active['待处理体力变化'] = [0,10,5]
        passive['待处理体力变化'] = [0,20,10]

        f = True
        
    else:
        if obey_check(0,active,passive,com_trait):
            active['标志']['手占用'] = 2
            append_doing_list(active,passive,2)
        else:
            a.t('{}架开了{}的咸猪手'.format(pname,aname),True)
            a.t()
            pm['反感'] += 20
            pm['好感度'] = -5
    
    return f
def undocom2(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],2])
    active['标志']['手占用'] = 0
    a.repeat()
    #a.t()