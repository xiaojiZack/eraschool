import erajs.api as a
import funcs as f

def check_menstrual_period(ovulation_date):
    time_day = a.sav()['日期']['周']
    if (abs(ovulation_date-time_day) <= 1 ):
        return "危险日"
    else:
        return "安全日"

#怀孕判断 todo
