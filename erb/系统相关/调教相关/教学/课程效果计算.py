import erajs.api as a

def cal_course_effect(c,course_tag,course_difficulty):
    #根据输入的角色数据计算
    dev_list = c['开发']
    exp_list = c['经验']
    obey_point = 0

    #服从
    obey_level = [0,10,20,50,100,200]
    obey_point = obey_point+obey_level[dev_list['服从']]

    #欲望
    obey_level = [0,10,20,50,100,200]
    obey_point = obey_point+obey_level[dev_list['欲望']]

    #tag:侍奉
    if '侍奉' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['侍奉欲望']]
    
    #tag:V
    if 'V' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['V感觉']]

    #tag:A
    if 'A' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['A感觉']] 

    #tag:C
    if 'C' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['C感觉']]   
    
    #tag:M
    if 'M' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['M感觉']]
    
    #tag:B
    if 'B' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['B感觉']]
    
    #tag:W
    if 'W' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['W感觉']]
    
    #tag:U
    if 'U' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['U感觉']]
    
    #tag:露出
    if '露出' in course_tag:
        obey_level = [-20,0,20,40,80,150]
        obey_point = obey_point+obey_level[dev_list['露出癖']]
    
    #tag:精液
    if '精液' in course_tag:
        obey_level = [-20,0,20,40,100,200]
        obey_point = obey_point+obey_level[dev_list['精液成瘾']]
        
    #tag:受虐
    if '受虐' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['M属性']]
    
    #tag:施虐
    if '施虐' in course_tag:
        obey_level = [-20,0,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['S属性']]
    
    #tag:自慰
    if '自慰' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['自慰成瘾']]
    
    #tag:被射
    if '被射' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['被射中毒']]
    
    #tag:射精
    if '射精' in course_tag:
        obey_level = [0,10,20,50,100,200]
        obey_point = obey_point+obey_level[dev_list['射精中毒']]
    
    #tag:喷乳
    if '喷乳' in course_tag:
        obey_level = [0,20,40,80,120,200]
        obey_point = obey_point+obey_level[dev_list['喷乳成瘾']]
    
    #tag:药物
    if '药物' in course_tag:
        obey_level = [-20,0,40,80,120,200]
        obey_point = obey_point+obey_level[dev_list['药物成瘾']]
    
    #tag:排泄
    if '排泄' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['排泄成瘾']]
    
    #tag:兽交
    if '兽交' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['兽交中毒']]

    #tag:触手
    if '触手' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['触手适性']]

    #tag:受孕
    if '受孕' in course_tag:
        obey_level = [-40,-20,0,20,50,100]
        obey_point = obey_point+obey_level[dev_list['受孕成瘾']]
    
    #体力、理智修正
    if (c['体力值']/c['最大体力值']) < 0.25:
        obey_point = obey_point*0.75
    if (c['理智值']/c['最大理智值']) < 0.25:
        obey_point = obey_point*0.75

    if obey_point < course_difficulty:
        return 'C'
    elif obey_point < 2*course_difficulty:
        return 'B'
    elif obey_point < 3*course_difficulty:
        return 'A'
    elif obey_point < 4*course_difficulty:
        return 'S'
    elif obey_point < 5*course_difficulty:
        return 'SS'
    else:
        return 'SSS'