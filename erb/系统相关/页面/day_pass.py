import erajs.api as a
from ..建筑相关.building import exec_building
from ..事件.daily_event import daily_event
from ..system_time import date_count
from ..事件.event import event_check

def day_pass():
    a.divider('建筑事件')
    exec_building()
    a.t('',True)
    a.divider('日常事件')
    a.t('',True)
    daily_event()
    a.divider('大型事件')
    a.t('',True)
    date_count()
    event_check()
    a.t('',True)
    a.back(2)



