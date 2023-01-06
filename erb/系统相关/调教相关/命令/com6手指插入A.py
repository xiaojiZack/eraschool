import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入 import insert, insert_check
from erb.系统相关.调教相关.插入尺寸计算 import check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 6
def com6(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A','疼痛','污臭']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    check_result = insert_check(active,passive,'F','A',com_trait)
    if check_doing_list(active,passive,6) and check_result!=False:
        insert(active,passive,'F','A',check_result)
                
        pm['快A'] += 15 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 150 * (1+active['开发']['指技']*1)
        pm['欲情'] += 50 * (1+active['开发']['指技']*1)
        pm['习得'] += 50 * (1+active['开发']['指技']*1)
        pm['苦痛'] += 40 * 2^(-active['开发']['指技']*1)
        pm['恭顺'] += 45 * (1+active['开发']['指技']*1)
        am['习得'] += 5
        pm['反感'] += 20
        pe['A经验'] += 1 * (1+active['开发']['指技']*1)
        pm['好感度'] += 1 * (1+active['开发']['指技']*1)
        ae['指技经验'] += 1 * (1+active['开发']['指技']*1)
        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,25,10])
        comkojo(active,passive,6,{'com':'doing'})
        f = True
        
    else:
        if  obey_check(10,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 6
            append_doing_list(active,passive,6)
            comkojo(active,passive,6,{'com':'add'})
        else:
            pm['反感'] += 100
            pm['好感度'] += -10
            comkojo(active,passive,6,{'com':'fail'})
    return f

def undocom6(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],6])
    comkojo(active,passive,6,{'com':'undo'})
    active['标志']['手占用'] = 0
    del passive['身体信息']['肛门']['内容固体'][active['名字']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False