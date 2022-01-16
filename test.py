import erajs.api as a
import funcs as f
print(type(2).__name__ == 'classobj')
class A():
    a = 0
    name = None
    b = 1
    def __init__(self,name):
        self.a = 2
        self.b = 3
        self.name = name
    def test(self):
        print ('a normal func.')
class B(A):
    x = 1
    list1 = [1, 2,3]
    dict1 = {"1":2}
    def test_B(self):
        print ('func named test_B')


class test:
    name = ['A','B']
    def __init__(self):
        for i in self.name:
            exec("self.{} = {}(\"{}\")".format(i,i,"jack"))
            pass
    def ctd(self):
        return f.classtodict(self)

t = test()
x = str(type(t).__name__)


print(t.ctd())
pass