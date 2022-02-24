import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.处女 import check_pure, pure_punish
from erb.系统相关.调教相关.插入尺寸计算 import check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

def com63(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['V']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    if check_doing_list(active,passive,63):
                        
        pm['苦痛'] += 10
        pm['欲情'] += 5 * (1+active['开发']['腰技']*1)
        pm['恭顺'] += 5 * (1+active['开发']['腰技']*1)
        pm['习得'] += 5 * (1+active['开发']['腰技']*1)
        pm['反感'] += 10
        pe['V经验'] += 1 * (1+active['开发']['腰技']*1)
        pm['好感度'] += 1 * (1+active['开发']['腰技']*1)
        
        am['欲情'] += 5 * (1+active['开发']['腰技']*1)
        am['习得'] += 5*(1+passive['开发']['腰技']*1)
        am['主导'] += 10*(1+passive['开发']['腰技']*1)
        ae['腰技经验'] += 1
        pe['腰技经验'] += 1
        
        sum_pp(active,[0,10,0])
        sum_pp(passive,[0,5,5])
        
        f = True
        
    else:
        #此处可能需要处理替换的问题
        append_doing_list(active,passive,63)
        
    return f

def undocom63(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],63])
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False