import erajs.api as a
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
from ..memory_cal import memory_cal

def com1(active,passive):
    a.divider()
    a.mode()

    #成功判定
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['B','C']
    p = passive['待处理记忆']
    pe = passive['待处理经验']
    if obey_check(0,active,passive,com_trait):
        active['标志']['手占用'] = 1
        p['快B'] += 20 * (1+active['开发']['指技']*1)
        p['羞耻'] += 20 * (1+active['开发']['指技']*1)
        p['欲情'] += 10 * (1+active['开发']['指技']*1)
        p['习得'] += 5 * (1+active['开发']['指技']*1)
        p['反感'] += 10
        pe['C经验'] += 1
        pe['B经验'] += 1
        a.t('{}的手在{}身上轻柔抚摸'.format(aname,pname),True)
        a.t()