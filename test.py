import erajs.api as a
import funcs as f

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


def Launcher():
    a.page()
    blue_pic = {"1":test1, "2":test2}
    x = blue_pic["1"]()
    a.t(x.num)
    a.tmp()['testdebug'] = 2
    a.tmp()["testdebuglist"] = [1, 2, {"1":1, "2":2}] 
    a.tmp()['x'] = [x]
    print(a.tmp().keys())
    f.debug()


a.init()
a.cfg()['debug'] = True
a.goto(Launcher)