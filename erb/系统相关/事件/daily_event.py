import erajs.api as a
from random import choice
from erb.系统相关.事件.日常事件.日常事件1_打招呼 import try_event1
from erb.系统相关.事件.日常事件.日常事件2_一起观影 import try_event2
from erb.系统相关.事件.日常事件.日常事件3_早安咬 import try_event3
from erb.系统相关.事件.日常事件.日常事件4_早安骑 import try_event4


#日常事件触发函数，对可执行的日常事件进行选择
def daily_event():
    daily_events_list = [try_event1,try_event2,try_event3,try_event4]
    flag = False
    while not flag and len(daily_events_list):
        choice_event = choice(daily_events_list)
        if choice_event():
            flag = True
        else:
            daily_events_list.remove(choice_event)
    if len(daily_events_list) == 0:
        a.t('今日无事发生')
