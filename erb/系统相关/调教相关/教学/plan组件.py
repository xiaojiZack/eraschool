import erajs.api as a
import random
from erb.系统相关.口上相关.地文.课程_侍奉练习地文 import class4_main_describe
from erb.系统相关.口上相关.地文.课程_催眠洗脑地文 import class2_main_describe
from erb.系统相关.口上相关.地文.课程_淫物鉴赏地文 import class3_main_describe
from erb.系统相关.口上相关.地文.课程_耐力训练地文 import class5_main_describe

from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.记忆结算 import end_cal
from erb.系统相关.页面.check_character import detail_character
from erb.系统相关.调教相关.教学.课程效果计算 import cal_course_effect
from funcs import wait

class_kojo_dict = {
    '健身操':class5_main_describe,
    '跑步':class5_main_describe,
    '游泳':class5_main_describe,
    '常识变更':class2_main_describe,
    '性知识讲解':class2_main_describe,
    '催眠':class2_main_describe,
    '普通AV':class3_main_describe,
    '热门AV':class3_main_describe,
}

#找到对应课程口上地文函数
def find_kojo_func(material_name):
    for name in ['手交','口交','足交','乳交','素股','骑乘']:
        if name in material_name:
            return class4_main_describe
    return class_kojo_dict[material_name]

def determine(c, effect, effect_rate,material_name):
    #课程口上
    find_kojo_func(material_name)(c,effect_rate,material_name)
    #结算效果
    dic = {'SSS':5,'SS':4,'S':3,'A':2,'B':1,'C':0}
    el = dic[effect_rate]
    effect_type_level = [0.5, 1, 1.5, 2, 2.5, 3]
    for i in effect:
        if i == '随机技术':
            tech_list = ['腰技经验','舌技经验','指技经验','魔乳经验','足技经验']
            for j in range(effect['随机技术']):
                c['待处理经验'][random.choice(tech_list)] += 1
        elif i =='体力变化':
            for j in range(0,3):
                c['待处理体力变化'][j] = c['待处理体力变化'][j] + effect[i][j]
        elif i == '体力增长':
            c['最大体力值'] = int(c['最大体力值']+effect[i])
        elif '催眠' in i:
            c['催眠'] += int(effect[i]*effect_type_level[el])
        elif not '经验' in i:
            c['待处理记忆'][i] += int(effect[i]*effect_type_level[el])
        else:
            c['待处理经验'][i] += int(effect[i]*effect_type_level[el])
    all_cal(c)
    end_cal(c)
    wait()
    a.back(2)

def determine_participants(course_tag, course_difficulity, material_determine):
    a.divider()
    a.t('要选择哪些学生参加本课程？')
    a.mode('grid',7)
    a.tmp()['调教数据']={}
    a.tmp()['调教数据']['参与者'] = []
    a.tmp()['调教数据']['参与者'].append(a.sav()['character_list']['主角'])
    cl = a.sav()['character_list']['学生']
    for i in cl:
        c = cl[i]
        a.b(c['名字'], a.goto, detail_character, c)
        a.t()
        if c['性别'] == '男性':
            a.t('♂')
        elif c['性别'] == '女性':
            a.t('♀')
        else:
            a.t('♀♂')
        a.t()
        a.t('体力:')
        a.progress(c['体力值'],c['最大体力值'], [{'width': '30px'}, {}])
        a.t()
        a.t('气力:')
        a.progress(c['气力值'],c['最大气力值'], [{'width': '30px'}, {}])
        a.t()
        a.t('理智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '30px'}, {}])
        a.t()
        course_effect = cal_course_effect(c, course_tag, course_difficulity)
        effect_type = {'color':'#000'}
        if course_effect == 'C':
            effect_type = {'color':'#778899'}
        elif course_effect == 'B':
            effect_type = {'color':'#FFFF00'}
        elif course_effect == 'A':
            effect_type = {'color':'#008000'}
        elif course_effect == 'S':
            effect_type = {'color':'#FFC1C1'}
        elif course_effect == 'SS':
            effect_type = {'color':'#FF00FF'}
        elif course_effect == 'SSS':
            effect_type = {'color':'#FF0000'}
        a.t('预估表现:')
        a.t('{}'.format(course_effect), style = effect_type)
        a.t()
        if check_pp([c['体力值'],c['气力值'],c['理智值']],material_determine['效果']['体力变化']):
            a.b('决定',determine,c, material_determine['效果'],course_effect,material_determine['名称'])
        else:
            a.b('体力不足')
        a.t()
    
    a.divider()
    a.b('取消',a.back)

def check_tech(require):
    flag = True
    for i in require:
        if i == '无':f = True
        elif '建筑:' in i:
            f = False
            for building in a.sav()['校内建筑列表']:
                if building['名称'] in i:
                    f = True
        else: 
            if i in a.sav()['科技']: f = True
            else: f = False
        flag = flag and f
    return flag

def check_pp(c_pp, effect_pp):
    #检查是否有充足体力
    for i in range(0,3):
        if c_pp[i]<effect_pp[i]:
            return False
    return True