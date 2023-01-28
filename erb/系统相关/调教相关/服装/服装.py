import erajs.api as a
import random

from funcs import get_leading_character

def search_quaility(c,target):
    for i in c['属性']:
        for j in c['属性'][i]:
            if j == target:
                return True
    return False
sq = search_quaility

def init_cloth(cloth_name):
    #根据衣物名称生成衣物实体

    #衣物标准件
    cloth = {
        "名称":"标准件",
        "部位":"其他",
        "关键部位遮挡":{
            "阴部":True,"胸部":True,"肛门":True
            },
        "色情度":0,
        "羞耻度":0,
        "色情倍率":1,
        "遮挡下层":False,
        "前置":{
            '道具':'',
        },
        '描述':''
    }

    cloth_data = {}

    #寻找衣物数据
    for cloth_type in a.dat()['cloth_item']:
        for cloth_data_name in a.dat()['cloth_item'][cloth_type]:
            if cloth_data_name == cloth_name:
                cloth_data = a.dat()['cloth_item'][cloth_type][cloth_name]
                cloth_data['类别'] = cloth_type

    #衣物不存在
    if cloth_data == {}:
        return {}
    
    for cd in cloth_data:
        if cd == "关键部位遮挡":
            for i in cloth_data[cd]:
                cloth[cd][i] = cloth_data[cd][i]
        else:
            cloth[cd] = cloth_data[cd]
    cloth['名称'] = cloth_name
    
    
    return cloth

def cal_cloth_charm(cloth_list):
    #计算人物衣物效果值
    cloth_charm = 0
    cloth_unaccpection = 0
    charm_rate = 1
    
    #计算顺序
    cal_order = ['外部配件','全身','贴身全身','头部','面部','颈部','足部','上衣','下衣','贴身上衣','腿袜','贴身下衣','上部配件','下部配件']

    #可见衣物层
    visual_able = cal_order.copy()
    cloth = cloth_list['全身']
    if not cloth == {}:
        if cloth['遮挡下层']:
            for i in ['上衣','下衣','贴身上衣','贴身下衣','腿袜','上部配件','下部配件']:
                if i in visual_able: visual_able.remove(i)
    cloth = cloth_list['上衣']
    if not cloth == {}:
        if cloth['遮挡下层']:
            for i in ['贴身上衣','上部配件']:
                if i in visual_able: visual_able.remove(i)
    cloth = cloth_list['下衣']
    if not cloth == {}:
        if cloth['遮挡下层']:
            for i in ['贴身下衣','下部配件']:
                if i in visual_able: visual_able.remove(i)
    
    key_body_part = {
        '阴部':True,
        '胸部':True,
        '肛门':True
    }

    for cloth_type in cal_order:
        if '配件' in cloth_type:
            for cloth in cloth_list[cloth_type]:
                if cloth_list[cloth_type] == []: continue
                #衣物可见，色情度全算，羞耻度全算,倍率全算
                if cloth_type in visual_able:
                    cloth_charm += cloth['色情度']
                    charm_rate *= cloth['色情倍率']
                    cloth_unaccpection += cloth['羞耻度']
                else: #不可见，色情度0，羞耻度半算，倍率0
                    cloth_unaccpection += cloth['羞耻度']*0.5
                
                #关键部位遮挡
                for body_part in ['阴部','胸部','肛门']:
                    key_body_part[body_part] = key_body_part[body_part] and (not cloth['关键部位遮挡'][body_part])
        else:
            cloth = cloth_list[cloth_type]
            if cloth == {}: continue
            #衣物可见，色情度全算，羞耻度全算,倍率全算
            if cloth_type in visual_able:
                cloth_charm += cloth['色情度']
                charm_rate *= cloth['色情倍率']
                cloth_unaccpection += cloth['羞耻度']
            else: #不可见，色情度0，羞耻度半算，倍率0
                cloth_unaccpection += cloth['羞耻度']*0.5
            
            #关键部位遮挡
            for body_part in ['阴部','胸部','肛门']:
                key_body_part[body_part] = key_body_part[body_part] and (not cloth['关键部位遮挡'][body_part])
    
    #关键部位加成
    if key_body_part['阴部']:
        cloth_charm += 500
        cloth_unaccpection += 500
    if key_body_part['胸部']:
        cloth_charm += 300
        cloth_unaccpection += 300
    if key_body_part['肛门']:
        cloth_charm += 200
        cloth_unaccpection += 200
    
    #真空
    if cloth_list['贴身上衣'] == {} and not '贴身上衣' in visual_able:
        cloth_unaccpection += 40
    if cloth_list['贴身下衣'] == {} and not '贴身下衣' in visual_able: 
        cloth_unaccpection += 70
    
    #贴身衣物可见
    for i in visual_able:
        if ('贴身上衣' == i or '贴身下衣' == i) and cloth_list['贴身全身'] == {}:
            cloth_charm += 50
            cloth_unaccpection += 100
    
    cloth_charm *= charm_rate

    #色情度评级
    rate = ''
    if cloth_charm < 150:
        rate ='E'
    elif cloth_charm < 300:
        rate = 'D'
    elif cloth_charm < 500:
        rate = 'C'
    elif cloth_charm < 800:
        rate = 'B'
    elif cloth_charm < 1200:
        rate = 'A'
    else:
        rate = 'S'

    return {
        '色情度':int(cloth_charm), 
        '羞耻度':int(cloth_unaccpection), 
        '评级':rate,
        '关键部位':key_body_part
        }

