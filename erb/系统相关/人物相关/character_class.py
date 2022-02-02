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
    t= a.sav()['character_list']['character_number']
    new_character = {
        'CharacterId': int(t+1), '名字': '主人公', '外表年龄': '青年', '种族': '人类', '性别': '男性', 
        'koujo': '', '最大体力值': 0, '体力值': 0, '最大气力值': 0, 
        '气力值': 0, '最大理智值': 0, '理智值': 0, '好感度':0,'侍奉快乐':0,
                     '身体信息': {
                         '三围': {},'具体身高':0, '具体体重':0,
                         '肛门': {'改造': [], '内容固体': {}, '尺寸': ''}, 
                         '肠胃': {'容量': 0,'内容总量':0, '内容液体': {}, '改造': []}, 
                         '尿道': {'容量': 0,'内容总量':0, '内容液体': {}, '内容固体': {}, '改造': [], '尺寸': ''}, 
                         '口喉': {'改造': []}, 
                         '子宫': {'容量': 0,'内容总量':0, '内容液体': {}, '内容固体': {}, '危险日': 0, '怀孕标志': False, '改造': [], '胎儿信息': {}}, 
                         '阴道': {'容量': 0, '内容总量':0, '内容液体': {}, '内容固体': {}, '改造': [], '尺寸': ''}, 
                         '阴核': {'改造': []}, 
                         '乳房': {'容量': 0, '内容总量':0,'内容液体': {}, '生产速度': 0, '改造': [], '尺寸': '', '标准射出量': 0}, 
                         '阴茎': {'尺寸':'','容量': 0,'内容总量':0, '内容液体': {}, '生产速度': 0, '改造': [], '长度': 0, '直径': 0, '标准射出量': 0,'忍耐极限':10000,}}, 
                     '经验': {'C经验': 0, 'V经验': 0, 'B经验': 0, 'A经验': 0, '绝顶经验': 0, '精液经验': 0, 
                                'V扩张经验':0,'A扩张经验':0,
                                '喷乳经验': 0, '射精经验': 0, '漏尿经验': 0, '排泄经验': 0, '自慰经验': 0, 
                                '百合经验': 0, '男同经验': 0, '露出经验': 0, '侍奉经验': 0, '爱情经验': 0, '口交经验': 0, 
                                '腔射经验': 0, '肛射经验': 0, '腔内储精经验':0, '肠内储精经验':0,'子宫储精经验':0,
                                '饮精经验': 0, '亲吻经验': 0, '苦痛经验': 0, '受缚经验': 0, 
                                'SM经验': 0, '药物经验': 0, 'V插入经验': 0, 'A插入经验': 0, '异常经验': 0, '出产经验': 0, 
                                '被摄经验': 0, '卖春经验': 0, '艳舞经验': 0, '触手经验': 0, '兽奸经验': 0, '助手经验': 0
                                }, 
                     '记忆': {'快C记忆': 0, '快V记忆': 0, '快B记忆': 0, '快A记忆': 0, '快M记忆':0, '快P记忆':0, '快W记忆'
                                '习得记忆': 0, '恭顺记忆': 0, '欲情记忆': 0, '屈服记忆': 0, 
                                '羞耻记忆': 0, '苦痛记忆': 0, '恐惧记忆': 0, '药毒记忆': 0, '同化记忆': 0, '主导记忆': 0, '否定记忆': 0}, 
                     '开发': {'C感觉': 0, 'V感觉': 0, 'B感觉': 0, 'A感觉': 0, 'M感觉':0, 'P感觉':0,'W感觉':0,
                                '服从': 0, '欲望': 0, '侍奉欲望': 0, 
                                'V名器度':0, 'A名器度':0,'V扩张度':0,'A扩张度':0,'喉名器度':0,'喉扩张度':0,
                                '尿道名器度':0,'尿道扩张度':0,'指技':0,'口技':0,'腰技':0,'足技':0,'魔乳':0,
                                '露出癖': 0, 'S属性': 0, 'M属性': 0, '百合中毒': 0, '男同中毒': 0, '喷乳中毒': 0, '射精中毒': 0, 
                                '精液成瘾': 0, '自慰成瘾': 0, '药物成瘾': 0, '被射中毒': 0, 
                                '排泄成瘾': 0, '触手适性': 0, '兽交中毒': 0, '受孕成瘾': 0}, 
                     '刻印': {'苦痛刻印': 0, '快乐刻印': 0, '屈服刻印': 0, '药毒刻印': 0, '羞耻刻印': 0, '恐惧刻印': 0, '反发刻印': 0, 
                              '同化刻印': 0}, 
                     '学籍': {'班级': '', '成绩': {}, '社团': ''}, 
                     '属性': {'个性': [], '体质': [], '技能': [], '性癖': [], '其他': []},
                     '调教记忆':{'快C':0, '快V':0, '快B':0, '快A':0, '快M':0, '快P':0, '快W':0,
                        'V润':0,'A润':0,'习得':0, '恭顺':0, '欲情':0, '屈服':0, 
                        '羞耻':0, '苦痛':0, '恐惧':0, '药毒':0, '同化':0, '主导':0, '反感':0},
                     '其他参数':{'性欲':0,'精液欲':0,'尿意':0,'排泄欲':0,'本次绝顶次数':0,'本次精液次数':0,'射精数值':0,'射精极限':10000},
                     '待处理记忆':{'快C':0, '快V':0, '快B':0, '快A':0, '快M':0, '快P':0, '快W':0,
                        'V润':0,'A润':0,'习得':0, '恭顺':0, '欲情':0, '屈服':0, 
                        '羞耻':0, '苦痛':0, '恐惧':0, '药毒':0, '同化':0, '主导':0, '反感':0},
                     '待处理经验':{'C经验': 0, 'V经验': 0, 'B经验': 0, 'A经验': 0, '绝顶经验': 0, '精液经验': 0, 
                                'V扩张经验':0,'A扩张经验':0,
                                '喷乳经验': 0, '射精经验': 0, '漏尿经验': 0, '排泄经验': 0, '自慰经验': 0, 
                                '百合经验': 0, '男同经验': 0, '露出经验': 0, '侍奉经验': 0, '爱情经验': 0, '口交经验': 0, 
                                '腔射经验': 0, '肛射经验': 0, '腔内储精经验':0, '肠内储精经验':0,'子宫储精经验':0,
                                '饮精经验': 0, '亲吻经验': 0, '苦痛经验': 0, '受缚经验': 0, 
                                'SM经验': 0, '药物经验': 0, 'V插入经验': 0, 'A插入经验': 0, '异常经验': 0, '出产经验': 0, 
                                '被摄经验': 0, '卖春经验': 0, '艳舞经验': 0, '触手经验': 0, '兽奸经验': 0, '助手经验': 0
                                }, 
                     '衣物':[],
                     '标志':{'助手':False},
                     }
    return new_character

