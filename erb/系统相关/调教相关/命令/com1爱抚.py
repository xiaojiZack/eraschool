import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list, remove_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

#爱抚
comid = 1
def com1(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['B','C']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    f = False
    if check_doing_list(active,passive,1):
        pm['快C'] += 5 * (1+active['开发']['指技']*1)
        pm['快B'] += 5 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 20 * (1+active['开发']['指技']*1)
        pm['欲情'] += 20 * (1+active['开发']['指技']*1)
        pm['习得'] += 5 * (1+active['开发']['指技']*1)
        pm['恭顺'] += 20 * (1+active['开发']['指技']*1)
        
        am['习得'] += 5
        pm['反感'] += 10
        ae['指技经验'] += 1
        pe['C经验'] += 1
        pe['B经验'] += 1
        comkojo(active,passive,1,{'com':'doing'})
        a.t()
        pm['好感度'] += 1

        sum_pp(active,[0,10,0])
        sum_pp(passive,[0,90,10])
        
        f = True
    else:
        if obey_check(-20,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 1
            append_doing_list(active,passive,1)
            comkojo(active,passive,1,{'com':'add'})
            f = True
        else:
            comkojo(active,passive,1,{'com':'fail'})
            pm['反感'] += 20
            pm['好感度'] += -5
            f = False
    
    a.tmp()['执行结果'] = f

def undocom1(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],1])
    active['标志']['手占用'] = 0
    comkojo(active,passive,1,{'com':'undo'})
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()