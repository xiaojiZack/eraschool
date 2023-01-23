import erajs.api as a

def class4_student_performance(c,rate,material,method):
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
    if method == '理论':
        if rate == 'C':
            a.t('{}在课上睡着了。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}似乎在认真听讲，但仔细看就会发现其实在走神。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}脸红着似懂非懂地听完了课。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正在认真听课。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}在课本上努力记着笔记。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}在课后依然缠着你问问题。'.format(cname),style=color_dist[rate])
    if method == '假阳具训练':
        if rate == 'C':
            a.t('{}缩着手，碰都不碰假阳具。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}用两根手指夹起假阳具后僵在了原地。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}害羞地按照指示操作着。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正在服侍假阳具。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('即使是假阳具，{}也在认真地服侍假阳具。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}一脸陶醉在服侍阳具的喜悦中。'.format(cname),style=color_dist[rate])
    if method == '实际操作':
        if rate == 'C':
            a.t('{}缩着手，拒绝配合。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}用两根手指夹起阳具后僵在了原地。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}害羞地按照指示操作着。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正在服侍阳具。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}也在认真地服侍假阳具，脸上有些喜悦的气息。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}一脸陶醉在服侍阳具的喜悦中。'.format(cname),style=color_dist[rate])
    
    a.t('',wait=True)

def class4_describe(material,method):
    leading_character = a.sav()['character_list']['主角']
    lc_name = leading_character['名字']
    a.divider()
    a.mode()
    if method == '理论':
            a.t('{}在黑板上写下重点。'.format(lc_name))
    elif method == '假阳具练习':
        a.t('{}在将一个假阳具立在讲台上后又给每个人发放一个假阳具。'.format(lc_name))
    elif method == '实际练习':
        a.t('{}解开了裤子。'.format(lc_name))

    if material == '手交':
        if method == '理论':
            a.t('‘要注意刺激龟头、马眼、系带这些地方，常用的手法有...’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行手交'.format(lc_name),wait=True)
    if material == '口交':
        if method == '理论':
            a.t('‘像吃冰淇淋一样从下到上舔舐，用舌头在龟头上打转或者含着睾丸也是不错的方法...’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行口交'.format(lc_name),wait=True)
    if material == '足交':
        if method == '理论':
            a.t('‘一定要轻柔地摩擦...’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行足交'.format(lc_name),wait=True)
    if material == '乳交':
        if method == '理论':
            a.t('‘用双手从侧面给予乳压，上下翻动...’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行乳交'.format(lc_name),wait=True)
    if material == '素股':
        if method == '理论':
            a.t('‘用阴唇包裹肉棒以后用上体重摩擦，’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行素股'.format(lc_name),wait=True)
    if material == '骑乘':
        if method == '理论':
            a.t('‘用心感受肚子里的阳具，然后尽情扭腰或者上下摆动都是可以的...’。', wait=True)
        if method == '假阳具练习' or method == '实际练习':
            a.t('{}指导着肉便生们用所学知识进行骑乘训练'.format(lc_name),wait=True)
    
def class4_main_describe(c,rate,material):
    material_name = get_material_and_method(material)
    class4_describe(material_name[0],material_name[1])
    a.t()
    class4_student_performance(c,rate,material_name[0],material_name[1])

def get_material_and_method(material):
    material=material.split('-')
    return [material[0],material[1]]