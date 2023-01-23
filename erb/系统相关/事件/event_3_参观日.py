import erajs.api as a

def event3():
    #参观日

    #根据学校名气度生成游客列表
    visitor_list = cal_visitor_size()

    #根据学生整体色情度生成额外倍率
    cloth_bouns = cloth_rate()

    #显示部分
    a.page()
    a.mode('grid',1)
    a.h('开放参观日')
    a.divider()
    a.mode()
    a.t('难得的开放参观日到了，今日预计的游客有:',wait=True)
    a.t()
    for visitor in visitor_list:
        a.t('-{}:{}人'.format(visitor,visitor_list[visitor]))
        a.t()
    a.t('',wait=True)
    color_level = ['#778899', '#7FFF00', '#FFFF00', '#FFC1C1', '#FF0000']
    a.t('由于学生的平均服装色情度产生的倍率为:')
    a.t('{}'.format(cloth_bouns['rate']),wait=True,style={'color':color_level[cloth_bouns['level']]})
    a.t(',今天是难得的日子，请好好努力吧。',wait=True)
    a.t()
    
    #TODO
    #开放参观日特殊活动

    #TODO
    #建筑加成
    bb = building_bouns()

    bouns = {
        'money_bouns':cloth_bouns['rate']*bb['money_bouns'],
        'fame_bouns':cloth_bouns['rate']*bb['fame_bouns'],
        }
    reward = cal_reward(visitor_list,bouns)
    a.t('',wait=True)

    #TODO
    #特殊事件

def cal_visitor_size():
    fame = a.sav()['学院名气度']

    visitor_list = {}

    visitor_list['普通人'] = int(fame*0.5)+1
    if fame>100:
        visitor_list['慕名而来的人'] = int(fame*0.25)+1
    if fame>1000:
        visitor_list['来自全国各地的名流'] = int(fame*0.1)+1
    if fame>10000:
        visitor_list['显赫权贵'] = int(fame*0.01)+1
    
    return visitor_list

def cal_reward(visitor_list, bouns):
    money = 0
    fame = 0
    for v in visitor_list:
        if v == '普通人':
            money += visitor_list[v]*500
            fame += visitor_list[v]*0.5
        elif v == '慕名而来的人':
            money += visitor_list[v]*1000
            fame += visitor_list[v]*1
        elif v == '来自全国各地的名流':
            money += visitor_list[v]*5000
            fame += visitor_list[v]*2
        elif v == '显赫权贵':
            money += visitor_list[v]*10000
            fame += visitor_list[v]*5
    
    money = money*bouns['money_bouns']
    fame = fame*bouns['fame_bouns']
    
    a.sav()['资源']['金钱'] += money
    a.sav()['学院名气度'] += fame
    a.t('在{}金钱倍率，{}声望倍率下，'.format(bouns['money_bouns'],bouns['fame_bouns']))
    a.t('本次参观日共收到资助:{}G，'.format(money))
    a.t('名气度上升+{}'.format(fame))

    return {'money':money,'fame':fame}

def building_bouns():
    #部分固定设施bouns
    money_bouns = 1
    fame_bouns = 1

    building_list = a.sav()['校内建筑列表']
    for b in building_list:
        bname = b['名称']
        if bname == '广播站':
            fame_bouns=fame_bouns*1.05
        elif bname == '舞台':
            pass
        elif bname == '咖啡厅':
            pass
        elif bname == '娼馆':
            pass
        elif bname == '直播室':
            pass
        elif bname == '展览':
            pass
        elif bname == '便器屋':
            pass
        elif bname == '牧场':
            pass
        elif bname == '苗床馆':
            pass
        elif bname == '处刑台':
            pass
    
    return {'money_bouns':money_bouns,'fame_bouns':fame_bouns}

#不同季节的参观日
def event3_1():
    event3()
def event3_2():
    event3()
def event3_3():
    event3()

def cloth_rate():
    #计算学生的色情度加成
    student_list = a.sav()['character_list']['学生']
    beauty = 0
    mean_beauty = 0
    max_beauty = 0
    for student_id in student_list:
        student = student_list[student_id]
        beauty += student['衣物效果']['色情度']
        max_beauty = max(max_beauty, beauty)
    mean_beauty = int(beauty/len(student_list))

    rate_bouns = [1,1.2,1.5,1.8,2,3]
    rate_level = [150, 300, 500, 800, 1400]
    level = 0
    while rate_level[level]<mean_beauty and level<4:
        level += 1
    return {'rate':rate_bouns[level], 'level':level, 'max':max_beauty}