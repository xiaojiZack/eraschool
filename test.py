import erajs.api as a
import funcs as f
from erb.系统相关.页面.train_page import train_page
from erb.人物相关.character_creat import new_character_dict


a.init()
a.page()
a.sav()['日期'] = {
        '年':1, '季':1,
        '旬':1, '周':1,
        '总日数':1
    }
a.tmp()['调教数据']={}
a.tmp()['调教数据']['参与者'] = []
a.tmp()['调教数据']['参与者'].append(new_character_dict())
a.tmp()['调教数据']['参与者'][0]['基本信息']['性别']='女性'

train_page()