import erajs.api as a
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
from ..memory_cal import memory_cal
from ..体力衰减 import decrease_pp
from ..好感度和侍奉快乐 import cal_favor

def com5(active,passive):
    a.page()
    a.divider()
    a.mode()

    #成功判定
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['C','V','处女破坏']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    flag = check_size(passive['开发']['V扩张度'],'手指',passive['身体信息']['阴道']['内容固体'])
    if flag == False:
        com_trait.append('尺寸过大')
        com_trait.append('疼痛')
    
    if (flag or a.tmp()['调教数据']['尺寸警告标志'] == False):
        if  obey_check(20,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 5
            pm['快C'] += 5 * (1+active['开发']['指技']*1)
            pm['快V'] += 10 * (1+active['开发']['指技']*1)
            pm['羞耻'] += 10 * (1+active['开发']['指技']*1)
            pm['欲情'] += 5 * (1+active['开发']['指技']*1)
            pm['习得'] += 5 * (1+active['开发']['指技']*1)
            am['习得'] += 5
            pm['反感'] += 10
            pe['C经验'] += 1
            pe['V经验'] += 1
            decrease_a = [0,10,5]
            decrease_p = [0,20,10]
            favor = [1,0]
            if flag == False:
                size_punish(passive)
            f = True
            append_doing_list(active,passive,5)
        else:
            pm['反感'] += 50
            favor = [-5,0]
    
        passive['身体信息']['阴道']['内容固体'][active['名字']] = '手指'

        cal_favor(passive,favor)
        decrease_pp(active,decrease_a)
        decrease_pp(passive,decrease_p)
        if active['CharacterId'] != 0:
            active = memory_cal(active)
        if passive['CharacterId'] != 0:
            passive = memory_cal(passive)
        
        a.repeat()
    return f

def undocom5(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],5])
    active['标志']['手占用'] = 0
    passive['身体信息']['阴道']['内容固体'].remove([active['名字']])
    #a.t()
    a.repeat()