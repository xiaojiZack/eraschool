import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

#爱抚
def com3(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A','疼痛','污臭']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False

    if check_doing_list(active,passive,3):
        pm['快A'] += 5 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 10 * (1+active['开发']['指技']*1)
        pm['欲情'] += 5 * (1+active['开发']['指技']*1)
        pm['习得'] += 5 * (1+active['开发']['指技']*1)
        am['习得'] += 5
        pm['反感'] += 15
        pe['A经验'] += 1
        ae['指技经验'] += 1
        a.t('{}的手在{}身上轻柔抚摸'.format(aname,pname),True)
        a.t()
        pm['好感度'] += 1

        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,25,20])

        f = True
    else:
        if obey_check(10,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['手占用'] = 3
            append_doing_list(active,passive,3)
        else:
            pm['反感'] += 50
            pm['好感度'] += -5

        f = False

    return f

def undocom3(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],3])
    active['标志']['手占用'] = 0
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()