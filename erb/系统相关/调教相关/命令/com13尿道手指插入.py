import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.插入尺寸计算 import check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

def com13(active,passive):
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['U']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    
    flag = check_size(passive['开发']['尿道扩张度'],'手指',passive['身体信息']['尿道']['内容固体'])
    if flag == False:
        com_trait.append('尺寸过大')
        com_trait.append('疼痛')
    
    oil_flag = is_enough_oiling(passive,'V',1)
    if oil_flag >0:
        com_trait.append('润滑不足')
    
    if (flag or a.tmp()['调教数据']['尺寸警告标志'] == False):
        if check_doing_list(active,passive,13):
            
            if oil_flag >0:
                not_oiling_punish(passive,oil_flag)
            pm['快U'] += 10 * (1+active['开发']['指技']*1)

            pm['羞耻'] += 10 * (1+active['开发']['指技']*1)
            pm['欲情'] += 5 * (1+active['开发']['指技']*1)
            pm['习得'] += 5 * (1+active['开发']['指技']*1)
            pm['恐怖'] += 100 *2^(-active['开发']['指技']*1)
            pm['苦痛'] += 50
            am['习得'] += 5
            pm['反感'] += 50

            ae['指技经验'] += 1
            pe['U经验'] += 1 * (1+active['开发']['指技']*1)
            pm['好感度'] += 1 * (1+active['开发']['指技']*1)
            sum_pp(active,[0,10,5])
            sum_pp(passive,[0,25,20])
            if flag == False:
                size_punish(passive)
            f = True
                        
        else:
            if  obey_check(60,active,passive,com_trait):
                #此处可能需要处理替换的问题
                active['标志']['手占用'] = 13
                append_doing_list(active,passive,13)
                passive['身体信息']['尿道']['内容固体'][active['名字']] = '手指'
            else:
                pm['反感'] += 50
                pm['好感度'] += -15
    
        
    return f

def undocom13(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],13])
    active['标志']['手占用'] = 0
    del passive['身体信息']['尿道']['内容固体'][active['名字']]
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False