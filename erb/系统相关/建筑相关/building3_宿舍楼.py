import erajs.api as a

def exec3(building):
    #宿舍事件
    pass
    return True

def destory3(building):
    if len(a.sav()['character_list']['学生']) > a.sav()['学生上限人数'] -3:
        return False
    else:
        a.sav()['学生上限人数'] -= 3
        return True

def structure3(building={}):
    #最大收容数+3
    a.sav()['学生上限人数'] += 3
    return True