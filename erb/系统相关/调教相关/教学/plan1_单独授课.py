import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo, print_kojo
from erb.系统相关.页面.train_page import train_page
from erb.系统相关.页面.check_character import detail_character
from erb.系统相关.人物相关.character_creat import creat_normal_character
def plan1():
    #单独授课，即进入调教页面
    def plan():
        a.page()
        a.mode()
        a.t('要对谁进行单独指导呢？')
        a.divider()
        a.mode('grid',7)
        a.tmp()['调教数据']={}
        a.tmp()['调教数据']['参与者'] = []
        a.tmp()['调教数据']['参与者'].append(a.sav()['character_list']['主角'])
        cl = a.sav()['character_list']['学生']
        for i in cl:
            c = cl[i]
            a.b(c['名字'], a.goto, detail_character, c)
            a.t()
            if c['性别'] == '男性':
                a.t('♂')
            elif c['性别'] == '女性':
                a.t('♀')
            else:
                a.t('♀♂')
            a.t()
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
            #a.t(c['学籍']['班级'])
            a.t()
            a.b('决定',dertermine,c)
            a.t()
    a.cls()
    a.goto(plan)

def dertermine(c):
    a.tmp()['调教数据']['参与者'].append(c)
    a.tmp()['调教数据']['调教者'] = 0
    a.tmp()['调教数据']['被调教'] = c['CharacterId']
    a.tmp()['调教数据']['尺寸警告标志'] = True
    a.tmp()['调教数据']['破处警告标志'] = True
    a.tmp()['调教数据']['润滑警告标志'] = True
    a.tmp()['显示记忆'] = True
    a.tmp()['执行列表'] = []
    a.tmp()['高潮名单'] = {}
    a.tmp()['高潮口上记录'] = {
        '射精':{},#{谁射精(id),谁被射(id),射在哪，{射了什么}}
        '绝顶':{},#{谁绝顶(id):{哪个部位:绝顶程度}}
        '被射高潮':{},#{谁射精(id),谁被射(id),哪个部位}
        '淫纹':{}
    }
    a.tmp()['待显示口上'] = []
    a.tmp()['特殊事件'] = []
    a.tmp()['正在执行'] = False
    a.tmp()['去冲突标志'] = False

    comkojo(a.tmp()['调教数据']['参与者'], c, -1, {'特殊事件':['开场']})
    a.page()
    print_kojo()
    a.goto(train_page)
