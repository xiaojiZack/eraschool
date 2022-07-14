import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list, remove_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 71
def com71(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['精液','脏污','主导']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    f = False
    if check_doing_list(active,passive,71):
        pm['羞耻'] += 5 * (1+passive['开发']['指技']*1)
        pm['屈服'] += 5 * (1+passive['开发']['指技']*1)
        pm['主导'] += 30 * (1+passive['开发']['指技']*1)
        pm['习得'] += 10 * (1+passive['开发']['指技']*1)
        pm['快C'] += 5
        am['习得'] += 5
        pm['反感'] += 10


        a.t('{}的手在{}身上轻柔抚摸'.format(aname,pname),True)
        a.t()
        pm['好感度'] += 1
        pm['侍奉快乐'] += 1

        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,10,5])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
    else:
        if obey_check(25,active,passive,com_trait):
            #此处可能需要处理替换的问题
            passive['标志']['手占用'] = 71
            active['标志']['阴茎占用'] = 71
            active['身体信息']['阴茎']['插入位置'][passive['CharacterId']] = '足'
            append_doing_list(active,passive,71)
            comkojo(active,passive,comid,{'com':'add'})
            f = True
        else:
            pm['反感'] += 10
            pm['好感度'] += -5
            comkojo(active,passive,comid,{'com':'fail'})
            f = False
    
    a.tmp()['执行结果'] = f

def undocom71(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],71])
    passive['标志']['手占用'] = 0
    active['标志']['阴茎占用'] = 0
    del active['身体信息']['阴茎']['插入位置'][passive['CharacterId']]
    comkojo(active,passive,comid,{'com':'undo'})
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()