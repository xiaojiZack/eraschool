import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

comid = 8
def com8(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['C']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False

    if check_doing_list(active,passive,8):
        pm['快C'] += 20 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 200 * (1+active['开发']['指技']*1)
        pm['欲情'] += 200 * (1+active['开发']['指技']*1)
        pm['习得'] += 50 * (1+active['开发']['指技']*1)
        pm['恭顺'] += 100
        am['习得'] += 80
        pm['反感'] += 10
        pe['C经验'] += 1
        ae['指技经验'] += 1
        pm['好感度'] += 1
        
        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,20,10])
        comkojo(active,passive,8,{'com':'doing'})
        f = True
        
    else:
        if obey_check(5,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 8
            append_doing_list(active,passive,8)
            comkojo(active,passive,8,{'com':'add'})

        else:
            pm['反感'] += 30
            pm['好感度'] += -5
            comkojo(active,passive,8,{'com':'fail'})

        f = False

    return f

def undocom8(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],8])
    comkojo(active,passive,8,{'com':'undo'})
    active['标志']['手占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()