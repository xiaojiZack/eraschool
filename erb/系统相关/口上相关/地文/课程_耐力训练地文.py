import erajs.api as a

def class5_student_performance(c,rate,material):
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
    if material == '健身操':
        if rate == 'C':
            a.t('{}敷衍地动了动手臂。看来需要好好矫正一下这个小鬼的态度。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('即使你耐心地示范，{}也有点跟不上动作。也不知道是不是故意跟不上的。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('看的出来，{}还是有稍微用了心在训练。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}正在努力尝试模仿你的动作。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}在努力做完几套健身操后满头大汗。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}完美地模仿了你的动作。似乎没有什么需要指出的地方。'.format(cname),style=color_dist[rate])
    if material == '跑步':
        if rate == 'C':
            a.t('{}在课程中间从你的视野里消失了。'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}似乎完全没有在认真跑。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}有气无力地跑完了全程。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}只求无过地按照要求完成了所有训练项目。'.format(cname),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}跑完以后满头大汗地坐在地上，似乎是累坏了。'.format(cname),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}正在努力突破自己的记录，似乎能从身上看到‘必胜！’的气场。'.format(cname),style=color_dist[rate])
    if material == '游泳':
        if rate == 'C':
            a.t('{}在课程中间从你的视野里消失了。——给我好好重视体育课啊混蛋'.format(cname),style=color_dist[rate])
        if rate == 'B':
            a.t('{}从头到尾都在玩水。'.format(cname),style=color_dist[rate])
        if rate == 'A':
            a.t('{}有气无力地游完了全程。'.format(cname),style=color_dist[rate])
        if rate == 'S':
            a.t('{}按照要求完成了所有训练项目。{}顺便也摸了个爽。'.format(cname,lc_name),style=color_dist[rate])
        if rate == 'SS':
            a.t('{}积极地让{}手把手地为其矫正游泳动作。'.format(cname,lc_name),style=color_dist[rate])
        if rate == 'SSS':
            a.t('{}正在努力突破自己的记录，似乎能看到‘必胜！’的气场。'.format(cname),style=color_dist[rate])
    a.t('',wait=True)

def class5_describe(material):
    leading_character = a.sav()['character_list']['主角']
    lc_name = leading_character['名字']

    if material == '健身操':
        a.divider()
        a.mode()
        a.t('不管怎么说，做爱也好，调教也好，都必须要有足够的体力。要是在日后被残忍地SM调教或者连续中出耐久的途中因为体力不支昏过去就不好了。')
        a.t()
        a.t('所以在开始正式教育这些肉便生之前，锻炼体力也是一项很重要的工作。')
        a.t()
        a.t('听说，健身操在舒缓筋骨、增强体力方面有一些作用。即使是天生体质虚弱的人也可以从中受益。')
        a.t('{}开始尝试回忆以前学过的健身操动作,一招一式地耐心指导着。'.format(lc_name), wait=True)
    if material == '跑步':
        a.divider()
        a.mode()
        a.t('在{}的指导下，一次锻炼意志力和体力的田径课程开始了。'.format(lc_name))
        a.t()
        a.t('1000米长跑、100米往返跑、助跑跳远等等。除了常规的计时要求以外，跑的太慢的人还有额外的惩罚。')
        a.t()
        a.t('肉便生们在结束之后累到瘫倒在地上，内心哭诉着不想再来这样的阿鼻地狱也算很常见的。', wait=True)
    if material == '游泳':
        a.divider()
        a.mode()
        a.t('{}正在指导肉便生们进行游泳训练。由于是室内泳池，池水的清洁、水温、以及设施的保养都十分完美。'.format(lc_name))
        a.t()
        a.t('当然穿着泳衣进行指导就少不了大饱眼福和动手动脚的机会。')
        a.t('事实上，所有人都被乘机揉过重要部位。‘这是教育的一部分！’当然无论哪种角度来说的确如此。',wait=True)
    
def class5_main_describe(c,rate,material):
    class5_describe(material)
    a.t()
    class5_student_performance(c,rate,material)