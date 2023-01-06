import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import P_size_trans, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 32
def com32(active,passive):

    #成功判定
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['受缚']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    size = ''

    if check_equipment(passive,32):
    
        pm['屈服'] += 300
        pm['欲情'] += 50
        pm['恐惧'] += 500
        pm['反感'] += 50
        pm['好感度'] += 1
        pe['受缚经验'] += 1
        sum_pp(passive,[0,10,10])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
    else:
        append_doing_list(active,passive,32)
        passive['标志']['口枷'] = True
        comkojo(active,passive,comid,{'com':'add'})
        
    return f

def undocom32(active,passive):
    remove_equipment(passive,32)
    comkojo(active,passive,comid,{'com':'undo'})
    passive['标志']['口枷'] = False
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    
def remove_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            a.tmp()['执行列表'].remove(i)

def check_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            return True
    return False