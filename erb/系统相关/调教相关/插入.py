import erajs.api as a
from erb.系统相关.调教相关.处女 import check_pure, pure_punish
from erb.系统相关.调教相关.插入尺寸计算 import check_maintain_size, check_size, size_punish
from erb.系统相关.调教相关.润滑 import is_enough_oiling, not_oil_warning, not_oiling_punish
insertdist = {'P':"阴茎",'F':'手指'}
beinsertdist = {'V':'阴道','A':'肛门','U':'尿道','M':'口'}
oilneed = {'P':3,'F':1}
def insert_check(ac,pa,insertproject,place,com_trait):
    #insertproject = P/F, place = V/A/U
    if check_insert_obejct(ac,insertproject) == False:
        a.t('err-插入物不存在')
        return False
    else:
        expand_size = pa['开发']['{}扩张度'.format(place)]
        size = ''
        if insertproject == 'P':
            size = ac['身体信息'][insertdist[insertproject]]['尺寸']
        elif insertproject in insertdist.keys(): 
            size = insertdist[insertproject]
        else:
            size = insertproject
        have_inserted = pa['身体信息'][beinsertdist[place]]['内容固体']
        size_flag = check_size(expand_size,size,have_inserted)
        if ac['名字'] in have_inserted:
            if have_inserted[ac['名字']] == size:
                size_flag = check_maintain_size(expand_size,have_inserted)
        if size_flag  == False:
            com_trait.append('尺寸过大')
            com_trait.append('疼痛')
        if(a.tmp()['调教数据']['尺寸警告标志']==False or size_flag):
            #执行后续操作
            oil_require = is_enough_oiling(pa,place,oilneed[insertproject])
            if oil_require >0:
                com_trait.append('润滑不足')
            if (not_oil_warning(pa,oil_require)):
                pure_flag = check_pure(pa,place)
                if(pure_flag or a.tmp()['调教数据']['破处警告标志']==False):
                    #返回判断结果
                    return {'size_flag':size_flag,'oil_require':oil_require,'pure_flag':pure_flag}
    return False

def insert(ac,pa,insertproject,place,check_result):
    if check_result:
        if insertproject == 'P':
            size = ac['身体信息'][insertdist[insertproject]]['尺寸']
        elif insertproject in insertdist.keys(): 
            size = insertdist[insertproject]
        else:
            size = insertproject
        pa['身体信息'][beinsertdist[place]]['内容固体'][ac['名字']] = size
        if insertproject == 'P':
            ac['身体信息']['阴茎']['插入位置'][pa['CharacterId']] = beinsertdist[place]
        if check_result['size_flag']:
            size_punish(pa,place)
        if check_result['oil_require']>0:
            not_oiling_punish(pa,check_result['oil_require'])
        if check_result['pure_flag']:
            pure_punish(pa,place)
        return True
    return False

def check_insert_obejct(c,insertproject):
    #检查插入物是否存在
    if insertproject == 'P':
        if c['性别'] == '女性':
            return False
        else: return True
    elif insertproject == 'F':
        return True
    return True