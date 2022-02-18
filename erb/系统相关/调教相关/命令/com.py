import erajs.api as a
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list
from erb.系统相关.调教相关.绝顶 import main_orgasm
from .com1爱抚 import com1, undocom1
from .com2胸爱抚 import com2, undocom2
from .com3肛门爱抚 import com3, undocom3
from .com4舔弄V import com4, undocom4
from .com5手指插入V import com5, undocom5
from .com6手指插入A import com6, undocom6
from .com7舔弄肛门 import com7, undocom7
from .com8阴部爱抚 import com8, undocom8
from .com9展示阴道 import com9, undocom9
from .com10展示肛门 import com10, undocom10
from .com11接吻 import com11,undocom11
from .com12自慰 import com12,undocom12
from .com13尿道手指插入 import com13,undocom13
from .com21跳蛋 import com21, undocom21
from .com22跳蛋插入 import com22,undocom22
from .com23跳蛋肛门插入 import com23,undocom23
from .com24电动按摩器 import com24,undocom24
from .com25按摩棒 import com25,undocom25
from .com26肛用按摩棒 import com26,undocom26
from .com27阴蒂夹 import com27,undocom27
from .com28乳头夹 import com28,undocom28
from .com29飞机杯 import com29,undocom29
from .com30榨乳机 import com30,undocom30
from .com31绳缚 import com31,undocom31

com_number = 5
com_dict = {
    1:'爱抚',2:'胸爱抚',3:'肛门爱抚',4:'舔弄V',5:'手指插入',
    6:'手指插入A',7:'舔弄肛门',8:'阴部爱抚',9:'展示阴道',10:'展示肛门',
    11:'接吻',12:'自慰',13:'尿道手指插入',21:'跳蛋',22:'跳蛋插入',
    23:'跳蛋肛门插入',24:'电动按摩棒',25:'V按摩棒',26:'肛用按摩棒',
    27:'阴蒂夹',28:'乳头夹',29:'飞机杯',30:'榨乳机',31:'绳缚',
    }

def c1(active,passive):
    if check_doing_list(active,passive,1):
        a.b('结束爱抚',undocom1,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,1):
        a.b('爱抚',execcom1,active,passive)
