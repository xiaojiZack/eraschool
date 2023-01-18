import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

#爱抚
comid = 7
def com7(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    f = False

    if check_doing_list(active,passive,7):
        pm['快A'] += 20 * (1+active['开发']['舌技']*1)
        pm['A润'] += 20
        pm['羞耻'] += 100 * (1+active['开发']['舌技']*1)
        pm['欲情'] += 50 * (1+active['开发']['舌技']*1)
        pm['屈服'] += 250 * (1+active['开发']['舌技']*1)
        pm['习得'] += 5 * (1+active['开发']['舌技']*1)
        pm['恭顺'] += 45 * (1+active['开发']['舌技']*1)
        am['习得'] += 5
        am['屈服'] += 5
        pm['反感'] += 25
        pe['A经验'] += 1
        ae['舌技经验'] += 1
        a.t()
        pm['好感度'] += 1
        am['侍奉快乐'] += 1

        sum_pp(active,[0,10,15])
        sum_pp(passive,[0,70,10])
        comkojo(active,passive,7,{'com':'doing'})
        f = True
        
    else:
        if obey_check(5,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['口占用'] = 7
            append_doing_list(active,passive,7)
            comkojo(active,passive,7,{'com':'add'})
        else:
            pm['反感'] += 30
            pm['好感度'] += -5
            f = False
            comkojo(active,passive,7,{'com':'fail'})
    return f

def undocom7(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],7])
    comkojo(active,passive,7,{'com':'undo'})
    active['标志']['口占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False