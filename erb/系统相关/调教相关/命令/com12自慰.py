import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 12
def com12(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['B','C','露出']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False#记录本指令是否执行成功

    if check_doing_list(active,passive,12):
        pm['快B'] += 35 * (1+passive['开发']['指技']*1)
        pm['快C'] += 40 * (1+passive['开发']['指技']*1)
        pm['羞耻'] += 500 
        pm['欲情'] += 800 * (1+passive['开发']['指技']*1)
        pm['主导'] += 500 
        pm['习得'] += 500 * (1+passive['开发']['指技']*1)
        pm['屈服'] += 600 * (1+passive['开发']['指技']*1)
        pm['恭顺'] += 200 * (1+passive['开发']['指技']*1)
        am['习得'] += 100
        pm['反感'] += 10
        pe['自慰经验'] += 1
        pe['B经验'] += 1
        pe['C经验'] += 1
        pe['自慰经验'] += 1
        pe['露出经验'] += 1
        pe['指技经验'] += 1

        pm['好感度'] += 1
        comkojo(active,passive,12,{'com':'doing'})
        sum_pp(passive,[0,40,15])

        f = True
        
    else:
        if obey_check(30,active,passive,com_trait):
            passive['标志']['手占用'] = 12
            append_doing_list(active,passive,12)
            comkojo(active,passive,12,{'com':'add'})
        else:
            comkojo(active,passive,12,{'com':'fail'})
            pm['反感'] += 40
            pm['好感度'] += -5
    
    return f
def undocom12(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],12])
    passive['标志']['手占用'] = 12
    comkojo(active,passive,12,{'com':'undo'})
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()