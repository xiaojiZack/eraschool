#管理系统时间
import erajs.api as a
import funcs as f

def date_count():
    #负责日期变化进位
    time = a.sav()['time']
    time['day'] = time['day']+1
    if (time['day'] > 7):
        time['day'] = 1
        time['week'] = time['week']+1
    if (time['week'] > 2):
        time['week'] = 1
        time['season'] = time['season']+1
    if (time['season'] > 4):
        time['season'] = 1
        time['year'] = time['year'] + 1
    time['total_day'] = time['total_day'] + 1


