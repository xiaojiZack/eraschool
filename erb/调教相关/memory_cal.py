import erajs.api as a
from ..人物相关.character_class import search_quaility as sq

def memory_cal(c):
    memory_list = c['调教记忆']
    m = c['待处理记忆']
    ml = {
        '快C':0, '快V':0, '快B':0, '快A':0, '快M':0, '快P':0, '快W':0,
        '习得':0, '恭顺':0, '欲情':0, '屈服':0, 
        '羞耻':0, '苦痛':0, '恐惧':0, '药毒':0, '同化':0, '主导':0,
        }
    l = {
        '癔病':{'恐惧':2,'屈服':2},
        '反抗':{'*':0.75,'反感':2},
        '刚强':{'苦痛':0.75,'恐惧':0.75,'屈服':0.5},
        '顺从':{'屈服':1.5,'恭顺':1.5},
        '孩子气':{'恐惧':1.5,'反感':1.5,'欲情':1.5},
        '幼稚':{'恐惧':2,'反感':2,'欲情':2},
        '傲慢':{'屈服':0.5,'恭顺':0.5,'羞耻':1.5,'反感':1.5,'主导':1.5},
        '自卑':{'屈服':1.5,'恭顺':1.5,'反感':0.75,'主导':0.25},
        '自制':{'欲情':0.25,'药毒':0.25},
        '容易成瘾':{'欲情':1.5,'药毒':1.5},
        '纵欲':{'欲情':2,'药毒':2},
        '不关心':{'*':0.75,'反感':0.75},
        '淡漠':{'*':0.5,'反感':0.5},
        '乐观':{'恐惧':0.75,'屈服':0.75,'反感':0.75},
        '悲观':{'恐惧':1.5,'屈服':1.5,'反感':1.5},
        '献身':{'主导':1.5,'屈服':1.5,'恭顺':1.5},
        '难以逾越的底线':{'反感':1.5},
        '欲望压抑':{'欲情':0.5},
        '欲望解放':{'欲情':1.5},
        '不知耻':{'羞耻':0.5},
        '怕羞':{'羞耻':1.5},
        '小恶魔':{'主导':1.5,'屈服':0.75},
        '喜欢受人注目':{'羞耻':0.5},
        '承认快感':{'快C':1.5, '快V':1.5, '快B':1.5, '快A':1.5, '快M':1.5, '快P':1.5, '快W':1.5,},
        '否定快感':{'快C':0.75, '快V':0.75, '快B':0.75, '快A':0.75, '快M':0.75, '快P':0.75, '快W':0.75,},
        'V敏感':{'快V':1.5},
        'A敏感':{'快A':1.5},
        'C敏感':{'快C':1.5},
        'B敏感':{'快B':1.5},
        'M敏感':{'快M':1.5},
        'P敏感':{'快P':1.5},
        'V钝感':{'快V':0.5},
        'A钝感':{'快A':0.5},
        'C钝感':{'快C':0.5},
        'B钝感':{'快B':0.5},
        'M钝感':{'快M':0.5},
        'P钝感':{'快P':0.5},
        '怕痛':{'苦痛':1.5},
        '耐痛':{'苦痛':0.5},
        '聪慧':{'习得':1.5},
        '愚笨':{'习得':0.5},
        '药毒耐性':{'药毒':0.25},
        '淫药成瘾':{'药毒':2},
        '侍奉愿望':{'主导':1.5,'屈服':1.5,'恭顺':1.5},
        '性交成瘾':{'快C':2, '快V':2, '快B':2, '快A':2, '快M':2, '快P':2, '快W':2,},
        '受虐欲':{'反感':0.75},
        '施虐欲':{'主导':1.25},
        '恋慕':{'反发':0.5,'恭顺':2,'欲情':1.5,'屈服':1.25,'恐惧':0.5},
        '亲爱':{'反发':0.25,'恭顺':3,'欲情':2,'屈服':1.5,'恐惧':0.25},
        '相爱':{'反发':0,'恭顺':4,'欲情':3,'屈服':2,'恐惧':0},
        '服从':{'反发':0.5,'恭顺':1.25,'欲情':1.5,'屈服':2,'恐惧':1.25},
        '烙印':{'反发':0,'恭顺':1.5,'欲情':2,'屈服':3,'恐惧':1.25},
        '隶属':{'反发':0,'恭顺':2,'欲情':3,'屈服':4,'恐惧':0},
        '妄信':{'反发':0,'恭顺':4,'欲情':3,'屈服':4,'恐惧':0},
        '淫乱':{'快C':1.5, '快V':1.5, '快B':1.5, '快A':1.5, '快M':1.5, '快P':1.5, '快W':1.5,'恭顺':1.5, '欲情':1.5, '屈服':1.5, 
        '羞耻':0.5, '药毒':1.5, '同化':2, '主导':1.5,},
        '淫壶':{'快V':2},
        '淫核':{'快C':2},
        '淫茎':{'快C':2},
        '淫尻':{'快A':2},
        '淫乳':{'快B':2},
        '淫唇':{'快M':2},
        '淫靡尿道':{'快P':2},
        '淫靡子宫':{'快W':2},
        }
    
    for q in l:
        if sq(c,q):
            for j in l[q]:
                if j != '*':
                    m[j] = m[j]*l[q][j]
                else:
                    for k in ml:
                        m[k] = m[k]*l[q][j]

    
    #体液分泌
    sum_list = ['快C', '快V', '快B', '快A', '快M', '快P', '快W','欲情']
    sumup = 0
    for i in sum_list:
        sumup = sumup + m[i]
    if sumup<100000:
        sumup = sumup/10
    else:
        sumup = 10000
    m['V润'] = sumup
    m['A润'] = sumup

    l = {
        '肠液分泌体质':{'A润':1},
        '易湿':{'V润':1.5,'A润':1.5},
        '不易湿':{'V润':0.5,'A润':0.5},
        '淫乱':{'V润':1.5,'A润':1.5}
    }
    for q in l:
        if sq(c,q):
            for j in l[q]:
                if j != '*':
                    m[j] = m[j]*l[q][j]
                else:
                    for k in ml:
                        m[k] = m[k]*l[q][j]
    
    if (not sq(c,'肠液分泌体质')):
        m['A润'] = 0
    
    a.divider()
    a.t('{}:'.format(c['名字']))
    a.t()
    ml['反感'] = 0
    for i in ml:
        if m[i] != 0:
            a.t('{}:{} + {} = '.format(i, memory_list[i],m[i]))
            memory_list[i] = memory_list[i] + m[i]
            a.t('{}'.format(memory_list[i]))
            a.t()
            m[i] = 0
    c['调教记忆'] = memory_list
    c['待处理经验'] = m
    a.t('',True)
    return c