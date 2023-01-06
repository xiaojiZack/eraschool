import math
import erajs.api as a
from erb.系统相关.调教相关.体力衰减 import decrease_pp
from erb.系统相关.调教相关.液体 import liquid_updata
from ..人物相关.character_class import search_quaility as sq
from .刻印获取 import mark_get
def memory_cal(c):
    memory_list = c['调教记忆']
    m = c['待处理记忆']
    ml = {
        '快C':0, '快V':0, '快B':0, '快A':0, '快M':0, '快U':0, '快W':0,
        '习得':0, '恭顺':0, '欲情':0, '屈服':0, 
        '羞耻':0, '苦痛':0, '恐惧':0, '药毒':0, '同化':0, '主导':0,
        'V润':0,'A润':0
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
        '承认快感':{'快C':1.5, '快V':1.5, '快B':1.5, '快A':1.5, '快M':1.5, '快U':1.5, '快W':1.5,},
        '否定快感':{'快C':0.75, '快V':0.75, '快B':0.75, '快A':0.75, '快M':0.75, '快U':0.75, '快W':0.75,},
        'V敏感':{'快V':1.5},
        'A敏感':{'快A':1.5},
        'C敏感':{'快C':1.5},
        'B敏感':{'快B':1.5},
        'M敏感':{'快M':1.5},
        'P敏感':{'快U':1.5},
        'V钝感':{'快V':0.5},
        'A钝感':{'快A':0.5},
        'C钝感':{'快C':0.5},
        'B钝感':{'快B':0.5},
        'M钝感':{'快M':0.5},
        'P钝感':{'快U':0.5},
        '怕痛':{'苦痛':1.5},
        '耐痛':{'苦痛':0.5},
        '聪慧':{'习得':1.5},
        '愚笨':{'习得':0.5},
        '药毒耐性':{'药毒':0.25},
        '淫药成瘾':{'药毒':2},
        '侍奉愿望':{'主导':1.5,'屈服':1.5,'恭顺':1.5},
        '性交成瘾':{'快C':2, '快V':2, '快B':2, '快A':2, '快M':2, '快U':2, '快W':2,},
        '受虐欲':{'反感':0.75},
        '施虐欲':{'主导':1.25},
        '恋慕':{'反发':0.5,'恭顺':2,'欲情':1.5,'屈服':1.25,'恐惧':0.5},
        '亲爱':{'反发':0.25,'恭顺':3,'欲情':2,'屈服':1.5,'恐惧':0.25},
        '相爱':{'反发':0,'恭顺':4,'欲情':3,'屈服':2,'恐惧':0},
        '服从':{'反发':0.5,'恭顺':1.25,'欲情':1.5,'屈服':2,'恐惧':1.25},
        '烙印':{'反发':0,'恭顺':1.5,'欲情':2,'屈服':3,'恐惧':1.25},
        '隶属':{'反发':0,'恭顺':2,'欲情':3,'屈服':4,'恐惧':0},
        '妄信':{'反发':0,'恭顺':4,'欲情':3,'屈服':4,'恐惧':0},
        '淫乱':{'快C':1.5, '快V':1.5, '快B':1.5, '快A':1.5, '快M':1.5, '快U':1.5, '快W':1.5,'恭顺':1.5, '欲情':1.5, '屈服':1.5, 
        '羞耻':0.5, '药毒':1.5, '同化':2, '主导':1.5,},
        '淫壶':{'快V':2},
        '淫核':{'快C':2},
        '淫茎':{'快C':2},
        '淫尻':{'快A':2},
        '淫乳':{'快B':2},
        '淫唇':{'快M':2},
        '淫靡尿道':{'快U':2},
        '淫靡子宫':{'快W':2},
        }
    
    liquid_updata(c)
    dr = c['药物效果']

    for q in l:
        if sq(c,q):
            for j in l[q]:
                if j != '*':
                    m[j] = m[j]*l[q][j]
                else:
                    for k in ml:
                        m[k] = m[k]*l[q][j]

    #根据开发程度产生的不同加成(待写)
    sence_part = ['C','V','B','A','M','U','W']
    sence_level = [1,2,4,10,20,40]
    develop_info = c['开发']
    for part in sence_part:
        m['快'+part] = m['快'+part]*sence_level[develop_info[part+'感觉']]*(1+dr['cy']) #催淫
    #侍奉欲望
    level_gain = [1,2,4,7.5,10,20]
    m['恭顺'] = m['恭顺']*level_gain[develop_info['侍奉欲望']]
    #欲情
    level_gain = [1,2,4,8,20,50]
    m['欲情'] = m['欲情']*level_gain[develop_info['欲望']]*dr['cy']
    #屈服
    level_gain = [1,2,4,8,20,50]
    m['屈服'] = m['屈服']*level_gain[develop_info['服从']]*dr['cy']
    #施虐狂
    level_gain = [1,1.5,2,5,10,30]
    m['主导'] = m['主导'] * m['主导']*level_gain[develop_info['S属性']]*(1/(dr['mz']+1))
    m['欲情'] = m['欲情'] + m['主导']*level_gain[develop_info['S属性']]
    #受虐狂
    level_gain = [1,1.5,2,5,10,30]
    m['屈服'] = m['屈服'] + m['苦痛']*level_gain[develop_info['M属性']]
    m['欲情'] = m['欲情'] + m['苦痛']*level_gain[develop_info['M属性']]
    m['苦痛'] = m['苦痛'] * max(0.2,(2-level_gain[develop_info['M属性']]))*(1/(dr['mz']+1)) #麻醉
    #露出癖
    level_gain = [1,1.5,2,5,10,30]
    m['屈服'] = m['屈服'] + m['羞耻']*level_gain[develop_info['露出癖']]
    m['欲情'] = m['欲情'] + m['羞耻']*level_gain[develop_info['露出癖']]
    m['羞耻'] = m['羞耻']*max(0.2,(2-level_gain[develop_info['露出癖']]))

    #反感降低计算
    m['反感'] += (m['苦痛']+m['羞耻']+m['恐惧'])/10
    decrease_hate_quility = {'恋慕':0.25,'亲爱':0.1,'相爱':0,'服从':0.25,'烙印':0.1,'隶属':0,'妄信':0}
    for i in decrease_hate_quility:
        if sq(c,i):
            m['反感'] = m['反感']*decrease_hate_quility[i]
    m['反感'] = m['反感']*math.exp(-1*(c['好感度']/100))

    #各项记忆导致的好感度调整
    negative_emotion = c['调教记忆']['反感'] + c['调教记忆']['恐惧']
    if negative_emotion < 500:
        m['好感度'] = m['好感度']
    elif negative_emotion < 1000:
        m['好感度'] = m['好感度'] - 1
    elif negative_emotion < 10000:
        m['好感度'] = m['好感度'] - 5
    else:
        m['好感度'] = m['好感度'] - 10
    positive_emotion = 0
    for emotion in ['快C', '快V', '快B', '快A', '快M', '快U', '快W','欲情','屈服','恭顺']:
        positive_emotion = positive_emotion + c['调教记忆'][emotion]
    if positive_emotion < 5000:
        m['好感度'] = m['好感度']
    elif positive_emotion < 10000:
        m['好感度'] = m['好感度'] + 1
    elif positive_emotion < 50000:
        m['好感度'] = m['好感度'] + 5
    else:
        m['好感度'] = m['好感度'] + 10
    
    #体液分泌
    sum_list = ['快C', '快V', '快B', '快A', '快M', '快U', '快W','欲情','苦痛']
    sumup = 0
    for i in sum_list:
        sumup = sumup + m[i]*0.1
    if sumup<100000:
        sumup = sumup
    else:
        sumup = 10000
    m['V润'] = sumup
    m['A润'] = sumup

    l = {
        '肠液分泌体质':{'A润':1},
        '易湿':{'V润':1.5,'A润':1.5},
        '不易湿':{'V润':0.5,'A润':0.5},
        '淫乱':{'V润':2,'A润':2}
    }
    for q in l:
        if sq(c,q):
            for j in l[q]:
                if j != '*':
                    m[j] = m[j]*l[q][j]
                else:
                    for k in ml:
                        m[k] = m[k]*l[q][j]
    #射精槽计算
    c['待处理记忆'] = m
    eject_semen_cal(c)

    if (not sq(c,'肠液分泌体质')):
        m['A润'] = 0
    
    #获取刻印
    mark_get(c,m)

    flag = False
    for i in m:
        if m[i] >=1:
            flag = True
            break
    if flag:
        a.t()
        ml['反感'] = 0
        for i in ml:
            if m[i] != 0:
                m[i] = int(m[i])
                a.t('{}:{} + {} = '.format(i, memory_list[i],m[i]))
                memory_list[i] = memory_list[i] + m[i]
                a.t('{}'.format(memory_list[i]))
                a.t()
                m[i] = 0
        cal_favor(c,[m['好感度'],m['侍奉快乐']])
        c['调教记忆'] = memory_list
        c['待处理记忆'] = m
        a.t('',True)
    return c

