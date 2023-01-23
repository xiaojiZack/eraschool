from erajs import api as a
from erb.系统相关.调教相关.教学.学业评级 import rate_study
from erb.系统相关.调教相关.服装.服装 import cloth_rate_color
from erb.系统相关.页面.arrange_clothes import arrange_clothes_page
from erb.系统相关.页面.character_upgrade import character_upgrade_page


def check_character(cl):
    a.divider()
    a.mode('grid',6)
    #cl = a.sav()['character_list']['学生']
    for i in cl:
        c = cl[i]
        a.b('{}'.format(c['名字']), a.goto, detail_character, c)
        a.t()
        if c['性别'] == '男性':
            a.t('♂')
        elif c['性别'] == '女性':
            a.t('♀')
        else:
            a.t('♀♂')
        a.t()
        a.t('体')
        a.progress(c['体力值'],c['最大体力值'], [{'width': '80px'}, {}])
        a.t()
        a.t('气:')
        a.progress(c['气力值'],c['最大气力值'], [{'width': '80px'}, {}])
        a.t()
        a.t('智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '80px'}, {}])
        a.t()
        a.t('[{}]'.format(c['工作状态']))

def detail_character(c):
    def page_1():
        a.cls()
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider()
        a.mode('grid',1)
        a.h(c['名字'])
        a.divider()
        a.mode('grid', 4)
        a.t('性别:{}'.format(c['性别']))
        a.t()
        a.t('好感度:{}'.format(c['好感度']))
        a.t()
        a.t('侍奉快乐:{}'.format(c['侍奉快乐']))
        a.t()
        a.t('催眠:{}'.format(c['催眠']))
        a.t()
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
        a.b('第二页->',page_2)
        a.t()
        a.b('角色升级',a.goto,character_upgrade_page,c, 'check', style = {'color':'#778899'})
        a.t()
        a.b('返回',a.back)
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
        a.mode('grid',3)
        a.b('<-第一页',page_1)
        a.t()
        a.b('第三页->',page_3)
        a.t()
        a.b('返回',a.back)
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
        a.divider('评分')
        a.mode('grid',4)
        grades = c['学籍']['成绩']
        for i in grades:
            a.t('{}:'.format(i))
            show_grade(grades[i],i)
            a.t()
        show_clothes(c)
        a.divider()
        a.mode('grid',2)
        a.b('<-第二页',page_2)
        a.t()
        a.b('返回',a.back)
    
    page_1()

def show_clothes(c):
    a.divider('衣装')
    a.mode('line',1)
    clothes = c['衣物']
    for cloth_type in clothes:
        a.t('{}:'.format(cloth_type))
        if '配件' in cloth_type:
            for cloth in clothes[cloth_type]:
                a.t(cloth['名称'])
                a.t(' ')
            
        else:
            if clothes[cloth_type] == {}: 
                pass
            else:
                a.t('{}'.format(clothes[cloth_type]['名称']))
        a.t()
    a.divider()
    a.mode('grid',5)
    a.t('色情度:{}'.format(c['衣物效果']['色情度']), style=cloth_rate_color(c))
    a.t()
    a.t('羞耻度:{}'.format(c['衣物效果']['羞耻度']), style=cloth_rate_color(c))
    a.t()
    for bt in ['阴部','胸部','肛门']:
        a.t('{}:'.format(bt))
        if c['衣物效果']['关键部位'][bt]: a.t('可见',style={'color':'#FFC1C1'})
        else: a.t('不可见')
        a.t()
    a.mode('grid',1)
    if allow_change_clothes(c): 
        a.b('更换衣物', a.goto, arrange_clothes_page, c)
    else:
        a.b('{}现在还不允许你为其决定衣物'.format(c['名字']))

def allow_change_clothes(c):
    #判断是否允许玩家配置衣物
    def search_quaility(c,target):
        for i in c['属性']:
            for j in c['属性'][i]:
                if j == target:
                    return True
        return False
    #允许阈值为100
    allow_point = 0
    now_point = 0
    #服从贡献值
    obey_point = [0,10,20,30,40,50]
    now_point += obey_point[c['开发']['服从']]
    #欲望贡献值
    desire_point = [0,5,10,15,20,25]
    now_point += desire_point[c['开发']['欲望']]
    #露出癖贡献值
    exhibtion_point = [0,15,30,45,75]
    now_point += exhibtion_point[c['开发']['露出癖']]
    #快乐刻印
    happy_point = [0,10,20,30]
    now_point += happy_point[c['刻印']['快乐刻印']]
    #屈服刻印
    knee_point = [0,10,20,30]
    now_point += knee_point[c['刻印']['屈服刻印']]

    if search_quaility(c,'顺从'): now_point+= 5
    if search_quaility(c,'反抗'): now_point-= 5
    if search_quaility(c,'不知耻'): now_point+=20
    if search_quaility(c,'怕羞'): now_point -= 20
    if search_quaility(c,'喜欢受人注目'): now_point += 10

    if now_point>=allow_point:
        return True
    else:
        return False