def search_quaility(c,target):
    for i in c['属性']:
        for j in c['属性'][i]:
            if j == target:
                return True
    return False

def remove_quaility(c,target):
    if search_quaility(c,target):
        for i in c['属性']:
            for j in c['属性'][i]:
                if j == target:
                    c['属性'][i].remove(target)
                    return True
    else:
        return False
# class CharacterClass:
#     def __init__(self,data):
#         self.BasicProperty = BasicProperty(
#             f.dtc(data,"BasicProperty"))
#         self.BodyProperty = BodyProperty(f.dtc(data,"BodyProperty"),
#             self.BasicProperty.gender)
#         self.SexExp = SexExp(f.dtc(data,"SexExp"))
#         self.Memory = Memory(f.dtc(data,"Memory"))
#         self.SexSkill = SexSkill(f.dtc(data,"SexSkill"))
#         self.Mark = Mark(f.dtc(data,"Mark"))
#         self.StudentStute = StudentStute(
#             f.dtc(data,"StudentStute"))
#         self.Quaility = Quaility(f.dtc(data,"Quaility"))
#     def ToDict(self):
#         return f.classtodict(self)

# class BasicProperty:

#     def __init__(self, data):
#         self.CharacterId = f.dtc(data,"characterid")
#         self.name = f.dtc(data,"name")
#         self.race = f.dtc(data,"race")
#         self.gender = f.dtc(data,"gender")
#         self.koujo = f.dtc(data,"koujo")
#         self.MAXPhysicalPower = f.dtc(data,"MaxPhysicalPower")
#         self.PhysicalPower = self.MAXPhysicalPower
#         self.MAXEnergyPower = f.dtc(data,"MaxEnergyPower")
#         self.EnergyPower = self.MAXEnergyPower
#         self.MAXMindPower = f.dtc(data,"MaxMindPower")
#         self.MindPower = self.MAXMindPower
    
