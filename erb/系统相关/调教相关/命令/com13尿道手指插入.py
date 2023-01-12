import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入 import insert, insert_check
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 13
def com13(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['U']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    check_result = insert_check(active,passive,'F','V',com_trait)
    if check_doing_list(active,passive,13) and check_result!=False:
        insert(active,passive,'F','V',check_result)
            
        pm['快U'] += 10 * (1+active['开发']['指技']*1)

        pm['羞耻'] += 350 * (1+active['开发']['指技']*1)
        pm['欲情'] += 500 * (1+active['开发']['指技']*1)
        pm['习得'] += 500 * (1+active['开发']['指技']*1)
        pm['恐惧'] += 100 *2^(-active['开发']['指技']*1)
        pm['苦痛'] += 50
        am['习得'] += 5
        pm['反感'] += 50

        ae['指技经验'] += 1
        pe['U经验'] += 1 * (1+active['开发']['指技']*1)
        pm['好感度'] += 1 * (1+active['开发']['指技']*1)
        sum_pp(active,[0,15,5])
        sum_pp(passive,[0,150,40])
        comkojo(active,passive,13,{'com':'doing'})
        f = True
                    
    else:
        if  obey_check(60,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 13
            append_doing_list(active,passive,13)
            comkojo(active,passive,13,{'com':'add'})
        else:
            pm['反感'] += 200
            pm['好感度'] += -15
            comkojo(active,passive,13,{'com':'fail'})
        
    return f

def undocom13(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],13])
    active['标志']['手占用'] = 0
    comkojo(active,passive,13,{'com':'undo'})
    del passive['身体信息']['尿道']['内容固体'][active['名字']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False