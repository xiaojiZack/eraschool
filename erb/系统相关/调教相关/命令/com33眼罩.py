import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import P_size_trans, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 33
def com33(active,passive):

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

    if check_equipment(passive,33):
    
        pm['屈服'] += 20
        pm['恐惧'] += 20
        pm['反感'] += 5
        pm['好感度'] += 1
        pe['受缚经验'] += 1
        sum_pp(passive,[0,30,20])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
    else:
        #此处可能需要处理替换的问题
        append_doing_list(active,passive,33)
        passive['标志']['眼罩'] = True
        comkojo(active,passive,comid,{'com':'add'})
        
    return f

def undocom33(active,passive):
    remove_equipment(passive,33)
    comkojo(active,passive,comid,{'com':'undo'})
    passive['标志']['眼罩'] = False
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