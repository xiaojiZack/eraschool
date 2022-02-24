import erajs.api as a
import erb.系统相关.人物相关.character_class as c

def DebugPage():
#用于加入debug按钮，可以在此查看和编辑后台数据
    def CheckThedata(target):
        def ExpandorShowdata(target, targetname):

            def SeeAndChangeIntOrChar(target, targetname, type):
                def inputback(value):
                    path = ""
                    for i in pathlist:
                        path = path+i
                    if (type=="list"): path = path+"[{}]".format(targetname)
                    else: path = path+"[\"{}\"]".format(targetname)
                    exec('a.sav()'+path+'=value')

                a.t("{}:".format(targetname))
                a.input(inputback, target)

            def show_path():
                path = ""
                for i in pathlist:
                    if (i!=''):path = path+"/"+i
                a.t(path)
                a.t()

            def BackandPopPath():
                del pathlist[-1]
                a.back()

            def Addpath():
                if (pathlist[-1]!=targetname):pathlist.append(targetname)

            def ExpandForDifferentType(subtarget,targetname, typeinput):
                if (isinstance(subtarget,(str,int))):
                        SeeAndChangeIntOrChar(subtarget, targetname, typeinput)
                elif(isinstance(subtarget,(dict,list))):
                    if (typeinput == "dict"): 
                        path = "[\"{}\"]".format(targetname)
                    else: 
                        path = "[{}]".format(targetname)
                    a.b("{}|{}".format(
                            targetname,str(type(subtarget))),
                            a.goto,ExpandorShowdata,subtarget, path)
                else:a.t(str(subtarget)+str(type(subtarget)))
                a.t()

            Addpath()
            a.page()
            if (len(pathlist)!=1):
                show_path()
                a.b('返回上级',BackandPopPath) 
                a.t()
            if (isinstance(target,(dict))):
                for i in target: 
                    ExpandForDifferentType(target[i],i,"dict")
            elif(isinstance(target,(list))):
                for index,subtarget in enumerate(target):
                    ExpandForDifferentType(subtarget,index,"list")

        a.page()
        pathlist = ['']
        ExpandorShowdata(target, "")
        a.t()
        a.b('back',a.back)

    a.page()
    a.mode()
    a.b('tmp临时数据', a.goto, CheckThedata, a.tmp())
    a.b('dat静态数据', a.goto, CheckThedata, a.dat())
    a.b('sav存档数据', a.goto, CheckThedata, a.sav())
    a.b('cfg配置数据', a.goto, CheckThedata, a.cfg())
    a.t()
    a.b('back',a.back)

def debug():
    if (a.cfg()['debug'] == True):
        a.b('debug', a.goto, DebugPage)

def disktoinitclass(data, property):
    if data == None:
        return None
    if property in data:
        return data[property]
    elif "{}".format(property) in data:
        return data["{}".format(property)]
    else:
        return None

dtc = disktoinitclass

def classtodict(item):
    #字典化
    data = {}
    allowedtype = ['int','list','dict','bool','str','set','tuple','float','double','NoneType']
    if (type(item).__name__ in allowedtype):
        return item
    else:
        for i in item.__dict__:
            arr = item.__dict__[i]
            data[str(i)] = classtodict(arr)
        return data

ctd = classtodict

def test_character():
    def test_load():
        def load():
            a.sav()['character'] = {}
            a.page()
            a.widget_load()
        a.page()
        a.button('读档',a.goto,load)
        
        a.b("check",a.goto,DebugPage)

    data = {'BasicProperty':{
                'name':['test', 2, {"x":1}],
                'gender':'female',
                'race':'human'
                },
            }
    
    a.page()
    test_chara = c.CharacterClass(data)
    testdict = test_chara.ToDict()
    new_chara = c.CharacterClass(testdict)
    pass
    a.t(testdict)
    a.sav()['character']={}
    a.sav()['character']['testdict'] = testdict
    a.widget_save()
    a.button('读档',a.goto,test_load)
    a.b("check",a.goto,DebugPage)

def colorful_progress(now, max, style = None):
    if (now > max*0.5):
        color = '#0f0'
    elif(now>max*0.2):
        color = '#0ff'
    else:
        color = '#f00'
    style.append({'color':color})
    style.append({'background-color': color})
    a.progress(now, max, style)