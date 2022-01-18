import sys
sys.path.append("C:\\Users\\Zack\\Desktop\\develop\\eraschool\\src")
import erajs.api as a
import funcs as f
import character_class as cc

def character_creat(gender):
    #创建新角色，首先需要输入默认性别
    #可以自定义的部分：姓名，
    data = {"BasicProperty":{
        "CharacterId":0,
        "gender":gender,
        }}
    creat_leading_character(cc.new_character_dict())




def creat_leading_character(empty_character):
    #创建主角
    ec = empty_character
    ec['BasicProperty']["MAXPhysicalPower"] = 2000
    ec['BasicProperty']['MAXEnergyPower'] = 2000
    ec['BasicProperty']["PhysicalPower"] = ec['BasicProperty']["MAXPhysicalPower"]
    ec['BasicProperty']['EnergyPower'] = ec['BasicProperty']['MAXEnergyPower']
    talent_point = a.sav()['achievement']['achievement_point']+10
    a.tmp()['talent_point'] = talent_point
    
    def BasicProperty():
        #口上设定部分未完成
        a.page()
        a.mode('line', 2)
        
        #BasicProperty
        def change_name(name):
            ec['BasicProperty']['name'] = name
        a.t('名字')
        a.input(change_name, ec['BasicProperty']['name'])
        a.t()

        def change_gender(gender):
            l = ['male','female']
            ec['BasicProperty']['gender'] = l[gender['index']-1]
        a.t('性别')
        s = 1
        if ec['BasicProperty']['gender'] == "male": s =1
        else: s =2
        a.dropdown(['男','女'], change_gender, s)
        a.t()

        a.t('点数:{}'.format(a.tmp()['talent_point']))
        a.t()
        a.mode('line',2)
        a.t('最大体力:')
        a.t(ec['BasicProperty']["MAXPhysicalPower"])
        def decrease():
            ec['BasicProperty']["MAXPhysicalPower"] -= 250
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['BasicProperty']["MAXPhysicalPower"] += 250
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['BasicProperty']["MAXPhysicalPower"]>1500:
            a.b('-', decrease)
        if ec['BasicProperty']["MAXPhysicalPower"]<2500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        
        a.t('最大气力:')
        a.t(ec['BasicProperty']["MAXEnergyPower"])
        def decrease():
            ec['BasicProperty']["MAXEnergyPower"] -= 100
            a.tmp()['talent_point'] +=1
            a.repeat()
        def increase():
            ec['BasicProperty']["MAXEnergyPower"] += 100
            a.tmp()['talent_point'] -=1
            a.repeat()
        if ec['BasicProperty']["MAXEnergyPower"]>1500:
            a.b('-', decrease)
        if ec['BasicProperty']["MAXEnergyPower"]<2500 and a.tmp()['talent_point']>0:
            a.b('+', increase)
        a.t()
        ec['BasicProperty']["PhysicalPower"] = ec['BasicProperty']["MAXPhysicalPower"]
        ec['BasicProperty']['EnergyPower'] = ec['BasicProperty']['MAXEnergyPower']
        

        

        
        
    


a.init()
character_creat('')
