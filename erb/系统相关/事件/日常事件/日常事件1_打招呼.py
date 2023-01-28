import erajs.api as a
from funcs import get_student_list
from random import choice

def try_trigger1(c):
    flag = True
    #好感度>100
    if c['好感度']<0:
        flag = False
    if c['刻印']['反发刻印']>2:
        flag = False
    return flag

def try_event1():
    student_list = get_student_list()
    can_trigger_students = []
    for student_id in student_list:
        student = student_list[student_id]
        if try_trigger1(student):
            can_trigger_students.append(student_id)
    if can_trigger_students == []:
        return False
    else:
        student_id = choice(can_trigger_students)
        student = student_list[student_id]
        performance1(student)
        return True

def performance1(c):
    if c['刻印']['反发刻印']>0:
        a.t('远远的看到了{}，但对方无视你扭头离开了。')
    elif '狂乱' in c['属性']['个性'] or '崩坏' in c['属性']['个性']:
        a.t('路上碰到了{}，对方像是行尸走肉一般漫游着。'.format(c['名字']))

    elif '臆病' in c['属性']['个性'] or '自卑' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，对方像过街老鼠似的低着头走在路边上的。试图上去打招呼的时候对方缩成一团逃走了。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方像过街老鼠似的低着头走在路边上的。对方小声地回应了你的问候。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，对方像过街老鼠似的低着头走在路边上的。{}在发现你以后抓着你的手臂粘了好久。'.format(c['名字'],c['名字']))
    elif '反抗' in c['属性']['个性'] or '高傲' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，对方无视了你的招呼擦肩而过。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方简短地回应了你的问候。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，对方礼貌地回应了你的问候。'.format(c['名字']))
    elif '刚强' in c['属性']['个性'] or '坦率' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，大步流星地走着。对方像是跟邻居打招呼般回应了问候。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方充满元气地回应了你的问候。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，对方远远地看到你就充满活力的向你跑来。'.format(c['名字']))
    elif '孩子气' in c['属性']['个性'] or '傲娇' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，对方以蔑视的眼光嫖了你一眼后就扬长而去。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，很有仪式感地向你行了一礼。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，对方紧紧抓着你的衣角粘着你好几分钟。'.format(c['名字']))
    elif '顺从' in c['属性']['个性'] or '无节操' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，结果是对方先打了招呼。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方亲切地问你今天有什么能帮的上忙的。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，对方温顺地从后面抱住你撒娇了一会。'.format(c['名字']))
    elif '好色' in c['属性']['个性'] or '小恶魔' in c['属性']['个性']:
        if c['好感度']<100:
            a.t('路上碰到了{}，打招呼的时候总感觉距离莫名的近。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方向你摆出诱惑的姿势。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，被问到今天有没有兴趣来调教对方。'.format(c['名字']))
    else:
        if c['好感度']<100:
            a.t('路上碰到了{}，互相简短地回应了一声。'.format(c['名字']))
        elif c['好感度']<1000:
            a.t('路上碰到了{}，对方停下来和你寒暄了一会。'.format(c['名字']))
        else:
            a.t('路上碰到了{}，轻轻抱了你一会。'.format(c['名字']))
    
    c['好感度'] += 10
    a.t('对方对你的好感度似乎上升了一些')