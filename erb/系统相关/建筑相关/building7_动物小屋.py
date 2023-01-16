import random
import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal

def exec7(building):
    #动物小屋效果，收获一点钱，随机增加情欲
    
    a.t('饲养的动物产出了一些可以换钱的东西，获得了500G.')
    a.t()
    a.sav()['资源']['金钱'] += 500

    #随机触发
    if random.random()>0.5:
        #随机选取一个学生
        student_list = a.sav()['character_list']['学生']
        if len(student_list) == 0: #防止因为没有人可选导致报错
            return False
        student = student_list[random.choice(list(student_list.keys()))]
        m = student['待处理记忆']
        e = student['待处理经验']

        a.t('{}在路过动物小屋时看到了动物交配的场景。'.format(student['名字']))
        a.t()
        m['欲情'] += 1000
        m['习得'] += 500

        student = memory_cal(student)
    

def destory7(building):

    return True

def structure7(building={}):

    return True
