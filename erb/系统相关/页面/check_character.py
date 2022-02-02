from tkinter.ttk import Style
from erajs import api as a


def check_character():
    a.page()
    a.mode('grid',4)
    a.divider()
    cl = a.sav()['character_list']['学生']
    for i in cl:
        c = cl[i]
        a.b('{}'.format(c['名字']), a.goto, detail_character, c)
        a.t()
        if c['性别'] == '男性':
            a.t('♂')
        elif c['性别'] == '女性':
            a.t('♀')
        else:
            a.t('♀♂')
        a.t()
        a.t('体')
        a.progress(c['体力值'],c['最大体力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
        a.t()
        a.t('智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
        a.t()
        # a.t(c['学籍']['班级'])
        # a.t()
    a.divider()
    a.b('返回',a.back)

def detail_character(c):
    def page_1():
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider()
        a.mode('grid',1)
        a.h(c['名字'])
        a.divider()
        a.mode('grid', 3)
        a.t('性别:{}'.format(c['性别']))
        a.t()
        a.t('好感度:{}'.format(c['好感度']))
        a.t()
        a.t('侍奉快乐:{}'.format(c['侍奉快乐']))
        a.t()
        # a.t('种族:{}'.format(c['种族']))
        # a.t()
        a.t('体力:')
        a.progress(c['体力值'],c['最大体力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
        a.t()
        a.t('气力:')
        a.progress(c['气力值'],c['最大气力值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['气力值'],c['最大气力值']))
        a.t()
        a.t('理智:')
        a.progress(c['理智值'],c['最大理智值'], [{'width': '100px'}, {}])
        a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
        a.t()
        #胎内精液量
        a.divider('体型')
        a.mode('grid',5)
        a.t('身高:{}cm'.format(c['身体信息']['具体身高']))
        a.t()
        a.t('体重:{}kg'.format(c['身体信息']['具体体重']))
        a.t()
        if c['性别']!='男性':
            a.t('胸部:{}'.format(c['身体信息']['三围']['B']))
            a.t()
            a.t('腰部:{}'.format(c['身体信息']['三围']['H']))
            a.t()
            a.t('臀部:{}'.format(c['身体信息']['三围']['W']))
        a.divider('属性')
        a.mode('grid',1)
        q = c['属性']
        for i in q:
            if (len(q[i]) != 0):
                a.t('{}:'.format(i))
                for j in q[i]:
                    a.t('[{}]'.format(j))
                a.t()
        a.divider('经验')
        q = c['经验']
        a.mode('grid', 6)
        for i in q:
            if q[i] != 0:
                a.t('{}:{}'.format(i, q[i]))
                a.t()
        a.divider('身体开发')
        q = c['开发']
        for i in q:
            a.t('{}:Lv{}'.format(i, q[i]))
            a.t()
        a.divider()
        a.mode('grid',2)
        a.b('第二页',page_2)
        a.t()
        a.b('返回',a.back)
    def page_2():
        a.page()
        a.mode()
        a.b('返回',a.back)
        a.divider('堕落记忆')
        a.mode('grid', 6)
        q = c['记忆']
        for i in q:
            if q[i] != 0:
                a.t('{}:{}'.format(i, q[i]))
                a.t()
        a.divider('精神刻印')
        q = c['刻印']
        for i in q:
            a.t('{}:{}'.format(i, q[i]))
            a.t()
        a.divider()
        a.mode('grid',2)
        a.b('第一页',page_1)
        a.t()
        a.b('返回',a.back)
    page_1()