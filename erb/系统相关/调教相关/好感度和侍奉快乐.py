import erajs.api as a

def cal_favor(c,data):
    if data == []:
        return 0
    c['好感度'] += data[0]
    c['侍奉快乐'] += data[1]
    a.t('{}:'.format(c['名字']))
    a.t('好感度+({})'.format(data[0]))
    a.t(' 侍奉快乐+({})'.format(data[1]))