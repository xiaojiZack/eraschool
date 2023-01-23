import erajs.api as a
from random import choice

def perform_good(student):
    #描写表现最好的员工
    sentence = []
    if student['开发']['侍奉欲望']<4:
        sentence.append('{}按部就班地完成了工作，没有发生什么意外。'.format(student['名字']))
    elif student['开发']['侍奉欲望']>=4:
        sentence.append('{}像一个真正的女仆一样工作着，在客人享用咖啡的同时给客人们按摩、聊天，施展某种让食物美味的魔法。得到了顾客们的一致好评。'.format(student['名字']))
    
    choice_sentence = choice(sentence)
    a.t(choice_sentence, style={'color':'#0f0'})
    a.t()

def perform_bad(student):
    #描写表现最坏的员工
    sentence = []
    if student['开发']['侍奉欲望']>=4:
        sentence.append('{}笨手笨脚地侍奉客人。店里收到了一些差评。'.format(student['名字']))
    elif student['开发']['侍奉欲望']<4:
        sentence.append('{}在咖啡厅里打碎了好几个盘子，上错了好几次菜，回头先好好调教一下吧。'.format(student['名字']))
    
    choice_sentence = choice(sentence)
    a.t(choice_sentence, style={'color':'#f00'})
    a.t()