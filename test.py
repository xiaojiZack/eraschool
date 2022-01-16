
# -*- coding: utf-8 -*-
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
    def test_B(self):
        print ('func named test_B')


class test:
    name = ['A','B']
    def __init__(self):
        for i in self.name:
            exec("self.__dict__[{}] = {}(\"{}\")".format(i,i,"jack"))
            pass

t = test()
pass