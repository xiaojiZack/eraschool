import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

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
        pm['羞耻'] += 10 * (1+active['开发']['舌技']*1)
        pm['欲情'] += 20 * (1+active['开发']['舌技']*1)
        pm['主导'] += 10 
        pm['习得'] += 10 * (1+active['开发']['舌技']*1)
        am['习得'] += 10
        pm['反感'] += 10
        pe['M经验'] += 1 * (1+active['开发']['舌技']*1)
        pe['亲吻经验'] += 1
        ae['亲吻经验'] += 1
        ae['爱情经验'] += 1
        pe['爱情经验'] += 1
        ae['舌技经验'] += 1
        pe['舌技经验'] += 1 * (1+active['开发']['舌技']*1)
       
        pm['好感度'] += 1
        
        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,20,10])

        f = True
        
    else:
        if obey_check(20,active,passive,com_trait):
            active['标志']['口占用'] = 11
            passive['标志']['口占用'] = 11
            append_doing_list(active,passive,11)
        else:
            a.t('{}架开了{}的咸猪手'.format(pname,aname),True)
            a.t()
            pm['反感'] += 40
            pm['好感度'] += -5
    
    return f
def undocom11(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],11])
    active['标志']['口占用'] = 0
    passive['标志']['口占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()