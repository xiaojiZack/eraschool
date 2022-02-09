import erajs.api as a
from .com1爱抚 import com1, undocom1
from .com2胸爱抚 import com2, undocom2
from .com3肛门爱抚 import com3, undocom3
from .com4舔弄V import com4, undocom4
from .com5手指插入V import com5, undocom5

com_number = 5
com_dict = {1:'爱抚',2:'胸爱抚',3:'肛门爱抚',4:'舔弄V',5:'手指插入'}

def c1(active,passive):
    conflict_com = [2,3,5]
    def execcom1(active,passive):
        remove_com_conflict(active,passive,conflict_com)
        com1(active,passive)
    if check_doing_list(active,passive,1):
        a.b('中止爱抚',undocom1,active,passive, style = {'color':'#ff0'})
    else:
        a.b('爱抚',execcom1,active,passive)

def c2(active,passive):
    conflict_com = [1,3,4,5]
    def execcom2(active,passive):
        remove_com_conflict(active,passive,conflict_com)
        com2(active,passive)
    if check_doing_list(active,passive,2):
        a.b('中止爱抚',undocom2,active,passive, style = {'color':'#ff0'})
    else:
        a.b('胸爱抚',execcom2,active,passive)

def c3(active,passive):
    conflict_com = [1,2,5]
    def execcom3(active,passive):
        remove_com_conflict(active,passive,conflict_com)
        com3(active,passive)
    if check_doing_list(active,passive,3):
        a.b('中止爱抚',undocom3,active,passive, style = {'color':'#ff0'})
    else:
        a.b('肛门爱抚',execcom3,active,passive)

def c4(active,passive):
    conflict_com = [2]
    def execcom4(active,passive):
        remove_com_conflict(active,passive,conflict_com)
        com4(active,passive)
    if check_doing_list(active,passive,4):
        a.b('中止舔弄',undocom4,active,passive, style = {'color':'#ff0'})
    else:
        a.b('舔弄',execcom4,active,passive)

def c5(active,passive):
    conflict_com = [1,2,3]
    def execcom5(active,passive):
        remove_com_conflict(active,passive,conflict_com)
        com5(active,passive)
    if check_doing_list(active,passive,5):
        a.b('拔出手指',undocom5,active,passive, style = {'color':'#ff0'})
    else:
        a.b('手指插入V',execcom5,active,passive)



#_________________________________________________________________________________

def check_insert(active,passive,body_part):
    if active['名字'] in passive['身体信息'][body_part]['内容固体'].keys():
        return True
    return False

def remove_insert(active,passive,body_part):
    if check_insert(active,passive,body_part):
        del passive['身体信息'][body_part]['内容固体'][active['名字']]
        return True
    else:
        return False

def check_doing_list(active,passive,com):
    t = a.tmp()['执行列表']
    if [active['CharacterId'],passive['CharacterId'],com] in a.tmp()['执行列表']:
        return True
    else: return False

def remove_doing_list(active,passive,com):
    if check_doing_list(active,passive,com):
        a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],com])
    else:
        return False

def check_conflict_list(active,passive,conflict_list):
    for i in a.tmp()['执行列表']:
        if active['CharacterId'] == i[0] and passive['CharacterId'] == i[1]:
            if i[2] in conflict_list:
                return [active['CharacterId'],passive['CharacterId'],i[2]]
    return False

def remove_com_conflict(active,passive,conflict_list):
    while (check_conflict_list(active,passive,conflict_list)) != False:
        conflict_com = check_conflict_list(active,passive,conflict_list)
        active = find_people(conflict_com[0])
        passive = find_people(conflict_com[1])
        exec('undocom{}(active,passive)'.format(conflict_com[2]))
    
def find_people(CharacterId):
    for i in a.tmp()['调教数据']['参与者']:
        if i['CharacterId'] == CharacterId:
            return i
    return False

def updata_state():
    for i in a.tmp()['执行列表']:
        active = find_people(i[0])
        passive = find_people(i[1])
        com = com_dict[i[2]]
        if not [com,active['名字']] in passive['调教状态']:
            passive['调教状态'].append([com,active['名字']])
