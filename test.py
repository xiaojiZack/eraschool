import cx_Freeze
import erajs.api as a
import funcs as f
from erb.系统相关.页面.game_start import game_start

a.init()
a.cls()
# 调教页面测试
# a.page()
# a.sav()['日期'] = {
#         '年':1, '季':1,
#         '旬':1, '周':1,
#         '总日数':1
#     }
# a.sav()['character_number'] = 0
# a.tmp()['调教数据']={}
# a.tmp()['调教数据']['参与者'] = []
# a.tmp()['调教数据']['参与者'].append(new_character_dict())
# a.tmp()['调教数据']['参与者'][0]['性别']='男性'
# a.sav()['character_number'] = 1
# a.tmp()['调教数据']['参与者'].append(new_character_dict())
# a.tmp()['调教数据']['参与者'][1]['性别']='女性'
# a.tmp()['调教数据']['调教者'] = 0
# a.tmp()['调教数据']['被调教'] = 1
# a.tmp()['显示记忆'] = True

# a.goto(train_page)



a.footer('@xiaoji')
game_start()