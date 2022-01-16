import erajs.api as a
import funcs as f

'''
# class A():
#     a = 0
#     name = None
#     b = 1
#     def __init__(self,name):
#         self.a = 2
#         self.b = 3
#         self.name = name
#     def test(self):
#         print ('a normal func.')
# class B(A):
#     def test_B(self):
#         print ('func named test_B')


# class test:
#     name = ['A','B']
#     def __init__(self):
#         for i in self.name:
#             exec("self.__dict__[{}] = {}(\"{}\")".format(i,i,"jack"))
#             pass

# t = test()
# pass
'''


class CharacterClass:
    def __init__(self,data):
        self.BasicProperty = BasicProperty(
            f.dtc(data,"BasicProperty"))
        self.BodyProperty = BodyProperty(f.dtc(data,"BodyProperty"))
        self.SexExp = SexExp(f.dtc(data,"SexExp"))
        self.Memory = Memory(f.dtc(data,"Memory"))
        self.SexSkill = SexSkill(f.btc(data,"SexSkill"))
        self.Mark = Mark(f.btc(data,"Mark"))
        self.StudentStute = StudentStute(
            f.btc(data,"StudentStute"))
        self.Quaility = Quaility(f.btc(data,"Quaility"))
    def ToDict(self):
        return f.classtodict(self)

class BasicProperty:

    def __init__(self, data):
        self.CharacterId = f.dtc(data,"characterid")
        self.name = f.dtc(data,"name")
        self.race = f.dtc(data,"race")
        self.gender = f.dtc(data,"gender")
        self.koujo = f.dtc(data,"koujo")
        self.MAXPhysicalPower = f.dtc(data,"MaxPhysicalPower")
        self.PhysicalPower = self.MAXPhysicalPower
        self.MAXEnergyPower = f.dtc(data,"MaxEnergyPower")
        self.EnergyPower = self.MAXEnergyPower
        self.MAXMindPower = f.dtc(data,"MaxMindPower")
        self.MindPower = self.MAXMindPower
    
class BodyProperty:#身体实体

    def __init__(self,data):
        self.BWH = f.dtc(data,"BWH")
        self.weight = f.dtc(data,"weight")
        self.height = f.dtc(data,"height")
        self.ass = ass(f.dtc(data,"ass"))
        self.stomach = stomach(f.dtc(data,"stomach"))
        self.urethe = urethe(f.dtc(data,"urethe"))
        self.mouth = mouth(f.dtc(data,"mouth"))
        if data["gender"] != "male":
            self.womb = womb(f.dtc(data,"womb"))
            self.vagina = vagina(f.dtc(data,"vagina"))
            self.clit = clit(f.dtc(data,"clit"))
            self.breast = breast(f.dtc(data,"breast"))
        if data["gender"] != "female":
            self.penis = penis(f.dtc(data,"penis"))
            
class SexExp:#性经验

    def __init__(self,data):
        self.c = f.dtc(data,"c")
        self.v = f.dtc(data,"v")
        self.b = f.dtc(data,"b")
        self.a = f.dtc(data,"a")
        self.orgasm = f.dtc(data,"orgasm")
        self.semen = f.dtc(data,"semen")
        self.ejectmilk = f.dtc(data,"ejectmilk")
        self.ejectsemen = f.dtc(data,"ejectsemen")
        self.pee = f.dtc(data,"pee")#放尿
        self.excrete = f.dtc(data,"excrete")#排泄
        self.masturbation = f.dtc(data,"masturbation")#自慰
        self.lesbian = f.dtc(data,"lesbian")#蕾丝
        self.gay = f.dtc(data,"gay")
        self.expose = f.dtc(data,"expose")
        self.serve = f.dtc(data,"serve")#服侍
        self.love = f.dtc(data,"love")#爱情
        self.belowjob = f.dtc(data,"belowjob")#口交
        self.cuminv = f.dtc(data,"cuminv")#腔射经验
        self.cumina = f.dtc(data,"cumina")#肛射经验
        self.drinksemen = f.dtc(data,"drinksemen")
        self.kiss = f.dtc(data,"kiss")
        self.pain = f.dtc(data,"pain")
        self.bounded = f.dtc(data,"bounded")
        self.SM = f.dtc(data,"SM")
        self.drug = f.dtc(data,"drug")
        self.vinsert = f.dtc(data,"vinsert")
        self.ainsert = f.dtc(data,"ainsert")
        self.abnormal = f.dtc(data,"abnormal")
        self.givebrith = f.dtc(data,"givebrith")
        self.bephoto = f.dtc(data,"bephoto")#被摄影
        self.harlotry = f.dtc(data,"harlotry")#卖春
        self.sexdance = f.dtc(data,"sexdance")
        self.tentacle = f.dtc(data,"tentacle")
        self.animalsex = f.dtc(data,"animalsex")
        self.assistant = f.dtc(data,"assistant")#助手

