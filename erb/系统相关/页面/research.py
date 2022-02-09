from faulthandler import disable
import erajs.api as a

def research_page():
    def check_available(require):
        for i in require:
            if i == '无':pass
            else: 
                if not i in a.sav()['科技']: pass
                else: return False
        return True
    
    def begin_research(tech,time):
        def check(require):
            for i in require:
                if a.sav()['资源'][i]<require[i]:
                    return False
            return True
        if check(a.dat()['tech_item'][tech]['研发费用']):
            for i in a.dat()['tech_item'][tech]['研发费用']:
                a.sav()['资源'][i] -= a.dat()['tech_item'][tech]['研发费用'][i]
            l = a.sav()['正在研发']
            l[tech] = time
            a.msg('开始研发[{}]'.format(tech))
        else:
            a.msg('资源不足')
        a.repeat()
    
    def stop_research(tech):
        del a.sav()['正在研发'][tech]
        a.msg('取消了[{}]的研发,已退还费用'.format(tech))
        for i in a.dat()['tech_item'][tech]['研发费用']:
            a.sav()['资源'][i] += a.dat()['tech_item'][tech]['研发费用'][i]
        a.repeat()
    
    a.cls()
    a.page()
    a.mode('grid',1)
    a.h('研发部')
    a.divider('当前研发')
    for i in a.sav()['正在研发']:
        a.b('[{}:{}周]'.format(i,a.sav()['正在研发'][i]), stop_research,i)
    a.divider()
    a.mode('grid',3)
    tech_list = a.dat()['tech_item']
    for i in tech_list:
        t = tech_list[i]
        if check_available(t['前置']) and not i in a.sav()['科技'] and not i in a.sav()['正在研发']:
            a.b('[{}]'.format(i),begin_research, i,t['时间'], popup = '{}'.format(t['描述']))
            a.t()
            for j in t['研发费用']:
                a.t('{}:{}\n'.format(j,t['研发费用'][j]))
            a.t()
            a.t('{}周'.format(t['时间']))
            a.t()
    a.divider()
    a.b('返回',a.back)
    