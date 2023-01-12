import time
import erajs.api as a

def not_oil_warning(p,demand):
    flag = True
    a.tmp()['润滑警报确认中'] = False
    if a.tmp()['调教数据']['润滑警告标志'] and demand>=2:
        def undo_flag():
                a.tmp()['调教数据']['润滑警告标志'] = False
                a.msg('润滑警报已关闭')
                a.tmp()['润滑警报确认中'] = False
                flag = True
        def mercy():
            a.tmp()['润滑警报确认中'] = False
            flag = False
        a.tmp()['润滑警报确认中'] = True
        a.page()
        a.mode()
        pname = p['名字']
        a.h('警告!')
        a.t()
        a.t('对于{}来说，似乎还需要一些润滑来插入，即使这样也要强行继续吗?'.format(pname))
        a.t()
        a.b('残酷调教',undo_flag)
        a.t()
        a.b('仁慈放过',mercy)
    while(a.tmp()['润滑警报确认中']):
        time.sleep(0.1)
    return flag#返回能否执行后续操作

#通过输入的c来判断是否润滑不足，若润滑不足则返回不足程度
def is_enough_oiling(c,body_type,demand):
    if c['调教记忆']['{}润'.format(body_type)] <100:
        return demand-1
    elif c['调教记忆']['{}润'.format(body_type)]<1000:
        return demand-2
    elif c['调教记忆']['{}润'.format(body_type)]<3000:
        return demand-3
    else:
        return 0

def not_oiling_punish(c,degree):
    if degree == 3:
        c['待处理记忆']['苦痛'] += 3000
    elif degree == 2:
        c['待处理记忆']['苦痛'] += 1000
    elif degree == 1:
        c['待处理记忆']['苦痛'] += 100
    else:
        pass

def oiling_buff(p,body_part):
    #润滑充足对于获得VC快感的补正倍率
    if p['调教记忆']['{}润'.format(body_part)]>12000:
        return 2
    elif p['调教记忆']['{}润'.format(body_part)]>8000:
        return 1.5
    elif p['调教记忆']['{}润'.format(body_part)]>3000:
        return 1
    else:
        return 0.5
    