import erajs.api as a
from erb.系统相关.人物相关.character_class import search_quaility

#学业评级，关系到教学计划的实施、毕业校方收益
#评级分为4个方向1.服从性 2.身体开发 3.榨精力 4.个性科目
#服从性=服从等级+欲望等级+侍奉精神等级+刻印总算+堕落系素质+性格素质
#身体开发=器官敏感等级（素质补正）+扩张补正+体质系素质+堕落系素质
#榨精力 = 技巧等级+SM属性+名器度（榨精系体质素质）
#个性科目=异常开发等级（兽、触、露出）+异常体质+器官开发：射精量、射乳量+成瘾开发
def rate_study(c):
    if type(c) == int:
        c = find_people(c)
    obey = cal_obey(c)
    body_develop = cal_body_develop(c)
    squeeze = cal_squeeze(c)
    special = cal_special(c)
    if obey['分数']<20:
        obey['评级'] = 'D'
    elif obey['分数']<50:
        obey['评级'] = 'C'
    elif obey['分数']<100:
        obey['评级'] = 'B'
    elif obey['分数']<500:
        obey['评级'] = 'A'
    else:
        obey['评级'] = 'S'
    
    if body_develop['分数']<50:
        body_develop['评级'] = 'D'
    elif body_develop['分数']<200:
        body_develop['评级'] = 'C'
    elif body_develop['分数']<1000:
        body_develop['评级'] = 'B'
    elif body_develop['分数']<5000:
        body_develop['评级'] = 'A'
    else:
        body_develop['评级'] = 'S'
    
    if squeeze['分数']<20:
        squeeze['评级'] = 'D'
    elif squeeze['分数']<40:
        squeeze['评级'] = 'C'
    elif squeeze['分数']<60:
        squeeze['评级'] = 'B'
    elif squeeze['分数']<150:
        squeeze['评级'] = 'A'
    else:
        squeeze['评级'] = 'S'
    
    if special['分数']<20:
        special['评级'] = 'D'
    elif special['分数']<60:
        special['评级'] = 'C'
    elif special['分数']<200:
        special['评级'] = 'B'
    elif special['分数']<500:
        special['评级'] = 'A'
    else:
        special['评级'] = 'S'

    trans = {
        'D':1,'C':2,'B':3,'A':4,'S':5,
        '1':'D','2':'C','3':'B','4':'A','5':'S',
    }
    sumup = 0
    sumup_rate = 0
    c['学籍']['成绩']['服从性'] = obey
    sumup += obey['分数']
    sumup_rate += trans[obey['评级']]
    c['学籍']['成绩']['肉体开发'] = body_develop
    sumup += body_develop['分数']
    sumup_rate += trans[body_develop['评级']]
    c['学籍']['成绩']['榨精力'] = squeeze
    sumup += squeeze['分数']
    sumup_rate += trans[squeeze['评级']]
    c['学籍']['成绩']['个性科目'] = special
    sumup = special['分数']*sumup
    sumup_rate += trans[special['评级']]
    c['学籍']['成绩']['总分'] =  {'评级':trans[str(int(sumup_rate/4))],'分数':sumup}


def find_people(CharacterId):
    for i in a.tmp()['CharacterId']['学生']:
        if i['CharacterId'] == CharacterId:
            return i
    return False

