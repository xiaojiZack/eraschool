import erajs.api as a
from erb.系统相关.调教相关.液体 import eject_liquid, inject_liquid
from funcs import get_leading_character, get_student_list
from random import choice

def try_trigger3(c):
    flag = True
    #好感度>100
    if c['好感度']<1000:
        flag = False
    if c['刻印']['反发刻印']>1:
        flag = False
    if c['开发']['精液成瘾']<2:
        flag = False
    if c['经验']['口交经验']<50:
        flag = False
    return flag

def try_event3():
    student_list = get_student_list()
    can_trigger_students = []
    for student_id in student_list:
        student = student_list[student_id]
        if try_trigger3(student):
            can_trigger_students.append(student_id)
    if can_trigger_students == []:
        return False
    else:
        student_id = choice(can_trigger_students)
        student = student_list[student_id]
        performance3(student)
        return True

def performance3(c):
    a.t('在睡梦中朦朦胧胧地感觉到下体有着谜之快感，你迷迷糊糊地掀起被子发现')
    if '狂乱' in c['属性']['个性'] or '崩坏' in c['属性']['个性']:
        a.t('{}正双目无神地吸吮着你的肉棒。'.format(c['名字']))
        a.t('似乎完全是在按照本能行动')

    elif '臆病' in c['属性']['个性'] or '自卑' in c['属性']['个性']:
        a.t('{}正跪在你身下小心翼翼地舔舐着你的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后{}吓得肉棒都从嘴里滑了出来。'.format(c['名字']))
        a.t('觉得应对{}之后自顾自的道歉实在是好麻烦，你放弃思考把{}的头重新按回股间'.format(c['名字'],c['名字']))
    elif '无节操' in c['属性']['个性'] or '高傲' in c['属性']['个性']:
        a.t('{}正压住你的腿粗暴地用嘴榨取着你的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后{}摆出了一副‘咋了’的表情继续榨取着精液。'.format(c['名字']))
    elif '顺从' in c['属性']['个性'] or '坦率' in c['属性']['个性']:
        a.t('{}正趴在股间温柔地吸吮着你的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后{}含糊不清地问候了早安。'.format(c['名字']))
    elif '孩子气' in c['属性']['个性'] or '傲娇' in c['属性']['个性']:
        a.t('{}正偷偷吸吮着你的肉棒。'.format(c['名字']))
        a.t('如果被发现其实已经醒来的话估计又少不了大闹一番，你决定继续装睡。')
    elif '好色' in c['属性']['个性'] or '小恶魔' in c['属性']['个性']:
        a.t('{}正紧紧抱住你的腰部贪婪地榨取着清早的浓精，'.format(c['名字']))
        a.t('发现你已经醒了以后,{}吞咽着精液故意摆出了一副迷离的表情。'.format(c['名字']))
    else:
        a.t('{}正含着你的肉棒。'.format(c['名称']))
        a.t('在一阵响亮的吞咽声后{}娇声问候了一声早安。'.format(c['名称']))
    
    m = c['待处理记忆']
    e = c['待处理经验']
    m['好感度'] += 10
    m['恭顺'] += 1000
    m['欲情'] += 1000
    m['羞耻'] += 1000
    m['屈服'] += 1000
    m['侍奉快乐'] += 1
    e['爱情经验'] += 1
    count = 1+c['开发']['喉名器度']*c['开发']['舌技']
    e['饮精经验'] += count
    e['精液经验'] += count
    a.t()
    a.t('在{}口中射精了{}次。'.format(c['名字'],count))
    e['口交经验'] += 1
    e['舌技经验'] += 1
    e['侍奉经验'] += 1
    liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
    inject_liquid(c,'口',liquid_list)