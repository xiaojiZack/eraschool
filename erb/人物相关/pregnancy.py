import erajs.api as a
import funcs as f

def check_menstrual_period(character_id):
    character = a.sav()['character_list'][character_id]
    if (character.BasicProperty.gender != "male"):
        ovulation_date = character.BodyProperty.womb.ovulation_date
        time_day = a.sav()['time']['dat']
        if (abs(ovulation_date-time_day) <= 1 ):
            return "危险期"
        else:
            return "安全期"

#怀孕判断 todo
