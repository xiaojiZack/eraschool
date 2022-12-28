from faulthandler import disable
import erajs.api as a

def research_page():
    def check_available(require):
        for i in require:
            if i == '无':pass
            else: 
                if i in a.sav()['科技']: pass
                else: return False
        return True
    
    def begin_research(tech,time):
        #开始研究
        def check(require):
            #检查资源是否充足
            for i in require:
                if a.sav()['资源'][i]<require[i]:
                    return False
            return True
        if check(a.dat()['tech_item'][tech]['研发费用']):
            for i in a.dat()['tech_item'][tech]['研发费用']:
                a.sav()['资源'][i] -= a.dat()['tech_item'][tech]['研发费用'][i]
            if time == 0:
                #0时研发直接完成
                a.sav()['科技'].append(tech) 
                a.msg('[{}]研发完成'.format(tech))
                if '课程:' in tech:
                    temp = tech.replace('课程:','')
                    a.sav()['可用教案'].append(temp)
            else:
                l = a.sav()['正在研发']
                l[tech] = time
                a.msg('开始研发[{}]'.format(tech))
        else:
            a.msg('资源不足')
        a.repeat()
    
    def stop_research(tech):
        #终止研发
        del a.sav()['正在研发'][tech]
        a.msg('取消了[{}]的研发,已退还费用'.format(tech))
        for i in a.dat()['tech_item'][tech]['研发费用']:
            a.sav()['资源'][i] += a.dat()['tech_item'][tech]['研发费用'][i]
        a.repeat()
    
    a.cls()
    a.page()
    a.mode('grid',1)
    a.h('研发部')

    a.divider('已经研发')
    for i in a.sav()['科技']:
        a.b('[{}]'.format(i),popup = '{}'.format(a.dat()['tech_item'][i]['描述']))

    a.divider('当前研发')
    for i in a.sav()['正在研发']:
        a.b('[{}:{}周]'.format(i,a.sav()['正在研发'][i]), stop_research,i)

   

    a.divider('可开发项目')
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
    