import erajs.api as a
from erb.系统相关.口上相关.口上.示例 import kojosample
from erb.系统相关.口上相关.口上工具 import show_kojo
from erb.系统相关.口上相关.地文.comkojo import describe_kojo


def comkojo(attenders, person, comnumber, information={}):
    #指令调用口上的统一函数，根据口上人物找到对应文件，根据条件装载口上列表
    kojoid = person['kojo']
    describe_kojo(person, attenders, comnumber, information)
    eval('{}(person, attenders, comnumber, information)'.format(kojoid))
    
def print_kojo():
    show_kojo()