import erajs.api as a
from erb.系统相关.调教相关.教学.学业评级 import rate_study
from funcs import unwait, wait

#毕业奖金比例
bouns_rate = 1

def event2():
    #所有学生毕业检查
    student_list = a.sav()['character_list']['学生']

    id_list = list(student_list.keys()).copy()
    for id in id_list:
        student = student_list[id]
        graduate_character(student)
        wait()

        
        

def graduate_character(c,mode='一般'):
    #出货页面
    def page_1():
        a.cls()
        a.page()
        a.mode()
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
        a.divider('评级')
        rate_part()

    def rate_part():
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
            a.b('返回',page_1)
        
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

        a.mode('grid',4)
        grades = c['学籍']['成绩']
        for i in grades:
            a.t('{}:'.format(i))
            show_grade(grades[i],i)
            a.t()
        
        a.divider()
        a.mode()
        a.t('预计可以获得奖金{}G'.format(max(0,c['学籍']['成绩']['总分']['分数']*bouns_rate)))
        a.t()
        a.b('毕业', graduate, c)

    
    page_1()


def graduate(c):
    #将学生毕业，按照grade计算毕业奖金
    #日后加入志愿和委托系统
    grades = c['学籍']['成绩']['总分']['分数']

    bouns = max(0,grades*bouns_rate)
    a.sav()['资源']['金钱'] += bouns
    
    a.page()
    a.mode()
    a.t('{}成功毕业了。从某处获得了{}G作为毕业奖金。'.format(c['名字'],bouns), wait=True)

    id = c['CharacterId']
    a.sav()['character_list']['学生'].pop(id)
    a.sav()['character_list']['character_number'] -=1
    a.sav()['历史毕业人数'] += 1
    
    unwait()