#服从性计算
def cal_obey(c):
    develop = c['开发']
    mark = c['刻印']
    grade_for_obey = 5
    grade_for_desire = 5
    grade_for_serve = 5
    pl_check_list = {
        '反抗':-15,'坦率':5,'顺从':10,'幼稚':10,'高傲':-10,
        '自卑':5,'自制':-10,'纵欲':10,'傲娇':-1,
        '好奇心':5,'保守':-10,'倒错':10,
        '献身':5,'难以逾越的底线':-15,'无节操':5,
        '不知耻':5,'怕羞':-5,'纯情':-5,'好色':15,
        '忧郁':-5,'狂乱':999,'崩坏':999,'幼儿退化':999,
        '欲望压抑':-5,'欲望解放':5,
        '慕恋':10,'亲爱':20,'相爱':30,'服从':10,'隶属':30,'烙印':20,
        '妄信':30,'淫乱':20,'怕痛':-5,'耐痛':5,
    }
    mark_check_list={
        '苦痛刻印': 5, '快乐刻印': 5, '屈服刻印': 5, '药毒刻印': 5, 
        '羞耻刻印': 3, '恐惧刻印': 5, '反发刻印': -12, '同化刻印': 5
        }
    
    grade = 0
    detail_list={}
    if develop['服从']>0:
        grade += develop['服从']*grade_for_obey
        detail_list['服从'] = develop['服从']*grade_for_obey
    if develop['欲望']>0:
        grade += develop['欲望']*grade_for_desire
        detail_list['欲望'] = develop['欲望']*grade_for_desire
    if develop['侍奉欲望']>0:
        grade += develop['侍奉欲望']*grade_for_serve
        detail_list['侍奉欲望'] = develop['侍奉欲望']*grade_for_serve

    for i in pl_check_list:
        if search_quaility(c,i):
            grade += pl_check_list[i]
            detail_list[i] = pl_check_list[i]
    for i in mark_check_list:
        if mark[i]>0:
            grade += mark_check_list[i]
            detail_list['i'] = mark_check_list[i]
    grade = int(grade)
    return {'分数':grade,'细则':detail_list}

#身体开发计算
def cal_body_develop(c):
    develop = c['开发']
    mark = c['刻印']
    grade = 0
    detail_list = {}

    develop_check_list = {
        'C感觉': 5, 'V感觉': 5, 'B感觉': 5, 'A感觉': 5, 
        'M感觉':5, 'U感觉':5,'W感觉':5,
        'V扩张度':3,'A扩张度':3,'尿道扩张度':5,
    }
    times_check_list = {
        'V敏感':2,'A敏感':2,'C敏感':2,'B敏感':2,
        'M敏感':2,'U敏感':2,'V钝感':0.5,'A钝感':0.5,
        'C钝感':0.5,'B钝感':0.5,'M钝感':0.5,
        'U钝感':0.5,
    }
    quaility_check_list = {
        '腔射弱点':15,
        '肛射弱点':15,
        '饮精弱点':15,
        '尿道被射弱点':15,
        }
    product_list = {
        '淫壶':3,
        '淫核':3,
        '淫茎':3,
        '淫尻':3,
        '淫乳':3,
        '淫唇':3,
        '淫靡尿道':3,
        '淫靡子宫':3,
        '易湿':1.5,'不易湿':0.75,
        '肠液分泌体质':1.5,'呕吐反射耐性':1.5,
        '精爱味觉':3,'漏尿癖':2,'泌乳体质':3,'药毒耐性':0.5,
        '扩张适性':1.5,'快速回复':1.5,'病弱':0.5,'污臭敏感':0.5,
        '污臭钝感':1.5,
    }
    
    for i in develop_check_list:
        if develop[i]>0:
            grade+=develop_check_list[i]*develop[i]
            detail_list[i] = develop_check_list[i]*develop[i]
    for i in times_check_list:
        if search_quaility(c,i):
            target = i[0]
            if '{}感觉'.format(target) in detail_list:
                grade = grade - detail_list['{}感觉'.format(target)]
                grade = grade + detail_list['{}感觉'.format(target)]*times_check_list[i]
                if '敏感' in i:
                    detail_list['{}感觉(敏）'.format(target)] = detail_list['{}感觉'.format(target)]*times_check_list[i]
                elif '钝感' in i:
                    detail_list['{}感觉(钝）'.format(target)] = detail_list['{}感觉'.format(target)]*times_check_list[i]
                del detail_list['{}感觉'.format(target)]
    for i in quaility_check_list:
        if search_quaility(c,i):
            grade += quaility_check_list[i]
            detail_list[i] = quaility_check_list[i]  
    for i in product_list:
        if search_quaility(c,i):
            grade *= product_list[i]
            detail_list[i] = '*{}'.format(product_list[i])
    
    add = eject_check(c)
    grade += add[0]
    detail_list.update(add[1])
    grade = int(grade)
    return {'分数':grade,'细则':detail_list}

