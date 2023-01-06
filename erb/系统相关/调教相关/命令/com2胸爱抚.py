import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 2
def com2(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['B']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False#记录本指令是否执行成功

    if check_doing_list(active,passive,2):
        pm['快B'] += 20 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 20 * (1+active['开发']['指技']*1)
        pm['欲情'] += 20 * (1+active['开发']['指技']*1)
        pm['习得'] += 5 * (1+active['开发']['指技']*1)
        pm['恭顺'] += 10 * (1+active['开发']['指技']*1)
        am['习得'] += 5
        pm['反感'] += 10
        ae['指技经验'] += 1
        pe['B经验'] += 1
        pm['好感度'] += 1
        comkojo(active,passive,2,{'com':'doing'})
        
        sum_pp(active,[0,10,0])
        sum_pp(passive,[0,20,10])


        f = True
        
    else:
        if obey_check(0,active,passive,com_trait):
            active['标志']['手占用'] = 2
            append_doing_list(active,passive,2)
            comkojo(active,passive,2,{'com':'add'})
        else:
            comkojo(active,passive,2,{'com':'fail'})
            pm['反感'] += 20
            pm['好感度'] += -5
    
    return f
def undocom2(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],2])
    comkojo(active,passive,2,{'com':'undo'})
    active['标志']['手占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()