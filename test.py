import erajs.api as a

class test1:
    num = 1
    list = [1]
    def delect(self):
        del self

class test2:
    num = 2
    list = [1]
    def delect(self):
        del self

def debug():

    def DebugTmp():
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
        tmp = a.tmp()
        pathlist = ['']
        ExpandorShowdata(tmp, "")
        a.t()
        a.b('back',a.back)

    a.page()
    a.mode()
    a.b('tmp', a.goto, DebugTmp)
    a.t()
    a.b('back',a.back)


def Launcher():
    a.page()
    blue_pic = {"1":test1, "2":test2}
    x = blue_pic["1"]()
    a.t(x.num)
    a.tmp()['testdebug'] = 2
    a.tmp()["testdebuglist"] = [1, 2, {"1":1, "2":2}] 
    print(a.tmp().keys())
    a.b('debug',a.goto,debug)


a.init()
a.goto(Launcher)