#榨精力计算
def cal_squeeze(c):
    develop = c['开发']
    mark = c['刻印']
    grade = 0
    detail_list = {}

    develop_check_list = {
        '指技':3,'舌技':5,'腰技':10,'足技':3,'魔乳':5,
        'V名器度':10, 'A名器度':10,'喉名器度':10,
        'S属性': 5, 'M属性': 5,
        }
    quaility_check_list = {
        '爱抚知识':5,'淫具知识':5,'淫药知识':5,
        '好为人师':5,'SM才能':5,'扩张知识':5,
        '魔法回路':10,'触手使役':10,'禁断知识':10,
        '洗脑知识':10,'饲育知识':10,
        'V名器':10,'A名器':10,
        'M名器':10,'喉性感':10,'子宫性感':10,'尿道性感':10,
    }
    product_list={
        '魅惑':2,'人气':3,'倾国':5,'煽动':2,
        '诱惑':3,'无知':0.5,
    }
    for i in quaility_check_list:
        if search_quaility(c,i):
            grade += quaility_check_list[i]
            detail_list[i] = quaility_check_list[i] 
    for i in develop_check_list:
        if develop[i]>0:
            grade+=develop_check_list[i]*develop[i]
            detail_list[i] = develop_check_list[i]*develop[i]
    for i in product_list:
        if search_quaility(c,i):
            grade *= product_list[i]
            detail_list[i] = '*{}'.format(product_list[i])
    grade = int(grade)
    return {'分数':grade,'细则':detail_list}

def cal_special(c):
    develop = c['开发']
    grade = 0
    detail_list = {}
    quaility_check_list = {
        '处女':30,'A处女':10,
        '性交成瘾':20,'被射成瘾':20,
        '储精依存':20,'自慰成瘾':20,
        '淫药成瘾':30,'受孕愿望':30,
        '便器愿望':30,'侍奉愿望':30,
        '饮精成瘾':30,'受虐欲':20,
        '施虐欲':20,'射乳成瘾':20,
        '射精成瘾':20,'排泄成瘾':20,
        '露出癖':20,'卖春成瘾':20,
        '音感':10,'音痴':-10,
        '料理苦手':-10,'料理得意':10,
        '善舞':10,'舞痴':-10,
        '摄影才能':10,
        '穿环':10,
    }
    develop_check_list = {
        '精液成瘾': 10, '自慰成瘾': 10, '药物成瘾': 10, 
        '被射中毒': 10, 
        '排泄成瘾': 10, '触手适性': 15, '兽交中毒': 15, 
        '受孕成瘾': 15,
        '百合中毒': 5, '男同中毒': 5, '喷乳中毒': 5, '射精中毒': 5,
    }
    product_list={
        '花魁':3,'教具':3,'性畜':3,'人气AV':3,
        '苗床':3,
        '淫药体质':3,'不孕不育':0.25,'苗床体质':3,
        '子宫柔软':2,
        '发情体质':2,'吸精体质':3,'种付体质':2,'精畜体质':3,
    }

    for i in develop_check_list:
        if develop[i]>0:
            grade+=develop_check_list[i]*develop[i]
            detail_list[i] = develop_check_list[i]
    for i in quaility_check_list:
        if search_quaility(c,i):
            grade += quaility_check_list[i]
            detail_list[i] = quaility_check_list[i]
    for i in product_list:
        if search_quaility(c,i):
            grade *= product_list[i]
            detail_list[i] = '*{}'.format(product_list[i])
    grade = int(grade)
    return {'分数':grade,'细则':detail_list}

def eject_check(c):
    grade = 0
    detail_list = {}
    if c['性别'] != '女性':
        p = c['身体信息']['阴茎']
        produce = p['生产速度']
        limit = p['容量']
        eject_rate = p['标准射出量']
        if produce != 0:
            grade += int(limit/10*(limit/produce)*eject_rate)
            detail_list['产精性能'] = int(limit/10*(limit/produce)*eject_rate)
    if c['性别'] != '男性':
        p = c['身体信息']['乳房']
        produce = p['生产速度']
        limit = p['容量']
        eject_rate = p['标准射出量']
        if produce != 0:
            grade += int(limit/10*(limit/produce)*eject_rate)
            detail_list['产乳性能'] = int(limit/10*(limit/produce)*eject_rate)
    return [grade,detail_list]
