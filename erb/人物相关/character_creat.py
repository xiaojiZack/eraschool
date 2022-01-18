import erajs as a
import funcs as f
import character_class as cc

def character_creat(gender):
    #创建新角色，首先需要输入默认性别
    #可以自定义的部分：姓名，
    data = {"BasicProperty":{
        "CharacterId":a.sav()['character_list']['characternumber'],
        "gender":gender,
        }}
    new_character = cc.CharacterClass(data)
    nc = new_character()


