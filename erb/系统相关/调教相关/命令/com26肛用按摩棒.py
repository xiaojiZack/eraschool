import time
from tkinter.ttk import Style
import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.处女 import check_pure, pure_punish
from erb.系统相关.调教相关.插入尺寸计算 import P_size_trans, check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oiling_punish
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq
comid = 26
def com26(active,passive):
    #成功判定
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['A']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']
    decrease_a = []#主导者体、气、智消耗
    decrease_p = []
    favor = []
    f = False
    size = ''

    if not check_equipment(passive,26):
        a.tmp()['暂停'] = True
        select_size(passive)
        while a.tmp()['暂停']: time.sleep(0.1)
        size = a.tmp()['按摩棒选择']
    else:
        size = passive['身体信息']['肛门']['内容固体']['按摩棒']

    pure_flag = check_pure(passive,'A')

    if not check_equipment(passive,26):
        size_flag = check_size(passive['开发']['A扩张度'],size,passive['身体信息']['肛门']['内容固体'])
    else: size_flag = check_maintain_size(passive['开发']['A扩张度'],passive['身体信息']['肛门']['内容固体'])

    if size_flag == False:
        com_trait.append('尺寸过大')
        com_trait.append('疼痛')
    
    oilneed = 3
    if size_flag == False: oilneed = 4
    else: oilneed = 3
    oil_flag = is_enough_oiling(passive,'A',oilneed)
    if oil_flag >0:
        com_trait.append('润滑不足')
    
    if (size_flag or a.tmp()['调教数据']['尺寸警告标志'] == False):
        if check_equipment(passive,26):
            if oil_flag >0:
                not_oiling_punish(passive,oil_flag)
            if size_flag == False:
                size_punish(passive)
                pe['A扩张经验'] += 1
                        
            pm['快A'] += 30 
            pm['欲情'] += 5 
            pm['屈服'] += 10
            pm['羞耻'] += 20
            pm['反感'] += 20
            pe['A经验'] += 1
            pm['好感度'] += 1
            sum_pp(passive,[0,30,20])
            comkojo(active,passive,26,{'com':'doing'})
            
            f = True
            
        else: 
            if  obey_check(25,active,passive,com_trait):
                #此处可能需要处理替换的问题
                append_doing_list(active,passive,26)
                comkojo(active,passive,26,{'com':'add'})
                passive['身体信息']['肛门']['内容固体']['按摩棒'] = size
                if pure_flag == False:
                    pure_punish(passive,'A')
                    passive['属性']['体质'].remove('A处女')
                    a.tmp()['特殊事件'].append(['A处女丧失','{}'.format(passive['名字'])])


            else:
                pm['反感'] += 30
                pm['好感度'] += -3
                comkojo(active,passive,26,{'com':'fail'})
        
    return f

def undocom26(active,passive):
    remove_equipment(passive,26)
    comkojo(active,passive,26,{'com':'undo'})
    del passive['身体信息']['肛门']['内容固体']['按摩棒']
    #a.t()
    if a.tmp()['去冲突标志'] == False:
        a.repeat()
    else:
        a.tmp()['去冲突标志'] = False

def select_size(passive):
    def get_select(size):
        a.tmp()['按摩棒选择'] = size
        a.tmp()['暂停'] = False
    a.page()
    a.mode()
    a.tmp()['按摩棒选择'] = ''
    a.h('要使用哪种尺寸的按摩棒呢？')
    a.t('{}的A扩张度为:{}'.format(passive['名字'],passive['开发']['A扩张度']))
    a.t()
    if passive['开发']['A扩张度']<4:
        a.b('普通按摩棒',get_select,'普通根',style = {'color':'#f00'})
    else:
        a.b('普通按摩棒',get_select,'普通根')
    a.t()
    if passive['开发']['A扩张度']<6:
        a.b('巨根按摩棒',get_select,'巨根',style = {'color':'#f00'})
    else:
        a.b('巨根按摩棒',get_select,'巨根')
    
    a.t()
    if passive['开发']['A扩张度']<8:
        a.b('拳交按摩棒',get_select,'手臂尺寸',style = {'color':'#f00'})
    else:
        a.b('拳交按摩棒',get_select,'手臂尺寸')
    a.t()
    if passive['开发']['A扩张度']<9:
        a.b('马根按摩棒',get_select,'马根',style = {'color':'#f00'})
    else:
        a.b('马根按摩棒',get_select,'马根')
    
def remove_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            a.tmp()['执行列表'].remove(i)

def check_equipment(c,com):
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[1] and com == i[2]:
            return True
    return False