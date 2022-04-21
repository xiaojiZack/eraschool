import time
import erajs.api as a

#插入时，插入尺寸的计算不会影响能否插入，但是会触发警告和惩罚
P_size_trans = {'迷你根':1,'小根':3,'手指':2,'普通根':4,'巨根':6,'手臂尺寸':8,'马根':9,'龙根':10}

def size_warning():
    def undo_flag():
        a.tmp()['调教数据']['尺寸警告标志'] = False
        a.msg('尺寸警报已关闭')
        a.tmp()['尺寸警报确认中'] = False
    def mercy():
        a.tmp()['尺寸警报确认中'] = False
    a.page()
    a.mode()
    l = a.tmp()['调教数据']['参与者']
    pname = ''
    for i in l:
        if i['CharacterId'] == a.tmp()['调教数据']['被调教']:
            pname = i['名字']
    a.h('警告!')
    a.t()
    a.t('对于{}来说，怎么想都进不去吧，即使这样也要强行继续吗?'.format(pname))
    a.t()
    a.b('残酷调教',undo_flag)
    a.t()
    a.b('仁慈放过',mercy)

def check_size(body_size,be_insert_size,have_inserted):
    #be_insert_size:扩张等级，insert_size:插入物的尺寸，have_inserted:已经插入的占用物品(字典)
    temp = body_size
    for i in have_inserted:
        temp -= P_size_trans[have_inserted[i]]
    if temp<P_size_trans[be_insert_size]:
        if a.tmp()['调教数据']['尺寸警告标志']:
            size_warning()
            a.tmp()['尺寸警报确认中'] = True
            while a.tmp()['尺寸警报确认中']:
                time.sleep(0.1)
        return False
    else:
        return True

def check_maintain_size(body_size,have_inserted):
    #be_insert_size:扩张等级，have_inserted:已经插入的占用物品(字典)
    #检查目前是否超过
    temp = body_size
    for i in have_inserted:
        temp -= P_size_trans[have_inserted[i]]
    if temp<0:
        if a.tmp()['调教数据']['尺寸警告标志']:
            size_warning()
            a.tmp()['尺寸警报确认中'] = True
            while a.tmp()['尺寸警报确认中']:
                time.sleep(0.1)
        return False
    else:
        return True

def size_punish(c,place):
    c['待处理记忆']['恐惧'] += 2000
    c['待处理记忆']['苦痛'] += 2000
    c['待处理记忆']['反感'] += 1000
    c['待处理经验']['{}扩张经验'.format(place)] += 1
