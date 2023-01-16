import random
import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal

def structure9():
    return True

def exec9():
    #随机触发
    if random.random()>0.3:
        #随机选取一个学生
        student_list = a.sav()['character_list']['学生']
        if len(student_list) == 0: #防止因为没有人可选导致报错
            return False
        student = student_list[random.choice(list(student_list.keys()))]
        m = student['待处理记忆']
        e = student['待处理经验']

        a.t('{}抽空去游泳了，体力上升了。'.format(student['名字']))
        a.t()
        student['最大体力值'] += 50
        student['最大气力值'] += 100

        student = memory_cal(student)

def destory9():
    return True