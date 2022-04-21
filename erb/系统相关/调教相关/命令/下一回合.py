import erajs.api as a
from erb.系统相关.口上相关.口上调用 import print_kojo
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.绝顶 import main_orgasm


def singal_step():
    doing_list = a.tmp()['执行列表']
    a.tmp()['连续执行'] = False
    for i in doing_list:
        active = find_people(i[0])
        passive = find_people(i[1])
        com = i[2]
        exec('com{}(active,passive)'.format(com))
    all_cal(a.tmp()['调教信息']['参与者'])
    main_orgasm(a.tmp()['调教信息']['参与者'])
    print_kojo()
    a.repeat()

def find_people(CharacterId):
    for i in a.tmp()['调教数据']['参与者']:
        if i['CharacterId'] == CharacterId:
            return i
    return False