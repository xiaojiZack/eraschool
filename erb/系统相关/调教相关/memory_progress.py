import erajs.api as a
import funcs as f
def memory_progress(data, name):
    level_count = [100, 500, 1000, 10000, 50000, 
    200000, 500000, 1000000, 5000000,10000000]
    level =0
    temp = data
    while (level <10):
        if (temp - level_count[level] >0):
            level = level +1
        else:
            break
    if (level < 3):
        style = {'color':'#fff'}
    elif (level <6):
        style = {'color':'#FFC1C1'}
    elif (level <9):
        style = {'color':'#FF00FF'}
    else:
        style = {'color':'#f00'}
    a.t('{}Lv{}'.format(name,level), style = style)
    a.progress(data, level_count[level], style = [{'width': '20px'},style,{'background-color': style['color']}, ])
    text = '0'
    if (data>10000):
        text = str(data/1000)+'k'
    else:
        text = str(data)
    a.t('{}'.format(text), style = style)