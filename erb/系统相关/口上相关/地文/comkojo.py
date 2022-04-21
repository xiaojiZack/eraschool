import erajs.api as a
from erb.系统相关.口上相关.口上工具 import comadd, comdoing, comfail, comundo, pt, push_text

def describe_kojo(person, attenders, comnumber, information):
    p = person
    at = None
    ats = None
    if get_attenders(attenders):
        at = attenders[0]
        ats = attenders
    else:
        at = attenders
    com = comnumber
    inf = information
    pn = p['名字']
    atn = at['名字']
    if com == 1:
        #爱抚
        if(comadd(inf)):
            push_text('{}用'.format(at['名字'])+'手'+'攀上了'+'{}'.format(person['名字'] +'身体'))
            pt()
        if(comdoing(inf)):
            push_text('{}用'.format(at['名字'])+'手'+'轻柔地抚摸'+'{}'.format(person['名字']))
            pt()
        if(comundo(inf)):
            push_text('{}'.format(pn)+'架开了'+'{}'.format(atn),{'color':'#f00'})
            pt()
        if(comfail(inf)):
            push_text('{}用'.format(at['名字'])+'手'+'离开了'+'{}'.format(person['名字'] +'身体'))
            pt()
            

def get_attenders(at):
    if isinstance(at,list):
        return True
    else:
        return False