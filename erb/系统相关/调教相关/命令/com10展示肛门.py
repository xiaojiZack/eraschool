import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 10
def com10(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['露出','A']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False#记录本指令是否执行成功

    if check_doing_list(active,passive,10):
        pm['快A'] += 10 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 350 * (1+active['开发']['指技']*1)
        pm['欲情'] += 150 * (1+active['开发']['指技']*1)
        pm['恭顺'] += 400
        pm['屈服'] += 500
        pm['反感'] += 10
        pe['露出经验'] += 1
        pm['好感度'] += 0
        sum_pp(active,[0,10,0])
        sum_pp(passive,[0,90,20])
        comkojo(active,passive,10,{'com':'doing'})

        f = True
        
    else:
        if obey_check(15,active,passive,com_trait):
            append_doing_list(active,passive,10)
            comkojo(active,passive,10,{'com':'add'})
        else:
            pm['反感'] += 50
            pm['好感度'] += -5
            comkojo(active,passive,10,{'com':'fail'})
    
    return f
def undocom10(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],10])
    comkojo(active,passive,10,{'com':'undo'})
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()