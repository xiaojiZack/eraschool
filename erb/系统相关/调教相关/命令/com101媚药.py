import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.液体 import inject_liquid
from funcs import unwait, wait
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

comid = 101
def com101(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['药物','M']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False


    if obey_check(80,active,passive,com_trait):
        inject_liquid(passive, '胃', {'媚药':100})
        pm['恐惧'] += 3000
        pm['药毒'] += 3000
        pm['反感'] += 5000
        pm['屈服'] += 1000
        pm['欲情'] += 100
        pe['药物经验'] += 1
        comkojo(active,passive,comid,{'com':'add'})
    else:
        comkojo(active,passive,comid,{'com':'fail'})
        pm['反感'] += 8000
        pm['好感度'] += -5

        f = False

    return f
