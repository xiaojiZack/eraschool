import erajs.api as a

def class3_student_performance(c,rate,material):
    cname = c['名字']
    leading_character = a.sav()['character_list']['主角']
    lc_name = leading_character['名字']
    color_dist = {
        'C':{'color':'#FF0000'},
        'B':{'color':'#FFFF00'},
        'A':{'color':'#008000'},
        'S':{'color':'#7FFF00'},
        'SS':{'color':'#FFC1C1'},
        'SSS':{'color':'#FFC1C1'},
    }
    if material == '普通AV':
        if rate == 'C':
            a.t('{}不知道跑到哪去了'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}红着脸，眼睛似乎在看着别的地方。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}半遮半掩地偷窥着影片。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}的脸通红，但是还是直视着大屏幕。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}正在仔细观赏女优的动作。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}津津有味地看完了全片，播放完后问了详细的番号。'.format(cname),style=color_dist[rate])
    if material == '热门AV':
        if rate == 'C':
            a.t('{}不知道跑到哪去了'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}红着脸，眼睛似乎在看着别的地方。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}半遮半掩地偷窥着影片。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}的脸通红，但是还是直视着大屏幕。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}正在仔细观赏女优的动作。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}津津有味地看完了全片，播放完后问了详细的番号。'.format(cname),style=color_dist[rate])

    a.t('',wait=True)

def class3_describe(material):
    leading_character = a.sav()['character_list']['主角']
    lc_name = leading_character['名字']

    if material == '普通AV':
        a.divider()
        a.mode()
        a.t('{}将一部学习资料投影到大屏幕上，一时间女优的淫叫充斥了整个房间。'.format(lc_name), wait=True)
    if material == '热门AV':
        a.divider()
        a.mode()
        a.t('{}将一部学习资料投影到大屏幕上，一时间女优的淫叫充斥了整个房间。'.format(lc_name), wait=True)

    
def class3_main_describe(c,rate,material):
    class3_describe(material)
    a.t()
    class3_student_performance(c,rate,material)