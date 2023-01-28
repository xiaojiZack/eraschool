from erajs import api as a
from erb.系统相关.调教相关.教学.学业评级 import rate_study
from erb.系统相关.调教相关.服装.服装 import cloth_rate_color
from erb.系统相关.调教相关.液体 import transform_liquid_list
from erb.系统相关.页面.arrange_clothes import arrange_clothes_page
from erb.系统相关.页面.character_upgrade import character_upgrade_page


def check_character():
    a.page()
    a.mode('grid',5)
    a.divider()
    cl = a.sav()['character_list']['学生']
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
        a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
        a.t()
        a.t('气:')
        a.progress(c['气力值'],c['最大气力值'], [{'width': '80px'}, {}])
        a.t('({}/{})'.format(c['气力值'],c['最大气力值']))
        a.t()
        a.t('智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '80px'}, {}])
        a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
        a.t()
        # a.t(c['学籍']['班级'])
        # a.t()
    a.divider()
    a.b('返回',a.back)

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
        a.mode('grid',4)
        a.b('<-第四页',page_4)
        a.t()
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
        a.mode('grid',3)
        a.b('<-第二页',page_2)
        a.t()
        a.b('->第四页',page_4)
        a.t()
        a.b('返回',a.back)
    def page_4():
        
        def describe_V():
            #角色检查描述阴道
            vagina = c['身体信息']['阴道']
            transform = ''
            if vagina['改造'] == []:
                transform = '健康的'
            if vagina['内容固体'] == {}:
                pass
            sentence = c['名字']+'有着一个'+transform+'阴道。'
            a.t(sentence)
            a.t()
            #V感觉描述
            if c['开发']['V感觉'] <= 1:
                a.t('似乎对刺激还不太敏感.')
            elif c['开发']['V感觉'] == 2:
                a.t('稍微能从性爱中获得快感.')
            elif c['开发']['V感觉'] == 3:
                a.t('已经能从性爱中获得许多快感.')
            elif c['开发']['V感觉'] == 4:
                a.t('似乎已经变成异常敏感的肉壶了，仅仅将手指插进去就可以高潮')
            else:
                a.t('已经被开发成极度敏感的腔穴，一旦被插入什么的话就会不停高潮直到昏死过去。拥有这样的肉壶可以说是某种酷刑也不为过。')
            a.t()
            #V扩张度
            if c['开发']['V扩张度'] <= 1:
                a.t(c['名字']+'的小穴紧闭着，很难插进去什么东西.')
            elif c['开发']['V扩张度'] == 2:
                a.t('小穴的尺寸稍微有点小，即使只插入一根成人的手指都有些紧。不能插入过大的东西.')
            elif c['开发']['V扩张度'] == 3:
                a.t(c['名字']+'的肉穴能插入正常尺寸的物体.')
            elif c['开发']['V扩张度'] == 4:
                a.t('可以插入像是易拉罐一般稍大的物体。')
            else:
                a.t(c['名字']+'的小穴被扩张到能吞下崩坏尺寸巨物。')
            a.t()
        
        def describe_W():
            #角色检查描述子宫
            transform = ''
            womb = c['身体信息']['子宫']
            if womb['改造'] == []:
                a.t(c['名字']+'有着一个健康的子宫。')
            if womb['内容固体'] == {}:
                pass


            #W感觉描述
            if c['开发']['W感觉'] <= 1:
                a.t('目前还不能从子宫获得快感。')
            elif c['开发']['W感觉'] == 2:
                a.t('子宫逐渐成为了敏感带，似乎能产生一些感觉了.')
            elif c['开发']['W感觉'] == 3:
                a.t('经过开发，'+c['名字']+'现在可以通过子宫高潮了.现在'+c['名字']+'可以被称为合格的孕袋了，可喜可贺.')
            elif c['开发']['W感觉'] == 4:
                a.t(c['名字']+'的子宫已经被调教成了敏感的淫肉，不仅能因为被注入精种而高潮不已，在妊娠时也偶尔会因为胎动而绝顶升天')
            else:
                a.t(c['名字']+'的淫宫现在被开发成极度敏感的孕袋了，只需轻轻抚摸下腹就可以让其高潮到露出阿嘿颜，连妊娠似乎都成为了一件危险的事情。')
            a.t()

            #受孕成瘾描述
            if c['开发']['受孕成瘾'] == 0:
                a.t(c['名字']+'对于怀孕这件事还是保持拒绝的态度。')
            elif c['开发']['受孕成瘾'] == 1:
                a.t(c['名字']+'似乎对受孕有很大兴趣，本人描述是‘肚子里空空的会感觉有点痒’')
            elif c['开发']['W感觉'] == 2:
                a.t(c['名字']+'渴望受孕，肚子里没有胎儿或者子宫没有装满精种就会感到坐立难安')
            elif c['开发']['W感觉'] == 3:
                a.t(c['名字']+'的子宫已经被调教成了优秀的母胎，满脑子受孕、妊娠和出产。小腹中没有怀胎会让其焦虑到发狂。')

            #液体描述
            if womb['内容总量'] == 0:
                a.t('现在'+c['名字']+'的子宫里空空如也。')
            elif womb['内容总量'] < 0.5*womb['容量']:
                a.t(c['名字']+'的子宫里正装着一些液体')
            elif womb['内容总量'] < 0.8*womb['容量']:
                a.t(c['名字']+'的子宫里被灌注了液体，几乎已经装满了，在小腹上可以看到隐约凸起的轮廓，隐约有‘咣当’的水声。')
            else:
                a.t(c['名字']+'的子宫被灌的满满的，像是孕妇一般隆起。')
            a.t()
            a.b('胎内淫液:',show_liquid,'子宫')
            if womb['内容总量'] < 0.99*womb['容量']:
                a.progress(womb['内容总量'],womb['容量'])
            else:
                a.t('[满满的]',style={'color':'#FFC1C1'})

        def describe_B():
            transform = ''
            breast = c['身体信息']['乳房']
            if breast['改造'] == []:
                a.t(c['名字']+'有着一个健康胸部。')
            a.t()

            #B感觉描述
            if c['开发']['B感觉'] <= 1:
                a.t(c['名字']+'的胸部似乎对刺激还不太敏感.')
            elif c['开发']['B感觉'] == 2:
                a.t(c['名字']+'的胸部开始对揉捏产生了一些快感.')
            elif c['开发']['B感觉'] == 3:
                a.t('玩弄'+c['名字']+'的胸部现在可以得到非常可爱的反应。')
            elif c['开发']['B感觉'] == 4:
                a.t(c['名字']+'的胸部现在经过调教已经变得相当敏感，有时会因为衣物的摩擦而小小地高潮。')
            else:
                a.t(c['名字']+'的胸部现在经过调教已经变得异常敏感，即使不穿衣服，仅仅在乳头上吹过一阵微风也能让其高潮不止。')
            a.t()

            if breast['内容总量'] == 0:
                a.t('现在'+c['名字']+'的乳房里空空如也。')
            elif breast['内容总量'] < 0.5*breast['总量']:
                a.t(c['名字']+'的乳房里正装着一些液体')
            elif breast['内容总量'] < 0.8*breast['总量']:
                a.t(c['名字']+'的乳房里几乎装满了淫液。')
            else:
                a.t(c['名字']+'的乳房里装满着淫液。')
            a.t()
            a.b('乳内淫液:',show_liquid,'乳房')
            if breast['内容总量'] < 0.99*breast['容量']:
                a.progress(breast['内容总量'],breast['容量'])
            else:
                a.t('[满满的]',style={'color':'#FFC1C1'})

        def describe_A():
            #角色检查描述阴道
            anus = c['身体信息']['肛门']
            transform = ''
            if anus['改造'] == []:
                transform = '健康的'
            if anus['内容固体'] == {}:
                pass
            sentence = c['名字']+'有着一个'+transform+'菊穴。'
            a.t(sentence)
            a.t()
            #A感觉描述
            if c['开发']['A感觉'] <= 1:
                a.t('似乎对刺激还不太敏感.')
            elif c['开发']['A感觉'] == 2:
                a.t('稍微能从性爱中获得快感.')
            elif c['开发']['A感觉'] == 3:
                a.t('已经能从肛交中获得许多快感.')
            elif c['开发']['A感觉'] == 4:
                a.t('似乎已经变成异常敏感的后穴了，仅仅将手指插进去就可以高潮')
            else:
                a.t('已经被开发成极度敏感的后穴，坐在正常的椅子上都会高潮个不停，不断流出肠液。')
            a.t()
            #A扩张度
            if c['开发']['A扩张度'] <= 1:
                a.t(c['名字']+'的菊穴紧闭着，很难插进去什么东西.')
            elif c['开发']['A扩张度'] == 2:
                a.t(c['名字']+'的菊穴微闭着，如果要插入的话最好还是再扩张一下.')
            elif c['开发']['A扩张度'] == 3:
                a.t(c['名字']+'的菊穴现在已经被扩张开发到能轻松吞入正常尺寸的物体.')
            elif c['开发']['A扩张度'] == 4:
                a.t(c['名字']+'的菊穴富有难以想象的弹性，现在可以塞入腕大的东西了.')
            else:
                a.t('经过扩张调教，'+c['名字']+'的菊穴现在已经完全崩坏，连灭火器那样粗的阳具也可以轻松吞入肠内.')
            a.t()

            gut = c['身体信息']['肠道']
            if gut['内容总量'] == 0:
                a.t('现在'+c['名字']+'的肠子里没有被注入额外的液体。')
            elif gut['内容总量'] < 0.5*gut['容量']:
                a.t(c['名字']+'的肠道里被注入了一些液体，似乎能听到咕叽咕叽的微响。')
            elif gut['内容总量'] < 0.9*gut['容量']:
                a.t(c['名字']+'的肠道里几乎装满了淫液，使得小腹微微凸显出直肠的轮廓，每动一下腰肢便有‘咣当’的响声自肚内传出。')
            else:
                a.t(c['名字']+'的肠道里灌满了淫液，肚子也因此变得像临月孕妇一般高高隆起。')
            a.t()
            a.b('肠内淫液:',show_liquid,'肠道')
            if gut['内容总量'] < 0.99*gut['容量']:
                a.progress(gut['内容总量'],gut['容量'])
            else:
                a.t('[满满的]',style={'color':'#FFC1C1'})
        
        def describe_C():
            clit = c['身体信息']['阴核']
            if clit['改造'] == []:
                a.t(c['名字']+'有着一个健康阴蒂。')
            #C感觉描述
            if c['开发']['C感觉'] <= 1:
                a.t('似乎对刺激还不太敏感.')
            elif c['开发']['C感觉'] == 2:
                a.t('揉搓一下能有电流般的感觉.')
            elif c['开发']['C感觉'] == 3:
                a.t('经过调教以后，玩弄阴蒂可以让其发出娇艳的呻吟.')
            elif c['开发']['C感觉'] == 4:
                a.t('已经是变得过于敏感的阴蒂，由于衣料摩擦导致的快感使得穿着内裤也成了一种辛苦的事情。')
            else:
                a.t('已经被开发成极度敏感的淫核，仅仅是微风吹过都会高潮不止。')
            a.t()

        def describe_P():
            penis = c['身体信息']['阴茎']
            if penis['改造'] == []:
                a.t(c['名字']+'有着一个健康肉棒。')
            #C感觉描述
            if c['开发']['C感觉'] <= 1:
                a.t('似乎对刺激还不算太敏感.')
            elif c['开发']['C感觉'] == 2:
                a.t('揉搓一下能有电流般的快感.')
            elif c['开发']['C感觉'] == 3:
                a.t('经过调教以后，变成了有些敏感的阴茎。现在可以轻易地从中榨取精液了.')
            elif c['开发']['C感觉'] == 4:
                a.t('已经是变得过于敏感的肉棒，由于衣料摩擦导致的快感使得内裤里经常溢满了先走汁和精液。')
            else:
                a.t('已经被开发成极度敏感的淫茎，仅仅暴露在空气中都会一颤一颤地泄露精液。作为生产精液的精畜再适合不过。')
            a.t()

            if penis['内容总量'] == 0:
                a.t('现在'+c['名字']+'的精库已经被榨干了，干瘪着没有精神。')
            elif penis['内容总量'] < 0.5*penis['容量']:
                a.t(c['名字']+'的精袋里还有一些液体。')
            elif penis['内容总量'] < 0.9*penis['容量']:
                a.t(c['名字']+'的精袋里几乎要装满了。')
            else:
                a.t(c['名字']+'的精袋溢满了淫液，肉棒看起来饱满而鲜嫩多汁。')
            a.t()
            a.b('茎内淫液:',show_liquid,'阴茎')
            if penis['内容总量'] < 0.99*penis['容量']:
                a.progress(penis['内容总量'],penis['容量'])
            else:
                a.t('[满满的]',style={'color':'#FFC1C1'})

        def show_liquid(body_part):
            liquid_list = c['身体信息'][body_part]['内容液体']
            trans_liquid_list = transform_liquid_list(liquid_list)
            a.page()
            a.mode()
            for liquid in trans_liquid_list:
                a.t('{}:{}ml'.format(liquid,trans_liquid_list[liquid]))
                a.t()
            a.b('返回',a.back)
        #身体具体信息
        a.cls()
        a.page()
        a.mode()
        a.h('身体状态')
        if not c['性别'] == '男性':
            a.divider()
            describe_V()
        if c['性别'] == '女性':
            a.divider()
            describe_C()
        if not c['性别'] == '女性':
            a.divider()
            describe_P()
        a.divider()
        describe_A()
        a.divider()
        describe_B()
        if not c['性别'] == '男性':
            a.divider()
            describe_W()

        a.divider()
        a.mode('grid',3)
        a.b('<-第三页',page_3)
        a.t()
        a.b('->第一页',page_1)
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
    allow_point = 100
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
