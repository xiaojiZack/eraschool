import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list, remove_doing_list
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 70
def com70(active,passive):

    aname = active['名字']
    pname = passive['名字']
    com_trait = ['精液','脏污','主导','C']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    f = False
    if check_doing_list(active,passive,70):
        am['快C'] += 5 * (1+passive['开发']['腰技']*1)
        pm['羞耻'] += 5 * (1+passive['开发']['腰技']*1)
        pm['屈服'] += 10 * (1+passive['开发']['腰技']*1)
        pm['主导'] += 20 * (1+passive['开发']['腰技']*1)
        pm['习得'] += 10 * (1+passive['开发']['腰技']*1)
        pm['快C'] += 5
        am['习得'] += 5
        pm['反感'] += 10
        pe['腰技经验'] += 1

        a.t('{}的手在{}身上轻柔抚摸'.format(aname,pname),True)
        a.t()
        pm['好感度'] += 1
        pm['侍奉快乐'] += 1

        sum_pp(active,[0,10,5])
        sum_pp(passive,[0,20,10])
        comkojo(active,passive,comid,{'com':'doing'})
        
        f = True
    else:
        if obey_check(15,active,passive,com_trait):
            #此处可能需要处理替换的问题
            passive['标志']['手占用'] = 70
            active['标志']['阴茎占用'] = 70
            active['身体信息']['阴茎']['插入位置'][passive['CharacterId']] = '股间'
            append_doing_list(active,passive,70)
            comkojo(active,passive,comid,{'com':'add'})
            f = True
        else:
            pm['反感'] += 10
            pm['好感度'] += -5
            f = False
            comkojo(active,passive,comid,{'com':'fail'})
    
    a.tmp()['执行结果'] = f

def undocom70(active,passive):
    a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],70])
    passive['标志']['手占用'] = 0
    active['标志']['阴茎占用'] = 0
    del active['身体信息']['阴茎']['插入位置'][passive['CharacterId']]
    comkojo(active,passive,comid,{'com':'undo'})
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False
    #a.t()