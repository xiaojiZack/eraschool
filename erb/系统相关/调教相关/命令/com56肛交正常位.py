import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.处女 import check_pure, pure_punish
from erb.系统相关.调教相关.插入 import insert, insert_check
from erb.系统相关.调教相关.插入尺寸计算 import check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish, oiling_buff
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 56
def com56(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A','苦痛','中出','精液']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    obey_challenge = 35
    
    check_result = insert_check(active,passive,'P','A',com_trait)
    if check_doing_list(active,passive,56) and check_result!=False:
        insert(active,passive,'P','A',check_result)
                                
        pm['快A'] += 100 * (1+active['开发']['腰技']*1)
        pm['苦痛'] += 450 * (1-active['开发']['腰技']*0.1)
        pm['恐惧'] += 550 * (1-active['开发']['腰技']*0.1)
        pm['屈服'] += 500 * (1+active['开发']['腰技']*1)
        pm['羞耻'] += 450 * (1+active['开发']['腰技']*1)
        pm['欲情'] += 250 * (1+active['开发']['腰技']*1)
        pm['恭顺'] += 250 * (1+active['开发']['腰技']*1)
        pm['习得'] += 50 * (1+active['开发']['腰技']*1)
        pm['反感'] += 60
        pe['C经验'] += 1 * (1+active['开发']['腰技']*1)
        pe['A经验'] += 1 * (1+active['开发']['腰技']*1)
        pe['A性交经验'] += 1 * (1+active['开发']['腰技']*1)
        pm['好感度'] += 1 * (1+active['开发']['腰技']*1)
        
        am['快C'] += ((1+passive['开发']['A名器度'])*200)*(1+passive['开发']['腰技']*1)
        am['欲情'] += 100 * (1+active['开发']['腰技']*1)
        am['习得'] += 5*(1+passive['开发']['腰技']*1)
        am['主导'] += 5*(1+passive['开发']['腰技']*1)
        ae['腰技经验'] += 1
        ae['A插入经验'] += 1
        pe['腰技经验'] += 1

        am['快C'] = oiling_buff(passive, 'A')*am['快C']
        pm['快A'] = oiling_buff(passive, 'A')*pm['快A']
        
        sum_pp(active,[0,100,5])
        sum_pp(passive,[0,350,35])
        comkojo(active,passive,comid,{'com':'doing'})
        f = True
        
    else:
        if check_result!=False:
            if  obey_check(obey_challenge,active,passive,com_trait):
                #此处可能需要处理替换的问题
                active['标志']['阴茎占用'] = comid
                append_doing_list(active,passive,comid)
                comkojo(active,passive,comid,{'com':'add'})
                
            else:
                pm['反感'] += 50
                pm['好感度'] += -5
                comkojo(active,passive,comid,{'com':'fail'})
        
    return f

def undocom56(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],56])
    comkojo(active,passive,comid,{'com':'undo'})
    active['标志']['阴茎占用'] = 0
    del passive['身体信息']['肛门']['内容固体'][active['名字']]
    del active['身体信息']['阴茎']['插入位置'][passive['CharacterId']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False