# class BodyProperty:#身体实体

#     def __init__(self,data,gender):
#         self.BWH = f.dtc(data,"BWH")
#         self.weight = f.dtc(data,"weight")
#         self.height = f.dtc(data,"height")
#         self.ass = ass(f.dtc(data,"ass"))
#         self.stomach = stomach(f.dtc(data,"stomach"))
#         self.urethe = urethe(f.dtc(data,"urethe"))
#         self.mouth = mouth(f.dtc(data,"mouth"))
#         if gender != "male":
#             self.womb = womb(f.dtc(data,"womb"))
#             self.vagina = vagina(f.dtc(data,"vagina"))
#             self.clit = clit(f.dtc(data,"clit"))
#             self.breast = breast(f.dtc(data,"breast"))
#         if gender != "female":
#             self.penis = penis(f.dtc(data,"penis"))
            
# class SexExp:#性经验

#     def __init__(self,data):
#         self.c = f.dtc(data,"c")
#         self.v = f.dtc(data,"v")
#         self.b = f.dtc(data,"b")
#         self.a = f.dtc(data,"a")
#         self.orgasm = f.dtc(data,"orgasm")
#         self.semen = f.dtc(data,"semen")
#         self.ejectmilk = f.dtc(data,"ejectmilk")
#         self.ejectsemen = f.dtc(data,"ejectsemen")
#         self.pee = f.dtc(data,"pee")#放尿
#         self.excrete = f.dtc(data,"excrete")#排泄
#         self.masturbation = f.dtc(data,"masturbation")#自慰
#         self.lesbian = f.dtc(data,"lesbian")#蕾丝
#         self.gay = f.dtc(data,"gay")
#         self.expose = f.dtc(data,"expose")
#         self.serve = f.dtc(data,"serve")#服侍
#         self.love = f.dtc(data,"love")#爱情
#         self.belowjob = f.dtc(data,"belowjob")#口交
#         self.cuminv = f.dtc(data,"cuminv")#腔射经验
#         self.cumina = f.dtc(data,"cumina")#肛射经验
#         self.drinksemen = f.dtc(data,"drinksemen")
#         self.kiss = f.dtc(data,"kiss")
#         self.pain = f.dtc(data,"pain")
#         self.bounded = f.dtc(data,"bounded")
#         self.SM = f.dtc(data,"SM")
#         self.drug = f.dtc(data,"drug")
#         self.vinsert = f.dtc(data,"vinsert")
#         self.ainsert = f.dtc(data,"ainsert")
#         self.abnormal = f.dtc(data,"abnormal")
#         self.givebrith = f.dtc(data,"givebrith")
#         self.bephoto = f.dtc(data,"bephoto")#被摄影
#         self.harlotry = f.dtc(data,"harlotry")#卖春
#         self.sexdance = f.dtc(data,"sexdance")
#         self.tentacle = f.dtc(data,"tentacle")
#         self.animalsex = f.dtc(data,"animalsex")
#         self.assistant = f.dtc(data,"assistant")#助手

# class Memory:#**之珠

#     def __init__(self,data):
#         self.c = f.dtc(data,"c")
#         self.v = f.dtc(data,"v")
#         self.b = f.dtc(data,"b")
#         self.a = f.dtc(data,"a")
#         self.learn = f.dtc(data,"learn")#习得
#         self.humbly = f.dtc(data,"humbly")#恭顺
#         self.desire = f.dtc(data,"desire")#欲望
#         self.surrender = f.dtc(data,"surrender")#屈服
#         self.shame = f.dtc(data,"shame")#羞耻
#         self.pain = f.dtc(data,"pain")#苦痛
#         self.fear = f.dtc(data,"fear")#恐怖
#         self.drug = f.dtc(data,"drug")#药毒
#         self.assimile = f.dtc(data,"assimile")#同化
#         self.initiative = f.dtc(data,"initiative")#主动
#         self.unhappy = f.dtc(data,"unhappy")#否定