#计算射精槽
def eject_semen_cal(c):
    if c['性别'] == '女性':
        return False
    else:
        sumup = 0
        for i in ['V','A','M','B','C','W','U']:
            sumup += c['待处理记忆']['快{}'.format(i)]
        sumup += c['待处理记忆']['欲情']
        c['其他参数']['射精数值'] += sumup

#经验处理
def exp_cal(c):
    e = c['待处理经验']
    for i in e:
        if e[i] != 0:
            e[i] = int(e[i])
            a.t('{}:+{} '.format(i, e[i]))
            c['经验'][i] = c['经验'][i] + e[i]
            a.t()
            e[i] = 0
    c['待处理经验'] = e

def pp_cal(c):
    decrease_pp(c,c['待处理体力变化'])
    c['待处理体力变化'] = [0,0,0]

def cal_favor(c,data):
    if c['CharacterId'] == 0:
        return False
    if data == []:
        return 0
    c['好感度'] += data[0]
    c['侍奉快乐'] += data[1]
    if data[0] != 0:
        a.t('好感度+({})'.format(data[0]))
    if data[1] != 0:
        a.t(' 侍奉快乐+({})'.format(data[1]))
    c['待处理记忆']['好感度'] = 0
    c['待处理记忆']['侍奉快乐'] = 0

