import random
import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal

def exec2(building):
    #影视厅被动效果，随机选择一个学生，增加欲情/习得/x技经验
    
    #随机选取一个学生
    student_list = a.sav()['character_list']['学生']
    if len(student_list) == 0: #防止因为没有人可选导致报错
        return False
    student = student_list[random.choice(list(student_list.keys()))]
    m = student['待处理记忆']
    e = student['待处理经验']

    a.t('{}在影视厅观看了一部爱情动作片。'.format(student['名字']))
    a.t()
    m['欲情'] += 4000
    m['习得'] += 2000

    choice_exp = random.choice(['腰技','舌技','指技','魔乳','足技'])
    e['{}经验'.format(choice_exp)] += 1
    student = memory_cal(student)
    

def destory2(building):

    return True

def structure2(building={}):

    return True
