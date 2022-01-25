#管理系统时间
import erajs.api as a
import funcs as f

def date_count():
    #负责日期变化进位
    #一年=4季=4*2上下季=4*2*7周
    time = a.sav()['日期']
    time['周'] = time['周']+1
    if (time['周'] > 7):
        time['周'] = 1
        time['旬'] = time['旬']+1
    if (time['旬'] > 2):
        time['旬'] = 1
        time['季'] = time['季']+1
    if (time['季'] > 4):
        time['季'] = 1
        time['年'] = time['年'] + 1
    time['总日数'] = time['总日数'] + 1


