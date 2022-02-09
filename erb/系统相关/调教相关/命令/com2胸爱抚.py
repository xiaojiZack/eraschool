import erajs.api as a
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list
from erb.系统相关.调教相关.好感度和侍奉快乐 import cal_favor
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
from ..memory_cal import memory_cal
from ..体力衰减 import decrease_pp

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
    decrease_a = []
    decrease_p = []
    favor = []
    f = False#记录本指令是否执行成功

    if obey_check(0,active,passive,com_trait):
        active['标志']['手占用'] = 2
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
        decrease_a = [0,10,5]
        decrease_p = [0,20,10]
        favor = [1,0]
        f = True
        append_doing_list(active,passive,2)
    else:
        a.t('{}架开了{}的咸猪手'.format(pname,aname),True)
        a.t()
        pm['反感'] += 20
        favor = [-5,0]
    
    cal_favor(passive,favor)
    decrease_pp(active,decrease_a)
    decrease_pp(passive,decrease_p)
    if active['CharacterId'] != 0:
        active = memory_cal(active)
    if passive['CharacterId'] != 0:
        passive = memory_cal(passive)
    
    a.repeat()
    return f
def undocom2(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],2])
    active['标志']['手占用'] = 0
    a.repeat()
    #a.t()