def execcom1(active,passive):
    conflict_com = [2,3,5]
    remove_com_conflict(active,passive,conflict_com)
    com1(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c2(active,passive):
    if check_doing_list(active,passive,2):
        a.b('结束胸爱抚',undocom2,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,2):
        a.b('胸爱抚',execcom2,active,passive)
def execcom2(active,passive):
    conflict_com = [1,3,4,5]
    remove_com_conflict(active,passive,conflict_com)
    com2(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c3(active,passive):
    if check_doing_list(active,passive,3):
        a.b('结束肛门爱抚',undocom3,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,3):
        a.b('肛门爱抚',execcom3,active,passive)
def execcom3(active,passive):
    conflict_com = [1,2,5]
    remove_com_conflict(active,passive,conflict_com)
    com3(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c4(active,passive):
    if check_doing_list(active,passive,4):
        a.b('结束舔弄',undocom4,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,4):
        a.b('舔弄V',execcom4,active,passive)
def execcom4(active,passive):
    remove_body_type_occupy(active,'口占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com4(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c5(active,passive):
    if check_doing_list(active,passive,5):
        a.b('拔出手指',undocom5,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,5):
        if passive['性别'] == '女性':
            a.b('手指插入V',execcom5,active,passive)
def execcom5(active,passive):
    conflict_com = [1,2,3,6]
    remove_com_conflict(active,passive,conflict_com)
    com5(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c6(active,passive):
    if check_doing_list(active,passive,6):
        a.b('拔出手指',undocom6,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,6):
        a.b('手指插入A',execcom6,active,passive)
def execcom6(active,passive):
    conflict_com = [1,2,3,5]
    remove_com_conflict(active,passive,conflict_com)
    com6(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c7(active,passive):
    if check_doing_list(active,passive,7):
        a.b('结束舔弄',undocom7,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,7):
        a.b('舔弄肛门',execcom7,active,passive)
def execcom7(active,passive):
    conflict_com = [active['标志']['口占用']]
    remove_com_conflict(active,passive,conflict_com)
    com7(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c8(active,passive):
    if check_doing_list(active,passive,8):
        a.b('中止阴部爱抚',undocom8,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,8):
        a.b('阴部爱抚',execcom8,active,passive)
def execcom8(active,passive):
    remove_body_type_occupy(active,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com8(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c9(active,passive):
    if check_doing_list(active,passive,9):
        a.b('放开阴道',undocom9,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,9):
        a.b('展示阴道',execcom9,active,passive)
def execcom9(active,passive):
    remove_body_type_occupy(active,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com9(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c10(active,passive):
    if check_doing_list(active,passive,10):
        a.b('放开屁股',undocom10,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,10):
        a.b('展示肛门',execcom10,active,passive)
def execcom10(active,passive):
    remove_body_type_occupy(active,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com10(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c11(active,passive):
    if check_doing_list(active,passive,11):
        a.b('中止接吻',undocom11,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,11):
        a.b('接吻',execcom11,active,passive)
def execcom11(active,passive):
    remove_body_type_occupy(active,'口占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com11(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c12(active,passive):
    if check_doing_list(active,passive,12):
        a.b('打断自慰',undocom12,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,12):
        a.b('命令自慰',execcom12,active,passive)
def execcom12(active,passive):
    remove_body_type_occupy(passive,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com12(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c13(active,passive):
    if check_doing_list(active,passive,13):
        a.b('拔出手指',undocom13,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,13):
        a.b('尿道手指插入',execcom13,active,passive)
def execcom13(active,passive):
    remove_body_type_occupy(active,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com13(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c21(active,passive):
    if check_doing_list(active,passive,21):
        a.b('结束跳蛋调教',undocom21,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,21):
        a.b('跳蛋',execcom21,active,passive)
def execcom21(active,passive):
    remove_body_type_occupy(active,'手占用')
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com21(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c22(active,passive):
    if check_doing_list(active,passive,22):
        a.b('拉出跳蛋',undocom22,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,22):
        a.b('跳蛋插入',execcom22,active,passive)
def execcom22(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com22(active,passive)
    a.repeat()

def c23(active,passive):
    if check_doing_list(active,passive,23):
        a.b('拉出A跳蛋',undocom23,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,23):
        a.b('跳蛋A插入',execcom23,active,passive)
def execcom23(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com23(active,passive)
    a.repeat()

def c24(active,passive):
    if check_doing_list(active,passive,24):
        a.b('C电动按摩棒',undocom24,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,24):
        a.b('C电动按摩棒',execcom24,active,passive)
def execcom24(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com24(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c25(active,passive):
    if check_doing_list(active,passive,25):
        a.b('V按摩棒',undocom25,active,passive, style = {'color':'#ff0'})
    elif check_doing_list(active,passive,26) and check_bound_conflict(passive,25):
        a.b('双插按摩棒',execcom26,active,passive, style = {'color':'#FFC1C1'})
    elif check_bound_conflict(passive,25):
        a.b('V按摩棒',execcom25,active,passive)
def execcom25(active,passive):
    conflict_com = [50,51,52,53,54,55]
    remove_com_conflict(active,passive,conflict_com)
    com25(active,passive)
    a.repeat()

def c26(active,passive):
    if check_doing_list(active,passive,26):
        a.b('肛用按摩棒',undocom26,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,26) and check_doing_list(active,passive,25):
        a.b('双插按摩棒',execcom26,active,passive, style = {'color':'#FFC1C1'})
    elif check_bound_conflict(passive,26):
        a.b('肛用按摩棒',execcom26,active,passive)
def execcom26(active,passive):
    conflict_com = [56,57,58,59,60,61]
    remove_com_conflict(active,passive,conflict_com)
    com26(active,passive)
    a.repeat()

def c27(active,passive):
    if check_doing_list(active,passive,27):
        a.b('拿掉阴蒂夹',undocom27,active,passive, style = {'color':'#ff0'})
    elif passive['性别'] == '女性'and check_bound_conflict(passive,27):
        a.b('阴蒂夹',execcom27,active,passive)
def execcom27(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com27(active,passive)
    a.repeat()

def c28(active,passive):
    if check_doing_list(active,passive,28):
        a.b('拿掉乳头夹',undocom28,active,passive, style = {'color':'#ff0'})
    elif check_bound_conflict(passive,28):
        a.b('乳头夹',execcom28,active,passive)
def execcom28(active,passive):
    conflict_com = [30]
    remove_com_conflict(active,passive,conflict_com)
    com28(active,passive)
    a.repeat()

def c29(active,passive):
    if check_doing_list(active,passive,29):
        a.b('飞机杯',undocom29,active,passive, style = {'color':'#ff0'})
    elif passive['性别'] != '女性' and check_bound_conflict(passive,29):
        a.b('飞机杯',execcom29,active,passive)
def execcom29(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com29(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def c30(active,passive):
    if check_doing_list(active,passive,30):
        a.b('榨乳机',undocom30,active,passive, style = {'color':'#ff0'})
    elif passive['性别'] != '男性' and check_bound_conflict(passive,29):
        a.b('榨乳机',execcom30,active,passive)
def execcom30(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com30(active,passive)
    a.repeat()

def c31(active,passive):
    if check_doing_list(active,passive,31):
        a.b('绳缚',undocom31,active,passive, style = {'color':'#ff0'})
    else:
        a.b('绳缚',execcom31,active,passive)

def execcom31(active,passive):
    conflict_com = []
    remove_com_conflict(active,passive,conflict_com)
    com31(active,passive)
    if not a.tmp()['正在执行']:
        singal_step()

def singal_step():
    a.page()
    a.divider()
    a.mode()
    doing_list = a.tmp()['执行列表']
    a.tmp()['正在执行'] = True
    for i in doing_list:
        active = find_people(i[0])
        passive = find_people(i[1])
        com = i[2]
        exec('com{}(active,passive)'.format(com))
    a.tmp()['正在执行'] = False
    for c in a.tmp()['调教数据']['参与者']:
        all_cal(c)
    main_orgasm(a.tmp()['调教数据']['参与者'])
    a.repeat()

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
        a.tmp()['去冲突标志'] = True
        exec('undocom{}(active,passive)'.format(conflict_com[2]))

def remove_body_type_occupy(c,body_type):
    com = c['标志'][body_type]
    for i in a.tmp()['执行列表']:
        if c['CharacterId'] == i[0] and com == i[2]:
            conflict_com = i
            active = find_people(conflict_com[0])
            passive = find_people(conflict_com[1])
            a.tmp()['去冲突标志'] = True
            exec('undocom{}(active,passive)'.format(conflict_com[2]))

def find_people(CharacterId):
    for i in a.tmp()['调教数据']['参与者']:
        if i['CharacterId'] == CharacterId:
            return i
    return False

equipment_com_list = [22,23,25,26,27,28,30]
bound_trans_dict = {1:'镣铐束缚',2:'龟甲缚',3:'桌台束缚',4:'桌台束缚(背)',5:'四肢吊起',6:'单脚站立'}
def updata_state():
    for i in a.tmp()['执行列表']:
        active = find_people(i[0])
        passive = find_people(i[1])
        com = com_dict[i[2]]
        if not [com,''] in passive['调教状态']:
            if i[2] == 31:
                passive['调教状态'].append([bound_trans_dict[passive['标志']['受缚类型']],''])
            elif i[2] in equipment_com_list:
                passive['调教状态'].append([com,''])
            else:
                passive['调教状态'].append([com,active['名字']])

#记录每一种捆缚的冲突指令
bound_conflict_table = {
    1:[12,55,61,65,67,68],
    2:[12,65,67,68],
    3:[12,51,52,53,54,55,57,58,59,60,61,65,67,68,70,71],
    4:[12,21,24,29,50,52,53,54,55,56,58,59,60,61,65,67,68,70,71],
    5:[12,50,51,52,55,56,57,58,61,65,67,68,70,71],
    6:[12,50,51,52,53,54,55,56,57,58,59,60,61,65,67,68,70,71],
}
#检查指令com是否与角色受缚情况冲突
def check_bound_conflict(c,com):
    bound_type = c['标志']['受缚类型']
    if bound_type == 0: return True
    if com in bound_conflict_table[bound_type]:
        return False
    else:
        return True

