import time
import erajs.api as a
from erb.系统相关.人物相关.character_class import search_quaility

#插入时，插入尺寸的计算不会影响能否插入，但是会触发警告和惩罚
P_size_trans = {'迷你根':1,'小根':3,'手指':2,'普通根':4,'巨根':6,'马根':8,'手臂尺寸':9,'龙根':10}

def pure_warning(body_type):
    def undo_flag():
        a.tmp()['调教数据']['破处警告标志'] = False
        a.msg('破处警报已关闭')
        a.tmp()['破处警报确认中'] = False
    def mercy():
        a.tmp()['破处警报确认中'] = False
    a.page()
    a.mode()
    l = a.tmp()['调教数据']['参与者']
    pname = ''
    for i in l:
        if i['CharacterId'] == a.tmp()['调教数据']['被调教']:
            pname = i['名字']
    a.h('警告!')
    a.t()
    pure_name = ''
    if body_type == 'V': pure_name = '处女'
    if body_type == 'A': pure_name = '肛门处女'
    if body_type == 'P': pure_name = '童贞'
    a.t('确定要将{}的{}夺走吗?'.format(pname,pure_name))
    a.t()
    a.b('是',undo_flag)
    a.t()
    a.b('否',mercy)

def check_pure(c,body_type):
    #be_insert_size:扩张等级，insert_size:插入物的尺寸，have_inserted:已经插入的占用物品(字典)
    flag = True
    if search_quaility(c,'处女') and body_type == 'V':
        flag = False
    if search_quaility(c,'A处女') and body_type == 'A':
        flag = False
    if search_quaility(c,'童贞') and body_type == 'P':
        flag = False
    if flag == False:
        if a.tmp()['调教数据']['破处警告标志']:
            pure_warning(body_type)
            a.tmp()['破处警报确认中'] = True
            while a.tmp()['破处警报确认中']:
                time.sleep(0.1)
        return False
    else:
        return True

def pure_punish(c,body_type):
    c['待处理记忆']['恐惧'] += 200
    c['待处理记忆']['苦痛'] += 300
    c['待处理记忆']['反感'] += 500
    text = ''
    if (body_type) == 'V': text = '处女'
    if (body_type) == 'A': text = 'A处女'
    if (body_type) == 'P': text = '童贞'
    a.msg('{}失去了[{}]'.format(c['名字'],text),style={'color':'#f00'})