def special_bouns(c):
#多穴插入bouns，被虐快乐，施虐快乐，
    insert_count = 0
    if c != '男性':
        if len(c['身体信息']['阴道']['内容固体']) >0:
                insert_count += 1
    if len(c['身体信息']['肛门']['内容固体'])>0:
        insert_count += 1
    if len(c['身体信息']['尿道']['内容固体'])>0:
        insert_count += 1
    if len(c['身体信息']['口喉']['内容固体'])>0:
        insert_count += 1
    if insert_count >= 2:
        l = ['快V','快A','快U','屈服','恭顺','欲情']
        number_trans = {2:'二',3:'三',4:'四'}
        a.t()
        a.t('{}被{}穴插入 额外奖励   '.format(c['名字'],number_trans[insert_count]), style = {'color':'#FFC1C1'})
        for i in l:
            if c['待处理记忆'][i]>0:
                c['待处理记忆'][i] = c['待处理记忆'][i] * pow(1.5,number_trans)
    
    if c['待处理经验']['饮精经验']>0 and (c['待处理经验']['绝顶经验']>0 or c['待处理经验']['射精经验']>0):
        a.t()
        a.t('饮精绝顶({}) 额外奖励  '.format(c['名字']),style = {'color':'#FFC1C1'})
        bouns_list = ['M','恭顺','屈服','欲情','侍奉快乐']
        for i in bouns_list:
            c['待处理记忆'][i] = c['待处理记忆'][i] * pow(1.5,c['开发']['精液中毒']+max(c['待处理经验']['饮精经验'],c['待处理经验']['绝顶经验']))
    
    if c['待处理记忆']['苦痛']>100:
        sumup=0
        sum_list = ['快C', '快V', '快B', '快A', '快M', '快U', '快W']
        c['待处理经验']['被虐快乐经验'] = 0
        for i in sum_list:
            sumup += c['待处理记忆'][i]
        while sumup > 0:
            sumup -= 1000*2^c['待处理经验']['被虐快乐经验']
            c['待处理经验']['被虐快乐经验']+=1
    
    if c['待处理记忆']['主导']>100:
        sumup=0
        sum_list = ['快C', '快V', '快B', '快A', '快M', '快U', '快W']
        c['待处理经验']['施虐快乐经验'] = 0
        for i in sum_list:
            sumup += c['待处理记忆'][i]
        while sumup > 0:
            sumup -= 1000*2^c['待处理经验']['施虐快乐经验']
            c['待处理经验']['施虐快乐经验']+=1
    
    if c['待处理记忆']['侍奉快乐'] >0:
        sumup=0
        sum_list = ['快C', '快V', '快B', '快A', '快M', '快U', '快W']
        c['待处理经验']['施虐快乐经验'] = 0
        for i in sum_list:
            sumup += c['待处理记忆'][i]
        while sumup > 0:
            sumup -= 1000*2^c['待处理经验']['施虐快乐经验']
            c['待处理记忆']['侍奉快乐']+=1



def all_cal(c):
    pp_cal(c)
    memory_cal(c)
    exp_cal(c)
    