class Memory:#**之珠

    def __init__(self,data):
        self.c = f.dtc(data,"c")
        self.v = f.dtc(data,"v")
        self.b = f.dtc(data,"b")
        self.a = f.dtc(data,"a")
        self.learn = f.dtc(data,"learn")#习得
        self.humbly = f.dtc(data,"humbly")#恭顺
        self.desire = f.dtc(data,"desire")#欲望
        self.surrender = f.dtc(data,"surrender")#屈服
        self.shame = f.dtc(data,"shame")#羞耻
        self.pain = f.dtc(data,"pain")#苦痛
        self.fear = f.dtc(data,"fear")#恐怖
        self.drug = f.dtc(data,"drug")#药毒
        self.assimile = f.dtc(data,"assimile")#同化
        self.initiative = f.dtc(data,"initiative")#主动
        self.unhappy = f.dtc(data,"unhappy")#否定

class SexSkill:#开发等级
    def __init__(self,data):
        self.c = f.dtc(data,"c")#c感觉
        self.v = f.dtc(data,"v")
        self.b = f.dtc(data,"b")
        self.a = f.dtc(data,"a")
        self.humbly = f.dtc(data,"humbly")#恭顺
        self.desire = f.dtc(data,"desire")#欲望
        self.skillness = f.dtc(data,"skillness")#技巧
        self.serve = f.dtc(data,"serve")#侍奉
        self.expose = f.dtc(data,"expose")
        self.S = f.dtc(data,"S")
        self.M = f.dtc(data,"M")
        self.lesbian = f.dtc(data,"lesbian")#蕾丝
        self.gay = f.dtc(data,"gay")
        self.ejectmilk = f.dtc(data,"ejectmilk")
        self.ejectsemen = f.dtc(data,"ejectsemen")
        self.semenaddiction = f.dtc(data,"semenaddiction")
        self.masturbationaddiction = f.dtc(data,"masturbationaddiction")
        self.drugaddiction = f.dtc(data,"drugaddiction")
        self.cuminsideaddiction = f.dtc(data,"cuminsideaddiction")#内射
        self.excreteaddiction = f.dtc(data,"excreteaddiction")#排泄
        self.tentacle = f.dtc(data,"tentacle")
        self.animalsex = f.dtc(data,"animalsex")
        self.pergencyaddiction = f.dtc(data,"pergencyaddiction")#怀孕中毒

class Mark:#刻印
    def __init__(self,data):
        self.pain = f.dtc(data,"pain")
        self.happy = f.dtc(data,"happy")
        self.surrender = f.dtc(data,"surrender")
        self.drug = f.dtc(data,"drug")
        self.shame = f.dtc(data,"shame")
        self.fear = f.dtc(data,"fear")
        self.unhappy = f.dtc(data,"unhappy")#反发
        self.assimile = f.dtc(data,"assimile")#同化

class Cloth:
    #todo
    def __init__(self,data):
        pass

class StudentStute:#学籍系统

    def __init__(self,data):
        self.classgroup = f.dtc(data,"classgroup")
        self.score = f.dtc(data,"score")
        self.club = f.dtc(data,"club")

class Tattoo:#淫纹
    #todo
    def __init__(self):
        pass

class Quaility:#特质
    
    def __init__(self,data):
        self.gender = f.dtc(data,"gender")
        self.personality = f.dtc(data,"personality")#性格
        self.body_trait = f.dtc(data,"body_trait")#身体特质
        self.speciality = f.dtc(data,"speciality")#特长
        self.leaning = f.dtc(data,"leaning")#性癖
        self.others = f.dtc(data,"others")

class womb:
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.contentobject = f.dtc(data,"contentobject")
        self.MenstrualCycle = f.dtc(data,"MenstrualCycle")#生理期
        self.PregnancyFlag = f.dtc(data,"PregnancyFlag")
        self.transform = f.dtc(data,"transform")
        self.Pregnancy = f.dtc(data,"Pergnancy")       
class vagina:
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.contentobject = f.dtc(data,"contentobject")
        self.transform = f.dtc(data,"transform")
        self.size = f.dtc(data,"size")
class clit:
    def __init__(self,data):
        self.transform = f.dtc(data,"transform")
class penis:#实际上包含金玉
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.producerate = f.dtc(data,"producerate")
        self.transform = f.dtc(data,"transform")
        self.length = f.dtc(data,"length")
        self.diameter = f.dtc(data,"diameter")
        self.ejectrate =f.dtc(data,"ejectrate")#标准射精量
class breast:
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.producerate = f.dtc(data,"producerate")
        self.transform = f.dtc(data,"transform")
        self.size = f.dtc(data,"size")
        self.ejectrate =f.dtc(data,"ejectrate")#标准射乳量   
class ass:
    def __init__(self,data):
        self.transform = f.dtc(data,"transform")
        self.contentobject = f.dtc(data,"contentobject")
        self.size = f.dtc(data,"size")
        self.buttsize = f.dtc(data,"buttsize")
class stomach:
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.transform = f.dtc(data,"transform")       
class mouth:
    def __init__(self,data):
        self.transform = f.dtc(data,"transform")
class urethe:
    def __init__(self,data):
        self.volume = f.dtc(data,"volume")
        self.contentliquid = f.dtc(data,"contentliquid")
        self.contentobject = f.dtc(data,"contentobject")
        self.transform = f.dtc(data,"transform")
        self.size = f.dtc(data,"size")
