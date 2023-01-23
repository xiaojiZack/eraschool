import erajs.api as a
from erb.系统相关.口上相关.口上工具 import check_be_eject, check_eject, check_orgasm, check_special, comadd, comdoing, comundo, comfail, get_mark, pt, push_text

def kojosample(person, attenders, comnumber = 0, information = {}):
    #创建新口上时修改函数名'kojosample'为你喜欢的名字，请注意不要与其他口上重名
    #person 口上主角人物卡； attenders 发生口上时的伴随人物，一般为调教参与人员
    #comnumber 口上发生时的指令， information：携带信息
    p = person
    at = attenders
    com = comnumber
    inf = information
    e = person['经验']
    tm = person['调教记忆']
    mark = person['刻印']
    d = person['开发']
    b = person['身体信息']
    fav = person['好感度']
    #_______创建新口上时请复制本注释以上部分_______________

    #爱抚
    if (comnumber == 1 and comadd(inf) and fav<10 and d['C感觉']<1):
        #示范：当情景为[添加][‘爱抚’指令，指令编号1]且[好感度低于10]且[C感觉低于1]时
        push_text('此处为口上文本', style={'color':'#0f0'})
        #将口上'此处为口上文本'输出到口上输出序列，且颜色为绿色

        pt()
        #加入此函数以加入回车

    if (comnumber == 1 and comdoing(inf) and (d['C感觉']>=3 or mark['快乐刻印']>=1)):
        #示范：当情景为[持续执行][‘爱抚’指令，指令编号1]，且['C感觉'不小于3级]或['快乐刻印'不小于1]
        push_text('\"嗯哼哼哼啊啊啊啊啊啊啊啊啊!\"')
        #可以不携带style设定,用[\"]来在文本中输出"
        pt()
    
    if (check_orgasm(p,'C')>=2):
        #示范:当情景为[人物p，阴道‘V’绝顶不少于2次时]
        #函数check_orgasm()在不指定检查位置时可以用于仅检查人物是否高潮
        push_text('阴蒂绝顶了{}次'.format(check_orgasm(p,'C')))
        pt()
    
    if (check_eject(p)):
        #示范当情景为[人物p，射精时]
        res = check_eject(p)
        push_text('{}在{}的{}内射出了'.format(p['名字'],res['谁被射'],res['位置']))
        for liquid_type in res['液体']:
            push_text('{}ml的{},'.format(res['液体'][liquid_type],liquid_type))
        pt()
    
    if (check_be_eject(p)):
        res = check_be_eject(p)
        push_text('{}在{}的{}内射出了'.format(res['谁射'],p['名字'],res['位置']))
        for liquid_type in res['液体']:
            push_text('{}ml的{},'.format(res['液体'][liquid_type],liquid_type))
        pt()
    
    
    if (get_mark(inf,'反发刻印')==3):
        #示范当情景为[人物p获得反发刻印lv3]时
        push_text('请好好反省你自己的所作所为')
        pt()
    
    if (check_special(inf,'开场')):
        #示范：检查特殊事件示范包含‘开场’，可以替换为‘破处’‘结束调教’
        push_text('调教开场')
        pt()
    
    #示例，添加（comadd）命令“爱抚”（命令序列号为1）时给出口上
    if (comnumber == 1 and comadd(inf)):
        push_text('此处为口上文本', style={'color':'#0f0'})
        #将口上'此处为口上文本'输出到口上输出序列，且颜色为绿色

        pt()
        #加入此函数以加入回车
        push_text('此处为口上文本2', style={'color':'#0f0'})
        #将口上'此处为口上文本'输出到口上输出序列，且颜色为绿色

        pt()
        #加入此函数以加入回车