def cal_accpection(c):
    #影响羞耻衣服接受能力的因素:服从、欲望、露出癖
    #基础值
    accpection = 30

    #服从对于接受能力的影响
    obey_accp = [0,50,100,150,200,300]

    #欲望对于接受能力的影响
    desire_accp = [0,50,100,150,200,300]

    #露出癖对于接受能力的影响
    exhibition_accp = [0,60,120,200,300,500]

    accpection += obey_accp[c['开发']['服从']]
    accpection += desire_accp[c['开发']['欲望']]
    accpection += exhibition_accp[c['开发']['露出癖']]

    if sq(c,'好色') or sq(c,'不知耻') or sq(c, '喜欢受人注目'):
        accpection += 30

    return accpection

def creat_normal_cloth(c):
    #对于新生成的人物创建一般的衣物
    if not c['性别'] == '男性':
        cloth_list = {
            '头部':{},
            '面部':{},
            '颈部':{},
            '上衣':'制服',
            '贴身上衣':'胸罩',
            '上部配件':[],
            '下衣':'长裙',
            '贴身下衣':'三角内裤',
            '下部配件':[],
            '全身':{},
            '贴身全身':{},
            '腿袜':'短袜',
            '足部':'平板鞋',
            '外部配件':[]
        }

        #根据人物素质随机一部分衣物？
        if sq(c,'好色') or sq(c,'不知耻') or sq(c, '喜欢受人注目'):
            ranint = random.random()
            if ranint<0.2:
                cloth_list['头部'] = '发卡'
                cloth_list['下衣'] = '迷你裙'
                cloth_list['贴身上衣'] = '蕾丝胸罩'
            if ranint <0.05:
                cloth_list['贴身上衣'] = {}
            if ranint <0.01:
                cloth_list['贴身下衣'] = {}
    else:
        cloth_list = {
            '头部':{},
            '面部':{},
            '颈部':{},
            '上衣':'制服',
            '贴身上衣':{},
            '上部配件':[],
            '下衣':'长裤',
            '贴身下衣':'四角内裤',
            '下部配件':[],
            '全身':{},
            '贴身全身':{},
            '腿袜':'短袜',
            '足部':'平板鞋',
            '外部配件':[]
        }
    for cloth_type in cloth_list:
        if '配件' in cloth_type:
            new_cloth = []
            for cloth_name in cloth_list[cloth_type]:
                new_cloth.append(init_cloth(cloth_name))
            cloth_list[cloth_type] = new_cloth
            continue
    
        if cloth_list[cloth_type] == {}: continue
        cloth_list[cloth_type] = init_cloth(cloth_list[cloth_type])
    
    c['衣物'] = cloth_list
    c['设定衣物'] = cloth_list
    c['衣物效果'] = cal_cloth_charm(cloth_list)

    return c

def cloth_rate_color(c):
    rate = c['衣物效果']['评级']
    if rate == 'E':
        color = '#778899' #亮灰
    elif rate == 'D':
        color = '#008000' #绿色
    elif rate == 'C':
        color = '#FFFF00' #黄色
    elif rate == 'B':
        color = '#FFC1C1' #粉红
    elif rate == 'A':
        color = '#FF0000' #红色
    else:
        color = '#CD00CD' #紫色
    return {'color':color}

def updata_cloth(c):
    cloth_list = c['衣物']
    make_equipment_effect(c,cloth_list)
    c['衣物效果'] = cal_cloth_charm(cloth_list)
    check_suit(c)

def check_cloth_allow(c, cloth):
    #检查衣物条件
    f = True
    if "体质" in cloth['前置']:
        if cloth['前置']['体质'] == '非处女':
            if ['处女'] in c['属性']['体质'] or c['性别'] == '男性':
                f = f and False
    if "开发" in cloth['前置']:
        for i in cloth['前置']['开发']:
            if c['开发'][i]>= cloth['前置']['开发'][i]:
                f = f and False
            else:
                f = f and True
    if cloth['前置']['道具'] == '':
        f = f and True
    else:
        if cloth['前置']['道具'] in list(a.sav()['物品'].keys()):
            if cloth['前置']['道具']>=1:
                f = f and True
        f = f and False
    return f

