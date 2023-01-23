import erajs.api as a
from random import choice

def class2_student_performance(c,rate,material):
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
    if material == '性知识讲解':
        if rate == 'C':
            a.t('{}在课上睡着了。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}似乎在认真听讲，但仔细看就会发现其实在走神。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}似懂非懂地听完了课。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正在认真听课。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}在课本上努力记着笔记。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}在课后依然缠着你问问题。'.format(cname),style=color_dist[rate])
    if material == '常识变更':
        if rate == 'C':
            a.t('{}催一下动一下，完全没有干劲。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}含糊不清地快速念完了句子，然后又潦草地写了几个字。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}涨红了脸，总算是完成了任务。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}按照要求规规矩矩地完成了任务。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}正在大声朗读句子。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}在课后似乎打算把抄写的成果带回去贴墙上。'.format(cname),style=color_dist[rate])
    if material == '催眠':
        if rate == 'C':
            a.t('{}闭气凝神，捂着耳朵，紧闭双眼'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}躲闪着眼神，避免与催眠道具直视。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}似乎完全不在乎地坐着。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正目不转睛地盯着那些奇怪的图案。'.format(cname,lc_name),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}一脸迷糊地坐在位置上。'.format(cname,lc_name),style=color_dist[rate])
        if rate == 'SSS':
            a.t('‘肉便器？啊，我就是，怎么了吗？要不现在就来中出我吧。’{}在结束后这样回答道。'.format(cname),style=color_dist[rate])
    a.t('',wait=True)

def class2_describe(material):
    leading_character = a.sav()['character_list']['主角']
    lc_name = leading_character['名字']

    if material == '性知识讲解':
        a.divider()
        a.mode()
        a.t('{}正对着一幅子宫剖面图讲解着。')
        a.t('‘男性将精液注射到子宫后就可能会受精，子宫里精液越多受精的可能性越高。所以男性要射精的时候一定要夹紧阴道肌肉，努力用子宫口吸住男性的尿道口，这样才能用子宫尽可能多的榨取精液。’')
        a.t()
        a.t('‘为什么要这样做？')
        a.t('女性被中出受孕不是天经地义的事情吗？',style={'color':'#FFC1C1'},wait=True)
    if material == '常识变更':
        sentences = [
            '女性的天职就是作为性奴，服侍肉棒，成为肉棒的玩物。',
            '女性应该服从调教，以成为肉便器为荣。',
            '露出身体就像吃饭喝水一样稀松平常，所以要克服自己的羞耻心。',
            '被播种受孕不是什么可怕的事情，给予生命新生本身就是无上荣光。',
            '精液是重要的资源，需要尽可能地装在身体里或者挂在身上，以免不必要的浪费。',
            '肚子里被中出应当心怀感激。',
            '被强奸是一件无上幸福的事情，要一边装作被强迫的样子一边主动张开大腿接受侵犯。',
        ]
        choice_sentence = choice(sentences)
        a.divider()
        a.mode()
        a.t('[{}]'.format(choice_sentence))
        a.t('类似的标语写成了一个小本子，{}监督每个上课的肉便生在大声诵读10遍后抄写3次。'.format(lc_name),wait=True)
        a.t()

    if material == '催眠':
        a.divider()
        a.mode()
        a.t('{}特地把场地弄得昏暗后，点上了特殊的熏香，播放起有着奇怪节拍的音乐。'.format(lc_name))
        a.t('与此同时四周的墙壁上开始投影着奇怪的动态花纹。',wait=True)
    
def class2_main_describe(c,rate,material):
    class2_describe(material)
    a.t()
    class2_student_performance(c,rate,material)