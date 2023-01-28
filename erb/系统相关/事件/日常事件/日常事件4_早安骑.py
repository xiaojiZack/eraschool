import erajs.api as a
from erb.系统相关.调教相关.液体 import eject_liquid, inject_liquid
from funcs import get_leading_character, get_student_list
from random import choice

def try_trigger4(c):
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

def try_event4():
    student_list = get_student_list()
    can_trigger_students = []
    for student_id in student_list:
        student = student_list[student_id]
        if try_trigger4(student):
            can_trigger_students.append(student_id)
    if can_trigger_students == []:
        return False
    else:
        student_id = choice(can_trigger_students)
        student = student_list[student_id]
        performance4(student)
        return True

def performance4(c):
    a.t('在睡梦中朦朦胧胧地感觉到下体有着谜之快感，你迷迷糊糊地睁开眼睛发现')
    if '狂乱' in c['属性']['个性'] or '崩坏' in c['属性']['个性']:
        a.t('{}正双目无神地骑在你身上，肉棒在{}的身下进出抽插着。'.format(c['名字'],c['名字']))
        a.t('尽情地在{}肚内注入精种后发现{}似乎完全是在无意识地按照本能行动。'.format(c['名字'],c['名字']))

    elif '臆病' in c['属性']['个性'] or '自卑' in c['属性']['个性']:
        a.t('{}正扶着你的腰部小心地扭腰享受插入体内的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后{}一下子吓得僵住了。'.format(c['名字']))
        a.t('觉得应对{}之后自顾自的道歉实在是好麻烦，你放弃思考抓住{}的腰侧开始向上顶胯。'.format(c['名字'],c['名字']))
        a.t('{}立刻融化在升天的快感中，像一滩烂泥般倒在你身上任由你在体内注入精种。'.format(c['名字']))
    elif '无节操' in c['属性']['个性'] or '高傲' in c['属性']['个性']:
        a.t('{}正双手压住你的上臂粗暴地摆腰榨取着你的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后'+c['名字']+'红着脸俯视着你催促你赶快在体内播种')
    elif '顺从' in c['属性']['个性'] or '坦率' in c['属性']['个性']:
        a.t('{}正跪在你身上轻柔地摆动腰肢，服侍着你插入体内的肉棒。'.format(c['名字']))
        a.t('发现你已经醒来之后{}含糊不清地问候了早安，并在小腹中发出响亮的注精声后娇声汇报了今日的行程。'.format(c['名字']))
    elif '孩子气' in c['属性']['个性'] or '傲娇' in c['属性']['个性']:
        a.t('{}正骑在你身上偷偷用腔内榨取着精液。'.format(c['名字']))
        a.t('发现你已经清醒以后{}原本就红着的脸更是涨的通红，捂着脸欲哭无泪的样子实在是很可爱。'.format(c['名字']))
        a.t('自暴自弃地放弃抵抗的{}被你一个翻身压在身下，随后在娇柔的呻吟中被注入浓精。'.format(c['名字']))
    elif '好色' in c['属性']['个性'] or '小恶魔' in c['属性']['个性']:
        a.t('{}正紧紧骑在你的腰上贪婪地榨取着清早的浓精，'.format(c['名字']))
        a.t('发现你已经醒了以后,{}一脸坏笑地俯下身子玩弄你的乳头催促着体内射精。'.format(c['名字']))
    else:
        a.t('{}正用骑乘位榨取你一天中最浓的精种。'.format(c['名称']))
        a.t('在一阵响亮的注精声后{}娇声问候了一声早安，一边开始下一轮榨精一边提醒你今日的行程。'.format(c['名称']))
    
    m = c['待处理记忆']
    e = c['待处理经验']
    m['好感度'] += 100
    m['侍奉快乐'] += 10
    m['恭顺'] += 3000
    m['屈服'] += 3000
    m['欲情'] += 3000
    m['羞耻'] += 3000
    m['侍奉快乐'] += 1
    e['爱情经验'] += 3
    count = 1+c['开发']['喉名器度']*c['开发']['舌技']
    e['饮精经验'] += count
    e['精液经验'] += count
    a.t()
    if c['经验']['V经验']>c['经验']['A经验'] and not c['性别'] == '女性':
        count = 1+c['开发']['V名器度']*c['开发']['腰技']
        e['腔射经验'] += count
        e['精液经验'] += count
        a.t('在{}的腔内射精了{}次'.format(c['名字'],count))
        liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
        inject_liquid(c,'阴道',liquid_list)
    else:
        count = 1+c['开发']['A名器度']*c['开发']['腰技']
        e['肛射经验'] += count
        e['精液经验'] += count
        a.t('在{}的肠内射精了{}次'.format(c['名字'],count))
        liquid_list = eject_liquid(get_leading_character(),'阴茎',1+c['开发']['A名器度']*c['开发']['腰技'])
        inject_liquid(c,'肛门',liquid_list)
    e['腰技经验'] += 2