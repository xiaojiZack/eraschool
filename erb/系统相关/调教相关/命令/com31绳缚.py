import time
import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list, remove_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 31
def com31(active,passive):

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
    
    if check_equipment(passive,31):
        t = passive['标志']['受缚类型']
        if t == 1:
            pm['恐惧'] += 500
            pm['屈服'] += 500
            pm['苦痛'] += 300
            pm['反感'] += 40
            pm['羞耻'] += 200

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,20,30])
        if t == 2:
            pm['恐惧'] += 500
            pm['屈服'] += 500
            pm['苦痛'] += 400
            pm['反感'] += 60
            pm['羞耻'] += 200

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,40,30])
        if t == 3:
            pm['恐惧'] += 500
            pm['屈服'] += 500
            pm['苦痛'] += 300
            pm['反感'] += 30
            pm['羞耻'] += 200

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,20,30])
        if t == 4:
            pm['恐惧'] += 500
            pm['屈服'] += 500
            pm['苦痛'] += 500
            pm['反感'] += 60
            pm['羞耻'] += 400

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,30,40])
        if t == 5:
            pm['恐惧'] += 800
            pm['屈服'] += 800
            pm['苦痛'] += 700
            pm['反感'] += 80
            pm['羞耻'] += 500

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,80,40])
        if t == 6:
            pm['恐惧'] += 800
            pm['屈服'] += 800
            pm['苦痛'] += 500
            pm['反感'] += 80
            pm['羞耻'] += 500

            pm['好感度'] += 0

            pe['受缚经验'] += 1
            sum_pp(passive,[0,50,30])
        comkojo(active,passive,comid,{'com':'doing'})
        f = True
        
    else:
        select_bound(passive)
        remove_all_bound_conflict(passive,passive['标志']['受缚类型'])
        append_doing_list(active,passive,31)
        comkojo(active,passive,comid,{'com':'add'})
    return f

def undocom31(active,passive):
    remove_equipment(passive,31)
    comkojo(active,passive,comid,{'com':'undo'})
    passive['标志']['受缚类型'] = 0
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False

def select_bound(c):
    def get_select(t):
        c['标志']['受缚类型'] =t
        a.tmp()['暂停'] = False
    a.page()
    a.mode()
    a.h('采用哪种捆绑方式？')
    a.divider()
    a.mode('line',2)
    a.b('[镣铐束缚]',get_select,1)
    a.t()
    a.t('束缚对方的手和脚')
    a.t()
    a.b('[龟甲缚]',get_select,2)
    a.t()
    a.t('以强调部分身体为特点的全身束缚，紧缚感和羞耻感都是上佳')
    a.t()
    a.b('[桌台束缚]',get_select,3)
    a.t()
    a.t('将四肢分别固定到桌台的四个角上，不算很紧，但足够让你为所欲为')
    a.t()
    a.b('[桌台束缚(背面)]',get_select,4)
    a.t()
    a.t('同桌台束缚，只不过是背面朝上')
    a.t()
    a.b('[四肢吊起]',get_select,5)
    a.t()
    a.t('将四肢吊起，体力消耗巨大，提供大量屈服和苦痛')
    a.t()
    a.b('[单脚站立]',get_select,6)
    a.t()
    a.t('令人辛苦地单脚站立的姿势，暴露性器的同时也会产生大量屈服感')

    a.tmp()['暂停'] = True
    while(a.tmp()['暂停']): time.sleep(0.1)

def remove_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            a.tmp()['执行列表'].remove(i)

def check_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            return True
    return False

#记录每一种捆缚的冲突指令
bound_conflict_table = {
    1:[12,55,61,65,67,68],
    2:[12,65,67,68],
    3:[12,51,52,53,54,55,57,58,59,60,61,65,67,68,70,71],
    4:[12,21,24,29,50,52,53,54,55,56,58,59,60,61,65,67,68,70,71],
    5:[12,50,51,52,55,56,57,58,61,65,67,68,70,71],
    6:[12,50,51,52,53,54,55,56,57,58,59,60,61,65,67,68,70,71],
}

def remove_all_bound_conflict(c,bound_type):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[0]:
            remove_doing_list(i[0],i[1],i[2])
        elif c['CharacterId'] == i[1] and i[1] in bound_conflict_table[bound_type]:
            remove_doing_list(i[0],i[1],i[2])

