import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.处女 import check_pure, pure_punish
from erb.系统相关.调教相关.插入 import insert, insert_check
from erb.系统相关.调教相关.插入尺寸计算 import check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 64
def com64(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['V','W', '苦痛','中出','精液']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    check_result = insert_check(active,passive,'P','A',com_trait)
    if check_doing_list(active,passive,comid) and check_result!=False:
        insert(active,passive,'P','V',check_result)
                                
        pm['快W'] += 25 * (1+active['开发']['腰技']*1)
        pm['苦痛'] += 400 * (1+active['开发']['腰技']*1)
        pm['屈服'] += 600 * (1+active['开发']['腰技']*1)
        pm['羞耻'] += 300 * (1+active['开发']['腰技']*1)
        pm['欲情'] += 700 * (1+active['开发']['腰技']*1)
        pm['恭顺'] += 500 * (1+active['开发']['腰技']*1)
        pm['习得'] += 50 * (1+active['开发']['腰技']*1)
        pm['反感'] += 60
        pe['子宫经验'] += 1 * (1+active['开发']['腰技']*1)
        pe['子宫姦经验'] += 1
        
        am['欲情'] += 10 * (1+active['开发']['腰技']*1)
        am['习得'] += 5*(1+passive['开发']['腰技']*1)
        am['主导'] += 5*(1+passive['开发']['腰技']*1)
        ae['子宫插入经验'] += 1

        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,20,20])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
        
    else:
        if  obey_check(35,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['阴茎占用'] = comid
            append_doing_list(active,passive,comid)
            comkojo(active,passive,comid,{'com':'add'})
            
        else:
            pm['反感'] += 50
            pm['好感度'] += -5
            comkojo(active,passive,comid,{'com':'fail'})
        
    return f

def undocom57(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],comid])
    comkojo(active,passive,comid,{'com':'undo'})
    active['标志']['阴茎占用'] = 0
    del passive['身体信息']['肛门']['内容固体'][active['名字']]
    del active['身体信息']['阴茎']['插入位置'][passive['CharacterId']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False