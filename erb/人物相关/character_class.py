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

def new_character_dict():
    new_character = {'BasicProperty': {
        'CharacterId': 0, 'name': '', 'age': '青年', 'race': '', 'gender': 'futa', 
        'koujo': '', 'MAXPhysicalPower': 0, 'PhysicalPower': 0, 'MAXEnergyPower': 0, 
        'EnergyPower': 0, 'MAXMindPower': 0, 'MindPower': 0}, 
                     'BodyProperty': {
                         'BWH': [], 'weight': 0, 'height': 0, 
                         'real_length':0, 'real_weight':0,
                         'ass': {'transform': [], 'contentobject': {}, 'size': '', 'buttsize': ''}, 
                         'stomach': {'volume': 0, 'contentliquid': {}, 'transform': []}, 
                         'urethe': {'volume': 0, 'contentliquid': {}, 'contentobject': {}, 'transform': [], 'size': ''}, 
                         'mouth': {'transform': []}, 
                         'womb': {'volume': 0, 'contentliquid': {}, 'contentobject': {}, 'ovulation_date': 0, 'PregnancyFlag': False, 'transform': [], 'Pregnancy': {}}, 
                         'vagina': {'volume': 0, 'contentliquid': {}, 'contentobject': {}, 'transform': [], 'size': ''}, 
                         'clit': {'transform': []}, 
                         'breast': {'volume': 0, 'contentliquid': {}, 'producerate': 0, 'transform': [], 'size': '', 'ejectrate': 0}, 
                         'penis': {'volume': 0, 'contentliquid': {}, 'producerate': 0, 'transform': [], 'length': 0, 'diameter': 0, 'ejectrate': 0}}, 
                     'SexExp': {'c': 0, 'v': 0, 'b': 0, 'a': 0, 'orgasm': 0, 'semen': 0, 
                                'V_expand':0,'A_expand':0,
                                'ejectmilk': 0, 'ejectsemen': 0, 'pee': 0, 'excrete': 0, 'masturbation': 0, 
                                'lesbian': 0, 'gay': 0, 'expose': 0, 'serve': 0, 'love': 0, 'belowjob': 0, 
                                'cuminv': 0, 'cumina': 0, 'drinksemen': 0, 'kiss': 0, 'pain': 0, 'bounded': 0, 
                                'SM': 0, 'drug': 0, 'vinsert': 0, 'ainsert': 0, 'abnormal': 0, 'givebrith': 0, 
                                'bephoto': 0, 'harlotry': 0, 'sexdance': 0, 'tentacle': 0, 'animalsex': 0, 'assistant': 0}, 
                     'Memory': {'c': 0, 'v': 0, 'b': 0, 'a': 0, 'learn': 0, 'humbly': 0, 'desire': 0, 'surrender': 0, 
                                'shame': 0, 'pain': 0, 'fear': 0, 'drug': 0, 'assimile': 0, 'initiative': 0, 'unhappy': 0}, 
                     'SexSkill': {'c': 0, 'v': 0, 'b': 0, 'a': 0, 'humbly': 0, 'desire': 0, 'skillness': 0, 'serve': 0, 
                                  'expose': 0, 'S': 0, 'M': 0, 'lesbian': 0, 'gay': 0, 'ejectmilk': 0, 'ejectsemen': 0, 
                                  'semenaddiction': 0, 'masturbationaddiction': 0, 'drugaddiction': 0, 'cuminsideaddiction': 0, 
                                  'excreteaddiction': 0, 'tentacle': 0, 'animalsex': 0, 'pergencyaddiction': 0}, 
                     'Mark': {'pain': 0, 'happy': 0, 'surrender': 0, 'drug': 0, 'shame': 0, 'fear': 0, 'unhappy': 0, 
                              'assimile': 0}, 
                     'StudentStute': {'classgroup': '', 'score': {}, 'club': ''}, 
                     'Quaility': {'personality': [], 'body_trait': [], 'speciality': [], 'leaning': [], 'others': []}
                     }
    return new_character

class CharacterClass:
    def __init__(self,data):
        self.BasicProperty = BasicProperty(
            f.dtc(data,"BasicProperty"))
        self.BodyProperty = BodyProperty(f.dtc(data,"BodyProperty"),
            self.BasicProperty.gender)
        self.SexExp = SexExp(f.dtc(data,"SexExp"))
        self.Memory = Memory(f.dtc(data,"Memory"))
        self.SexSkill = SexSkill(f.dtc(data,"SexSkill"))
        self.Mark = Mark(f.dtc(data,"Mark"))
        self.StudentStute = StudentStute(
            f.dtc(data,"StudentStute"))
        self.Quaility = Quaility(f.dtc(data,"Quaility"))
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

    def __init__(self,data,gender):
        self.BWH = f.dtc(data,"BWH")
        self.weight = f.dtc(data,"weight")
        self.height = f.dtc(data,"height")
        self.ass = ass(f.dtc(data,"ass"))
        self.stomach = stomach(f.dtc(data,"stomach"))
        self.urethe = urethe(f.dtc(data,"urethe"))
        self.mouth = mouth(f.dtc(data,"mouth"))
        if gender != "male":
            self.womb = womb(f.dtc(data,"womb"))
            self.vagina = vagina(f.dtc(data,"vagina"))
            self.clit = clit(f.dtc(data,"clit"))
            self.breast = breast(f.dtc(data,"breast"))
        if gender != "female":
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
        self.ovulation_date = f.dtc(data,"ovulation_date")#排卵日
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
