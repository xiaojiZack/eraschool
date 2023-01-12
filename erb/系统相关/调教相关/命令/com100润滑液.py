import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from funcs import unwait, wait
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

comid = 100
def com100(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = []
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False

    def select_place():
        def select_v():
            pm['V润'] += 10000
            unwait()

        def select_A():
            pm['A润'] += 10000
            unwait()

        a.divider()
        a.mode()
        a.t('要涂抹哪里？')
        a.t()
        a.mode('grid', 2)
        a.b('腔穴', select_v)
        a.t()
        a.b('尻穴', select_A)
        wait()

    if obey_check(0,active,passive,com_trait):
        select_place()
        a.sav()['物品']['润滑液'] -= 1
        comkojo(active,passive,comid,{'com':'add'})
    else:
        comkojo(active,passive,comid,{'com':'fail'})
        pm['反感'] += 50
        pm['好感度'] += -5

        f = False

    return f
