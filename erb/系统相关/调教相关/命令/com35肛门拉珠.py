import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 35
def com35(active,passive):
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    a.page()
    a.mode()
    
    if check_equipment(passive,35):
        
        pm['快A'] += 80

        pm['羞耻'] += 500
        pm['欲情'] += 400
        pm['屈服'] += 800
        pm['苦痛'] += 400
        pm['恐惧'] += 300
        am['习得'] += 5
        pm['反感'] += 50

        pe['A经验'] += 2
        pm['好感度'] += 1

        sum_pp(passive,[0,100,15])
        comkojo(active,passive,comid,{'com':'doing'})

        f = True
        
    else:
        if  obey_check(20,active,passive,com_trait):
            #此处可能需要处理替换的问题
            append_doing_list(active,passive,35)
            comkojo(active,passive,comid,{'com':'add'})
        else:
            pm['反感'] += 15
            pm['好感度'] += -3
            comkojo(active,passive,comid,{'com':'fail'})

    return f

def undocom35(active,passive):
    remove_equipment(passive,35)
    comkojo(active,passive,comid,{'com':'undo'})
    passive['待处理记忆']['快A'] += 20
    passive['待处理经验']['A经验'] += 3
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