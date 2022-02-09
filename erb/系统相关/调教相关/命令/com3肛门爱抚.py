import erajs.api as a
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
from ..memory_cal import memory_cal
from ..体力衰减 import decrease_pp
from ..好感度和侍奉快乐 import cal_favor
#爱抚
def com3(active,passive):
    a.page()
    a.divider()
    a.mode()

    #成功判定
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A','疼痛','污臭']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    f = False

    if obey_check(10,active,passive,com_trait):
        #此处可能需要处理替换的问题
        active['标志']['手占用'] = 3
        pm['快A'] += 5 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 10 * (1+active['开发']['指技']*1)
        pm['欲情'] += 5 * (1+active['开发']['指技']*1)
        pm['习得'] += 5 * (1+active['开发']['指技']*1)
        am['习得'] += 5
        pm['反感'] += 15
        pe['A经验'] += 1
        a.t('{}的手在{}身上轻柔抚摸'.format(aname,pname),True)
        a.t()
        decrease_a = [0,10,5]
        decrease_p = [0,20,10]
        favor = [1,0]
        f = True
        append_doing_list(active,passive,3)
    else:
        a.t('{}试图抚摸{},但被{}躲开了'.format(aname,pname,pname),True)
        pm['反感'] += 50
        favor = [-5,0]
        f = False
    
    cal_favor(passive,favor)
    decrease_pp(active,decrease_a)
    decrease_pp(passive,decrease_p)
    if active['CharacterId'] != 0:
        active = memory_cal(active)
    if passive['CharacterId'] != 0:
        passive = memory_cal(passive)
    
    a.repeat()
    return f

def undocom3(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],3])
    active['标志']['手占用'] = 0
    a.repeat()
    #a.t()