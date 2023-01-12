import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 21
def com21(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['C']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    
    if check_doing_list(active,passive,21):
        
        pm['快C'] += 100
        pm['羞耻'] += 70
        pm['欲情'] += 150
        pm['屈服'] += 30
        pm['恭顺'] += 20
        pm['恐惧'] += 50
        am['习得'] += 10
        pm['反感'] += 20
        pe['C经验'] += 1
        pm['好感度'] += 0

        sum_pp(passive,[0,180,10])
        comkojo(active,passive,21,{'com':'doing'})
        f = True
        
    else:
        if  obey_check(0,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 21
            append_doing_list(active,passive,21)
            comkojo(active,passive,21,{'com':'add'})
        else:
            pm['反感'] += 10
            pm['好感度'] += -2
            comkojo(active,passive,21,{'com':'fail'})
    return f

def undocom21(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],21])
    active['标志']['手占用'] = 0
    comkojo(active,passive,21,{'com':'undo'})
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False