# class SexSkill:#开发等级
#     def __init__(self,data):
#         self.c = f.dtc(data,"c")#c感觉
#         self.v = f.dtc(data,"v")
#         self.b = f.dtc(data,"b")
#         self.a = f.dtc(data,"a")
#         self.humbly = f.dtc(data,"humbly")#恭顺
#         self.desire = f.dtc(data,"desire")#欲望
#         self.skillness = f.dtc(data,"skillness")#技巧
#         self.serve = f.dtc(data,"serve")#侍奉
#         self.expose = f.dtc(data,"expose")
#         self.S = f.dtc(data,"S")
#         self.M = f.dtc(data,"M")
#         self.lesbian = f.dtc(data,"lesbian")#蕾丝
#         self.gay = f.dtc(data,"gay")
#         self.ejectmilk = f.dtc(data,"ejectmilk")
#         self.ejectsemen = f.dtc(data,"ejectsemen")
#         self.semenaddiction = f.dtc(data,"semenaddiction")
#         self.masturbationaddiction = f.dtc(data,"masturbationaddiction")
#         self.drugaddiction = f.dtc(data,"drugaddiction")
#         self.cuminsideaddiction = f.dtc(data,"cuminsideaddiction")#内射
#         self.excreteaddiction = f.dtc(data,"excreteaddiction")#排泄
#         self.tentacle = f.dtc(data,"tentacle")
#         self.animalsex = f.dtc(data,"animalsex")
#         self.pergencyaddiction = f.dtc(data,"pergencyaddiction")#怀孕中毒

# class Mark:#刻印
#     def __init__(self,data):
#         self.pain = f.dtc(data,"pain")
#         self.happy = f.dtc(data,"happy")
#         self.surrender = f.dtc(data,"surrender")
#         self.drug = f.dtc(data,"drug")
#         self.shame = f.dtc(data,"shame")
#         self.fear = f.dtc(data,"fear")
#         self.unhappy = f.dtc(data,"unhappy")#反发
#         self.assimile = f.dtc(data,"assimile")#同化

# class Cloth:
#     #todo
#     def __init__(self,data):
#         pass

# class StudentStute:#学籍系统

#     def __init__(self,data):
#         self.classgroup = f.dtc(data,"classgroup")
#         self.score = f.dtc(data,"score")
#         self.club = f.dtc(data,"club")

# class Tattoo:#淫纹
#     #todo
#     def __init__(self):
#         pass

# class Quaility:#特质
    
#     def __init__(self,data):
#         self.个性 = f.dtc(data,"个性")#性格
#         self.体质 = f.dtc(data,"体质")#身体特质
#         self.技能 = f.dtc(data,"技能")#特长
#         self.leaning = f.dtc(data,"leaning")#性癖
#         self.others = f.dtc(data,"others")

# class womb:
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.contentobject = f.dtc(data,"contentobject")
#         self.ovulation_date = f.dtc(data,"ovulation_date")#排卵日
#         self.PregnancyFlag = f.dtc(data,"PregnancyFlag")
#         self.transform = f.dtc(data,"transform")
#         self.Pregnancy = f.dtc(data,"Pergnancy")  
# class vagina:
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.contentobject = f.dtc(data,"contentobject")
#         self.transform = f.dtc(data,"transform")
#         self.size = f.dtc(data,"size")
# class clit:
#     def __init__(self,data):
#         self.transform = f.dtc(data,"transform")
# class penis:#实际上包含金玉
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.producerate = f.dtc(data,"producerate")
#         self.transform = f.dtc(data,"transform")
#         self.length = f.dtc(data,"length")
#         self.diameter = f.dtc(data,"diameter")
#         self.ejectrate =f.dtc(data,"ejectrate")#标准射精量
# class breast:
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.producerate = f.dtc(data,"producerate")
#         self.transform = f.dtc(data,"transform")
#         self.size = f.dtc(data,"size")
#         self.ejectrate =f.dtc(data,"ejectrate")#标准射乳量   
# class ass:
#     def __init__(self,data):
#         self.transform = f.dtc(data,"transform")
#         self.contentobject = f.dtc(data,"contentobject")
#         self.size = f.dtc(data,"size")
#         self.buttsize = f.dtc(data,"buttsize")
# class stomach:
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.transform = f.dtc(data,"transform")       
# class mouth:
#     def __init__(self,data):
#         self.transform = f.dtc(data,"transform")
# class urethe:
#     def __init__(self,data):
#         self.volume = f.dtc(data,"volume")
#         self.contentliquid = f.dtc(data,"contentliquid")
#         self.contentobject = f.dtc(data,"contentobject")
#         self.transform = f.dtc(data,"transform")
#         self.size = f.dtc(data,"size")
