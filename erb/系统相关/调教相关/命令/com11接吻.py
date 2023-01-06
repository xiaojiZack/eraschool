import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 11
def com11(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['M','贞操']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False#记录本指令是否执行成功

    if check_doing_list(active,passive,11):
        pm['快M'] += 25 * (1+active['开发']['舌技']*1)
        pm['羞耻'] += 400 * (1+active['开发']['舌技']*1)
        pm['欲情'] += 500 * (1+active['开发']['舌技']*1)
        pm['恭顺'] += 400 * (1+active['开发']['舌技']*1)
        pm['主导'] += 500 
        pm['习得'] += 400 * (1+active['开发']['舌技']*1)
        am['习得'] += 10
        pm['反感'] += 50
        pe['M经验'] += 1 * (1+active['开发']['舌技']*1)
        pe['亲吻经验'] += 1
        ae['亲吻经验'] += 1
        ae['爱情经验'] += 1
        pe['爱情经验'] += 1
        ae['舌技经验'] += 1
        pe['舌技经验'] += 1 * (1+active['开发']['舌技']*1)
        pm['好感度'] += 1
        comkojo(active,passive,11,{'com':'doing'})
        sum_pp(active,[0,20,0])
        sum_pp(passive,[0,30,10])

        f = True
        
    else:
        if obey_check(20,active,passive,com_trait):
            active['标志']['口占用'] = 11
            passive['标志']['口占用'] = 11
            append_doing_list(active,passive,11)
            comkojo(active,passive,11,{'com':'add'})
        else:
            comkojo(active,passive,11,{'com':'fail'})
            pm['反感'] += 60
            pm['好感度'] += -5
    
    return f
def undocom11(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],11])
    comkojo(active,passive,11,{'com':'undo'})
    active['标志']['口占用'] = 0
    passive['标志']['口占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()