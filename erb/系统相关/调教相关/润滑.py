import erajs.api as a

#通过输入的c来判断是否润滑不足，若润滑不足则返回不足程度
def is_enough_oiling(c,body_type,demand):
    if c['调教记忆']['{}润'.format(body_type)] <100:
        return demand-1
    elif c['调教记忆']['{}润'.format(body_type)]<1000:
        return demand-2
    elif c['调教记忆']['{}润'.format(body_type)]<10000:
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