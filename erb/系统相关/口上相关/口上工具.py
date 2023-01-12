import time
import erajs.api as a

def show_kojo():
    #按照待显示口上列表逐条打印口上，口上列表每行包含一个字典{‘打印文本’：‘style格式’}
    kojolist = a.tmp()['待显示口上']
    for lines in kojolist:
        text = lines[0]
        if (text == ''):
            a.t()
        else:
            style = lines[1]
            a.t(text, style=style)
        time.sleep(0.01)
    a.t('',True)
    a.tmp()['待显示口上'] = []

def push_text(text, style = {}):
    #装载口上
    kojolist = a.tmp()['待显示口上']
    kojolist.append([text,style])

def pc(person,quaility):
    #快速查询人物特质，存在返回True，不存在返回false
    for i in person['属性']:
        for j in person['属性'][i]:
            if j == quaility:
                return True
    return False

def comadd(information):
    if information['com'] == 'add':
        return True
    else:
        return False

def comdoing(information):
    if information['com'] == 'doing':
        return True
    else:
        return False

def comundo(information):
    if information['com'] == 'undo':
        return True
    else:
        return False

def comfail(information):
    if information['com'] == 'fail':
        return True
    else:
        return False

def pt():
    kojolist = a.tmp()['待显示口上']
    kojolist.append(['',{}])

def check_orgasm(person, place='any'):
    #place = V/A/C/M/B/U/W
    ol = a.tmp()['高潮口上记录']['绝顶']
    result = {}
    for i in ol:
        if i == person['CharacterId']:
            result = ol[i]
    if (result == {}):
        return False
    if (place == 'any' and result != {}):
        return True
    elif (place != 'any'):
        for i in result:
            if i == place:
                return result[place]
        return False

def check_eject(person):
    ol = a.tmp()['高潮口上记录']['射精']
    result = []
    for i in ol:
        if i['whoeject'] == person['CharacterId']:
            result = i
        if (result == []):
            return False
        else:
            return {'谁被射':find_people(i['whoinject'])['名字'],'位置':i['place'],'液体':i['liquid']}

def check_be_eject(person):
    ol = a.tmp()['高潮口上记录']['射精']
    result = []
    for i in ol:
        if i['whoinject'] == person['CharacterId']:
            result = i
    if (result == []):
        return False
    else:
        return {'谁射':find_people(i['whoeject'])['名字'],'位置':i['place'],'液体':i['liquid']}

def get_mark(inf, mark):
    if '获得刻印' in inf:
        if (inf['获得刻印'][0] == mark):
            return inf['获得刻印'][1]
    else:
        return False

def find_people(CharacterId):
    for i in a.tmp()['调教数据']['参与者']:
        if i['CharacterId'] == int(CharacterId):
            return i
    return False

def find_people_name(name):
    for i in a.tmp()['调教数据']['参与者']:
        if i['名字'] == name:
            return i
    return False

def check_special(inf,type):
    if '特殊事件' in inf.keys():
        if type in inf['特殊事件']:
            return True
    return False