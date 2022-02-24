import erajs.api as a
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

def com37(active,passive):
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['V','扩张']
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
    
    if check_equipment(passive,37):
        
        pm['快V'] += 5

        pm['羞耻'] += 5
        pm['欲情'] += 10
        pm['苦痛'] += 20
        pm['恐惧'] += 10
        am['习得'] += 5
        pm['反感'] += 10

        pe['V经验'] += 1
        pe['V扩张经验'] += 2
        pm['好感度'] += 0

        sum_pp(passive,[0,20,10])

        f = True
        
    else:
        if  obey_check(25,active,passive,com_trait):
            #此处可能需要处理替换的问题
            append_doing_list(active,passive,37)
        else:
            pm['反感'] += 15
            pm['好感度'] += -3

    return f

def undocom37(active,passive):
    remove_equipment(passive,37)
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