def cal_mean_beauty(cl):
    #计算平均魅力值
        total_beauty = 0
        for student_id in cl:
            student = cl[student_id]
            total_beauty += student['衣物效果']['色情度']
        mean_beauty = int(total_beauty/len(cl))
        return mean_beauty

#检查套装效果
def check_suit(c):
    clothes = c['衣物']
    c['衣物效果']['套装效果'] = ''
    #女仆装+女仆头饰：侍奉加成+咖啡厅收入加成
    if check_is_cloth(clothes['全身'],'女仆装') and check_is_cloth(clothes['头部'],'女仆头饰'):
        c['衣物效果']['套装效果'] = '女仆装'
    #体操服上衣+体操服下衣+运动鞋: 长跑、健美操加成
    if check_is_cloth(clothes['上衣'],'体操服上衣') and check_is_cloth(clothes['下衣'],'体操服下衣') and check_is_cloth(clothes['足部'],'运动鞋'):
        c['衣物效果']['套装效果'] = '体操服'
    #泳衣胸罩+泳衣裙：游泳效果上升
    if check_is_cloth(clothes['贴身上衣'],'泳衣胸罩') and check_is_cloth(clothes['贴身下衣'],'泳衣裙'):
        c['衣物效果']['套装效果'] = '泳装'
    #婚纱+婚礼头纱：好感度上升、恭顺上升、爱情
    if check_is_cloth(clothes['全身'],'婚纱') and check_is_cloth(clothes['头部'],'婚礼头纱'):
        c['衣物效果']['套装效果'] = '婚纱'
    #兔女郎/逆兔女郎+兔耳+兔尾肛塞
    if ((check_is_cloth(clothes['贴身全身'],'兔女郎') or check_is_cloth(clothes['贴身全身'],'逆兔女郎')) 
        and check_is_cloth(clothes['头部'],'兔耳') and check_is_cloth(clothes['下部配件'],'兔尾肛塞',True)):
        c['衣物效果']['套装效果'] = '兔女郎'
    #大衣+龟甲缚：露出癖上升
    if check_is_cloth(clothes['全身'],'大衣') and check_is_cloth(clothes['贴身全身'],'龟甲缚'):
        c['衣物效果']['套装效果'] = '露出狂'
    #怪兽头罩+怪兽套装+精液+配件：精液成瘾上升、反感上升、露出癖
    #TODO
    if check_is_cloth(clothes['全身'],'') and check_is_cloth(clothes['贴身全身'],'') and check_is_cloth(clothes['上衣'],'') and check_is_cloth(clothes['下衣'],'') and check_is_cloth(clothes['贴身上衣'],'') and check_is_cloth(clothes['贴身下衣'],''):
        c['衣物效果']['套装效果'] = '裸体'
    #裸体围裙
    if c['衣物效果']['套装效果'] =='裸体' and check_is_cloth(clothes['外部配件'],'围裙',True):
        c['衣物效果']['套装效果'] = '裸体围裙'
    
def check_is_cloth(cloth,target_cloth,multipe=False):
    #检查对应部位也没有穿目标衣物,multipe用于处理多配件情况
    if multipe == False:
        if target_cloth == '':
            if cloth == {}: return True
            else: return False
        else: 
            if cloth == {}: return False
            elif cloth['名称'] == target_cloth: return True
            else: return False
    else:
        if target_cloth == '':
            if cloth == []:return True
            else:return False
        else:
            if cloth == []:return False
            else:
                for c in cloth:
                    if c['名称'] == target_cloth: return True
                return False

def make_equipment_effect(c,cloth_list):
    #根据装备的配件效果，更新身体装具信息
    for cloth in cloth_list['外部配件']:
        pass
    for cloth in cloth_list['上部配件']:
        pass
    for cloth in cloth_list['上部配件']:
        if cloth['名称'] in ['震动棒','阴道跳蛋']:
            c['身体信息']['阴道']['内容固体'][cloth['名称']] = cloth['名称']
        if cloth['名称'] in ['肛门震动棒','肛塞','兔尾肛塞','猫尾肛塞','肛门拉珠','肛门跳蛋']:
            c['身体信息']['肛门']['内容固体'][cloth['名称']] = cloth['名称']

def reinit_cloth(c):
    #调教后重置衣物
    body = c['身体信息']
    body['肛门']['内容固体'] = {}
    body['尿道']['内容固体'] = {}
    body['口喉']['内容固体'] = {}
    body['子宫']['内容固体'] = {}
    body['阴道']['内容固体'] = {}
    c['衣物'] = c['设定衣物']
    if not c == get_leading_character():
        updata_cloth(c)