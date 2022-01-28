import erajs.api as a

def plan1():
    #单独授课，即进入调教页面
    a.page()
    a.mode()
    a.tmp()['调教数据']={}
    a.tmp()['调教数据']['参与者'] = []
    cl = a.sav()['character_list']
    for i in cl:
        
    a.tmp()['调教数据']['参与者'].append(new_character_dict())
    a.tmp()['调教数据']['参与者'][0]['性别']='男性'
    a.sav()['character_number'] = 1
    a.tmp()['调教数据']['参与者'].append(new_character_dict())
    a.tmp()['调教数据']['参与者'][1]['性别']='女性'
    a.tmp()['调教数据']['调教者'] = 0
    a.tmp()['调教数据']['被调教'] = 1
    a.tmp()['显示记忆'] = True