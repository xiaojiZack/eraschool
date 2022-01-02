import erajs.api as a

def debug():
    #用于加入debug按钮，可以在此查看和编辑后台数据
    def DebugMode(target):
        def ExpandorShowdata(target, targetname):

            def SeeAndChangeIntOrChar(target, targetname, type):
                def inputback(value):
                    path = ""
                    for i in pathlist:
                        path = path+i
                    if (type=="list"): path = path+"[{}]".format(targetname)
                    else: path = path+"[\"{}\"]".format(targetname)
                    exec('a.tmp()'+path+'=value')

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
                else:a.t(str(subtarget))
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
    a.b('tmp临时数据', a.goto, DebugMode, a.tmp())
    a.b('dat静态数据', a.goto, DebugMode, a.dat())
    a.b('sav存档数据', a.goto, DebugMode, a.sav())
    a.b('cfg配置数据', a.goto, DebugMode, a.cfg())
    a.t()
    a.b('back',a.back)