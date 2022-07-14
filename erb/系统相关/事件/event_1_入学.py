import random
import time
import erajs.api as a
from erb.系统相关.调教相关.教学.学业评级 import rate_study
from ..人物相关.character_creat import creat_normal_character
from ..人物相关.character_class import new_character_dict

def event1():
    a.page()
    a.mode()
    num =number_of_new_student()
    a.t('\"今年有')
    a.t('{}'.format(num),style = {'color':'#f00'})
    a.t('个入学名额\"',True)
    a.t()
    a.t('\"以下是申请文件，请仔细挑选未来的肉便,嗯哼,学生\"',True)
    a.t()
    for i in range(0,num):
        a.tmp()['录取标志'] = False
        a.tmp()['拒绝标志'] = False
        c = {}
        while a.tmp()['录取标志'] == False:
            a.tmp()['录取标志'] = False
            a.tmp()['拒绝标志'] = False
            c = creat_new_student()
            detail_character(c)
            while a.tmp()['录取标志'] == False and a.tmp()['拒绝标志'] == False:
                time.sleep(0.1)
        roll(c)
    a.page()
    a.mode()
    a.t('\"录取名单已经收到。直到他们毕业为止，请好好负起责任来\"')
        

def number_of_new_student():
    fame = a.sav()['学院评级']
    if fame == 'D': ex_number = 1
    return ex_number+1

def creat_new_student():
    c = new_character_dict()
    c['性别'] = '女性'
    c = creat_normal_character(c)
    return c

def roll(c):
    word_list = [
        '希望ta能在毕业时成为优秀的便器',
        'ta还不知道前方有怎样的命运在等待',
        '您打算对ta实施怎么样的教育方针呢？',
        '又一具娇嫩的身躯。',
        'ta会很高兴的，呼呼呼',
        '宿舍的床位还有空的吗？',
        '更喜欢这种类型的是吗？']
    c['入学档案备份'] = c.copy()
    a.sav()['character_list']['学生'][c['CharacterId']] = c
    a.sav()['character_list']['character_number'] +=1
    a.msg('{}被录取了，{}'.format(c['名字'],random.choice(word_list)))

def detail_character(c,mode='一般'):
    def page_1():
        a.cls()
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider()
        a.mode('grid',1)
        a.h(c['名字'])
        a.divider()
        a.mode('grid', 3)
        a.t('性别:{}'.format(c['性别']))
        a.t()
        a.t('好感度:{}'.format(c['好感度']))
        a.t()
        a.t('侍奉快乐:{}'.format(c['侍奉快乐']))
        a.t()
        # a.t('种族:{}'.format(c['种族']))
        # a.t()
        a.t('体力:')
        a.progress(c['体力值'],c['最大体力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
        a.t()
        a.t('气力:')
        a.progress(c['气力值'],c['最大气力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['气力值'],c['最大气力值']))
        a.t()
        a.t('理智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
        a.t()
        #胎内精液量
        a.divider('体型')
        a.mode('grid',5)
        a.t('身高:{}cm'.format(c['身体信息']['具体身高']))
        a.t()
        a.t('体重:{}kg'.format(c['身体信息']['具体体重']))
        a.t()
        if c['性别']!='男性':
            a.t('胸部:{}'.format(c['身体信息']['三围']['B']))
            a.t()
            a.t('腰部:{}'.format(c['身体信息']['三围']['H']))
            a.t()
            a.t('臀部:{}'.format(c['身体信息']['三围']['W']))
        a.divider('属性')
        a.mode('grid',1)
        q = c['属性']
        for i in q:
            if (len(q[i]) != 0):
                a.t('{}:'.format(i))
                for j in q[i]:
                    a.t('[{}]'.format(j))
                a.t()
        a.divider('经验')
        q = c['经验']
        a.mode('grid', 6)
        for i in q:
            if q[i] != 0:
                a.t('{}:{}'.format(i, q[i]))
                a.t()
        a.divider('身体开发')
        q = c['开发']
        for i in q:
            a.t('{}:Lv{}'.format(i, q[i]))
            a.t()
        a.divider()
        a.mode('grid',3)
        a.b('第二页',page_2)
        a.t()
        a.b('录取',roll_in)
        a.t()
        a.b('拒绝',reject)
    def page_2():
        a.cls()
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider('堕落记忆')
        a.mode('grid', 6)
        q = c['记忆']
        for i in q:
            if q[i] != 0:
                a.t('{}:{}'.format(i, q[i]))
                a.t()
        a.divider('精神刻印')
        q = c['刻印']
        for i in q:
            a.t('{}:{}'.format(i, q[i]))
            a.t()
        a.divider()
        a.mode('grid',4)
        a.b('第一页',page_1)
        a.t()
        a.b('第三页',page_3)
        a.t()
        a.b('录取',roll_in)
        a.t()
        a.b('拒绝',reject)
    def page_3():
        def show_detail(grade,name):
            a.page()
            a.mode()
            a.h(name)
            a.divider()
            for i in grade['细则']:
                a.t('{}({})+'.format(i,grade['细则'][i]))
            a.t('...')
            a.t('={}'.format(grade['分数']))
            a.divider()
            a.b('返回',page_3)
        
        def show_grade(grade,i):
            style = change_style(grade['评级'])
            if i != '总分':
                a.b('{} [{}]'.format(grade['分数'],grade['评级']),show_detail,grades[i],i,style=style)
            else:
                a.t('{} [{}]'.format(grade['分数'],grade['评级']),style=style)

        def change_style(rate):
            style = {}
            if rate == 'D':
                style['color'] = '#778899'
            elif rate == 'C':
                style['color'] = '#7FFF00'
            elif rate == 'B':
                style['color'] = '#FFFF00'
            elif rate == 'A':
                style['color'] = '#FFC1C1'
            elif rate == 'S':
                style['color'] = '#FF0000'
            return style
        
        rate_study(c)
        a.cls()
        a.page()
        a.divider()
        a.mode('grid',4)
        grades = c['学籍']['成绩']
        for i in grades:
            a.t('{}:'.format(i))
            show_grade(grades[i],i)
            a.t()
        a.divider()
        a.mode('grid',3)
        a.b('第二页',page_2)
        a.t()
        a.b('录取',roll_in)
        a.t()
        a.b('拒绝',reject)
    
    page_1()

def roll_in():
    a.tmp()['录取标志'] = True
def reject():
    a.tmp()['拒绝标志'] = True