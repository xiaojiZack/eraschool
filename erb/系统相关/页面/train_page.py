import erajs.api as a
import funcs as f
from ...人物相关.pregnancy import check_menstrual_period
from ...调教相关.memory import memory_progress
def train_page():
    memory_list = [
            '快C', '快V', '快B', '快A', '快M', '快P', '快W',
            'V润','A润','习得', '恭顺', '欲情', '屈服', 
            '羞耻', '苦痛', '恐惧', '药毒', '同化', '主导', '反感']

    a.page()
    a.mode('grid',2)
    #time
    season = ['春','夏','秋','冬']
    week = ['上','下']
    date = a.sav()['日期']
    a.t('{}年{}季{}第{}周'.format(
        date['年'],season[date['季']-1],
        week[date['旬']-1],date['周']))
    a.t()
    #地点 todo
    #氛围
    data = a.tmp()['调教数据']
    a.divider()
    a.mode('grid',3)
    for c in data['参与者']:
        a.t(c['基本信息']['名字'])
        if c['基本信息']['性别'] == '男性':
            a.t('♂')
            a.t('[{}]'.format(c['身体信息']['阴茎']['尺寸']))
            a.t()
        elif c['基本信息']['性别'] == '女性':
            a.t('♀')
            t = check_menstrual_period(c['身体信息']['子宫']['危险日'])
            style = {}
            if (t =='危险日'):
                t = t+'♥'
                style = {'color':'#FFC1C1'}
            elif(t == '安全日'):
                style = {'color':'#7FFF00'}
            a.t('[{}]'.format(t), style = style)
            a.t()
        else:
            a.t('♀♂')
            a.t('[{}]'.format(c['身体信息']['阴茎']['尺寸']))
            t = check_menstrual_period(c['身体信息']['子宫']['危险日'])
            style = {}
            if (t =='危险日'):
                t = t+' ♥'
                style = {'color':'#FFC1C1'}
            elif(t == '安全日'):
                style = {'color':'#7FFF00'}
            a.t('[{}]'.format(t), style = style)
            a.t()
        a.t()
        a.t()
        a.t('体力:')
        f.colorful_progress(c['基本信息']['体力值'],c['基本信息']['最大体力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['基本信息']['体力值'],c['基本信息']['最大体力值']))
        a.t()
        a.t('气力:')
        f.colorful_progress(c['基本信息']['气力值'],c['基本信息']['最大气力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['基本信息']['气力值'],c['基本信息']['最大气力值']))
        a.t()
        a.t('理智:')
        f.colorful_progress(c['基本信息']['理智值'],c['基本信息']['最大理智值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['基本信息']['理智值'],c['基本信息']['最大理智值']))
        a.divider()
        a.mode('grid',4)
        if (c['基本信息']['CharacterId']==0):
            for i in memory_list:
                memory_progress(c['调教记忆'][i], i)
                a.t()
        if (c['基本信息']['性别'] != '女性'):
            a.t('精巢存量:')
            a.progress(c['身体信息']['阴茎']['内容总量'],c['身体信息']['阴茎']['容量'])
            a.t('({}/{})'.format(c['身体信息']['阴茎']['内容总量'], c['身体信息']['阴茎']['容量']))
            a.t()
        if (c['基本信息']['性别'] != '男性'):
            a.t('母乳存量:')
            a.progress(c['身体信息']['乳房']['内容总量'],c['身体信息']['乳房']['容量'])
            a.t('({}/{})'.format(c['身体信息']['乳房']['内容总量'],c['身体信息']['乳房']['容量']))
            a.t()
            a.t('胎内精液量:')
            if (c['身体信息']['子宫']['内容总量']<c['身体信息']['子宫']['容量']):
                a.progress(c['身体信息']['子宫']['内容总量'],c['身体信息']['子宫']['容量'])
            elif (c['身体信息']['子宫']['内容总量']<c['身体信息']['子宫']['容量']*2):
                a.t('[满满的♥]',style={'color':'#FFC1C1'})
            else:
                a.t('[♥子宫膨胀♥]',style={'color':'#FFC1C1'})
            a.t('({}/{})'.format(c['身体信息']['子宫']['内容总量'],c['身体信息']['子宫']['容量']))
            a.t()
        if (c['基本信息']['CharacterId']!=0):
            a.t('排泄欲:')
            if (c['身体信息']['肠胃']['内容总量']<c['身体信息']['肠胃']['容量']):
                a.progress(c['身体信息']['肠胃']['内容总量'],c['身体信息']['肠胃']['容量'])
            elif (c['身体信息']['肠胃']['内容总量']<c['身体信息']['肠胃']['容量']*2):
                a.t('[满满的♥]',style={'color':'#FFC1C1'})
            else:
                a.t('[♥西瓜肚♥]',style={'color':'#FFC1C1'})
            a.t('({}/{})'.format(c['身体信息']['肠胃']['内容总量'],c['身体信息']['肠胃']['容量']))
            a.t()
        a.t('尿意')
        a.progress(c['其他参数']['尿意'], 10000)
        a.t()
        if (c['基本信息']['CharacterId']!=0):
            a.t('性欲')
            if (c['其他参数']['性欲']>c['其他参数']['本次绝顶次数']):
                a.progress(c['其他参数']['本次绝顶次数'],c['其他参数']['性欲'],style=[
                    {'color':'#FFC1C1'},{'background-color':'#FFC1C1'},{'width':'50px'}])
            elif (2*c['其他参数']['性欲']>c['其他参数']['本次绝顶次数']):
                a.t('[满足♥]',style={'color':'#EEEE00'})
            else:
                a.t('[♥大满足♥]',style={'color':'#FFC1C1'})
            a.t('({}/{})'.format(c['其他参数']['本次绝顶次数'],c['其他参数']['性欲']))
            a.t()
            a.t('精液欲')
            if (c['其他参数']['精液欲']>c['其他参数']['本次精液次数']):
                a.progress(c['其他参数']['本次精液次数'],c['其他参数']['精液欲'],style=[
                    {'color':'#FFC1C1'},{'background-color':'#FFC1C1'},{'width':'50px'}])
            elif (2*c['其他参数']['精液欲']>c['其他参数']['本次精液次数']):
                a.t('[满足♥]',style={'color':'#EEEE00'})
            else:
                a.t('[♥大满足♥]',style={'color':'#FFC1C1'})
            a.t('({}/{})'.format(c['其他参数']['本次精液次数'],c['其他参数']['精液欲']))
        a.divider()
    #指令部分
    a.mode('grid',5)
    

