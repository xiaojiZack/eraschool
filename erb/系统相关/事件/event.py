import erajs.api as a
from .event_1_入学 import event1
from .event_2_毕业 import event2
from .event_3_参观日 import event3_1,event3_2,event3_3

event_time_table={
    '1':{'季':1,'旬':1,'周':1},
    '2':{'季':4,'旬':2,'周':7},
    '3_1':{'季':2,'旬':1,'周':2},
    '3_2':{'季':3,'旬':1,'周':1},
    '3_3':{'季':4,'旬':1,'周':1},
}

event_table = {
    '1':'入学',
    '2':'毕业',
    '3_1':'参观日',
    '3_2':'参观日',
    '3_3':'参观日',
}

def event_check():
    date = a.sav()['日期']
    for i in event_time_table:
        flag = True
        for j in ['季','旬','周']:
            if date[j]!=event_time_table[i][j]:
                flag = False
        if flag:
            exec('event{}()'.format(i))

def next_event():
    def change(date):
        day = date['季']*2*7
        day += date['旬']*7
        day += date['周']
        return day
    date = a.sav()['日期']
    mini = 4*2*7
    next_event = 1
    date_day =change(date)
    for i in event_time_table:
        if change(event_time_table[i]) < date_day:
            if mini > change(event_time_table[i]) - date_day+4*2*7:
                mini = change(event_time_table[i])-date_day+4*2*7
                next_event = i
        elif change(event_time_table[i])-date_day == 0:
            pass
        elif mini > change(event_time_table[i])-date_day:
            mini = change(event_time_table[i])-date_day
            next_event = i
    return [event_table[str(next_event)],mini]
