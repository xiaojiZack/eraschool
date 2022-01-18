import erajs.api as a
import funcs as f

class testclass():
    def __init__(self):
        self.i = 1

def test1():
    def adddata():
        i = a.sav()['testdata']
        i = i +1
        a.sav()['testdata'] = i
        a.repeat()
    def addclass():
        x = a.sav()['testclass']
        x.i = x.i +1
        #a.sav()['testclass'].i = i
        a.repeat()
    def addlist():
        i = a.sav()['testlist']
        s = i[0]
        s = s+1
        #a.sav()['testlist'][0] = i
        a.repeat()
    a.page()
    a.t(a.sav()['testdata'])
    a.b('+1', adddata)
    a.t()
    a.t(a.sav()['testclass'].i)
    a.b('+1', addclass)
    a.t()
    a.t(a.sav()['testlist'][0])
    a.b('+1', addlist)

def inputtest(i, c):
    c[0] = i
    a.t(c[0])

a.init()
a.sav()['testclass'] = testclass()
a.sav()['testdata'] = 1
a.sav()['testlist'] = [1]
a.button('test', a.goto,test1)
x = None
list1 = a.sav()['testlist'].copy()
a.input(inputtest, '', list1)



