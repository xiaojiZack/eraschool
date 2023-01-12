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
comid = 54
def com54(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['V','处女破坏','中出','精液']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    check_result = insert_check(active,passive,'P','V',com_trait)
    if check_doing_list(active,passive,54) and check_result!=False:
        insert(active,passive,'P','V',check_result)
                                
        pm['快V'] += 25 * (1+active['开发']['腰技']*1)
        pm['快B'] += 25 * (1+active['开发']['指技']*1)
        pm['快C'] += 25 * (1+active['开发']['指技']*1)
        pm['羞耻'] += 150 * (1+active['开发']['腰技']*1)
        pm['屈服'] += 250 * (1+active['开发']['腰技']*1)
        pm['欲情'] += 150 * (1+active['开发']['腰技']*1)
        pm['恭顺'] += 450 * (1+active['开发']['腰技']*1)
        pm['恐惧'] += 50 * (1+active['开发']['腰技']*1)
        pm['习得'] += 50 * (1+active['开发']['腰技']*1)
        pm['反感'] += 10
        pe['V经验'] += 1 * (1+active['开发']['腰技']*1)
        pe['V性交经验'] += 1 * (1+active['开发']['腰技']*1)
        pe['B经验'] += 1 * (1+active['开发']['指技']*1)
        pe['C经验'] += 1 * (1+active['开发']['指技']*1)
        pm['好感度'] += 2 * (1+active['开发']['腰技']*1)
        
        am['快C'] += ((1+passive['开发']['V名器度'])*250)*(1+passive['开发']['腰技']*1)
        am['欲情'] += 100 * (1+active['开发']['腰技']*1)
        am['习得'] += 5*(1+passive['开发']['腰技']*1)
        am['主导'] += 10*(1+passive['开发']['腰技']*1)
        ae['腰技经验'] += 1
        pe['腰技经验'] += 1
        ae['V插入经验'] += 1

        am['快C'] = oiling_buff(passive, 'V')*am['快C']
        pm['快V'] = oiling_buff(passive, 'V')*pm['快V']
        
        sum_pp(active,[0,100,5])
        sum_pp(passive,[0,200,20])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
        
    else:
        if  obey_check(35,active,passive,com_trait):
            #此处可能需要处理替换的问题
            active['标志']['阴茎占用'] = 54
            append_doing_list(active,passive,54)
            comkojo(active,passive,comid,{'com':'add'})
            
        else:
            pm['反感'] += 50
            pm['好感度'] += -5
            comkojo(active,passive,comid,{'com':'fail'})
        
    return f

def undocom54(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],54])
    comkojo(active,passive,comid,{'com':'undo'})
    active['标志']['阴茎占用'] = 0
    del passive['身体信息']['阴道']['内容固体'][active['名字']]
    del active['身体信息']['阴茎']['插入位置'][passive['CharacterId']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False