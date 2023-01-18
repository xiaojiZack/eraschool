import random
import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal

def exec21(building):
    #图书馆效果,随机选择一个学生，根据欲望等级选择一本书
    books = {
        '恋爱小说':{
            '效果':{
                '欲情':10000,
                '恭顺':1000,
            }
        },
        '《性爱三十八手》':{
            '效果':{
                '欲情':1000,
                '指技经验':1,
                '舌技经验':1,
                '腰技经验':1,
                '足技经验':1,
                '魔乳经验':1
            }
        },
        '本子':{
            '效果':{
                '欲情':50000
            }
        },
        'R18轻小说':{
            '效果':{
                '欲情':5000,
                '恭顺':5000,
            }
        }
    }
    
    #随机选取一个学生
    student_list = a.sav()['character_list']['学生']
    if len(student_list) == 0: #防止因为没有人可选导致报错
        return False
    student = student_list[random.choice(list(student_list.keys()))]
    m = student['待处理记忆']
    e = student['待处理经验']

    book = random.choice(list(books.keys()))

    a.t('{}在图书馆借走了一本{}。'.format(student['名字'],book))
    a.t()

    effect = books[book]['效果']
    for i in effect:
        if '经验' in i:
            e[i] += effect[i]
        else:
            m[i] += effect[i]

    student = memory_cal(student)
    

def destory21(building):

    return True

def structure21(building={}):

    return True
