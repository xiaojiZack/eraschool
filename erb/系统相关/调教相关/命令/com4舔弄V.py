import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

#爱抚
comid = 4
def com4(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['C']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    f = False

    if check_doing_list(active,passive,4):
        pm['快C'] += 25 * (1+active['开发']['舌技']*1)
        pm['V润'] += 20
        pm['羞耻'] += 150 * (1+active['开发']['舌技']*1)
        pm['欲情'] += 100 * (1+active['开发']['舌技']*1)
        pm['习得'] += 10 * (1+active['开发']['舌技']*1)
        pm['恭顺'] += 15 * (1+active['开发']['舌技']*1)
        am['习得'] += 10
        am['屈服'] += 10
        pm['反感'] += 25
        pe['C经验'] += 1
        ae['舌技经验'] += 1
        a.t()
        pm['好感度'] += 1
        am['侍奉快乐'] += 1

        sum_pp(active,[0,15,0])
        sum_pp(passive,[0,25,10])
        comkojo(active,passive,4,{'com':'doing'})
        f = True
        
    else:
        if obey_check(1,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['口占用'] = 4
            append_doing_list(active,passive,4)
            comkojo(active,passive,4,{'com':'add'})
        else:
            pm['反感'] += 25
            pm['好感度'] += -5
            f = False
            comkojo(active,passive,4,{'com':'fail'})
        
    return f

def undocom4(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],4])
    comkojo(active,passive,4,{'com':'undo'})
    active['标志']['口占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False