import erajs.api as a
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
        a.mode('grid',6)
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
            a.t('体')
            a.progress(c['体力值'],c['最大体力值'], [{'width': '100px'}, {}])
            a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
            a.t()
            a.t('san:')
            a.progress(c['理智值'],c['最大理智值'], [{'width': '100px'}, {}])
            a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
            a.t()
            #a.t(c['学籍']['班级'])
            a.t()
            a.b('决定',dertermine,c)
            a.t()
    a.goto(plan)

def dertermine(c):
    a.tmp()['调教数据']['参与者'].append(c)
    a.tmp()['调教数据']['调教者'] = 0
    a.tmp()['调教数据']['被调教'] = c['CharacterId']
    a.tmp()['调教数据']['尺寸警告标志'] = True
    a.tmp()['显示记忆'] = True
    a.tmp()['执行列表'] = []
    
    a.goto(train_page)