import erajs.api as a
from ..人物相关.character_class import search_quaility as sq


def decrease_pp(c,d):
    if d == []:
        return 0
    pp = d[0]
    ep = d[1]
    mp = d[2]
    a.divider()
    a.mode()
    
    if sq(c,'病弱'):
        pp = pp *1.5
        ep = ep *1.5
    if sq(c,'癔病'):
        mp = mp *1.5
    m = c['待处理记忆']
    if m['苦痛']>100:
        pp = pp*(1+5*len(str(int(m['苦痛']/10))))
        ep = ep*(1+5*len(str(int(m['苦痛']/10))))
    if m['恐惧']+m['反感']>100:
        mp = mp*(1+5*len(str(int((m['恐惧']+m['反感'])/10))))

    
    pp = int(pp)
    ep = int(ep)
    mp = int(mp)

    a.t('[{}]'.format(c['名字']))
    a.t()
    a.t('体力:{}-{} = {}'.format(c['体力值'],pp,c['体力值']-pp))
    c['体力值'] -= pp
    a.t()
    if c['CharacterId'] != 0:
        a.t('气力:{}-{} = {}'.format(c['气力值'],ep,c['气力值']-ep))
        c['气力值'] -= ep
        if (c['气力值']<0):
            c['体力值'] += int(c['气力值']*0.5)
            a.t(' 气力值不足,体力减少{}'.format(c['气力值']*1.5))
            c['气力值'] = 0
        a.t()
        if (c['气力值']>0):
            a.t('理智:{}-{} = {}'.format(c['理智值'],mp,c['理智值']-mp))
            c['理智值'] -= mp
        elif (c['气力值'] == 0):
            a.t('理智:{}-{} = {}（气力不足)'.format(c['理智值'],int(mp*1.5),c['理智值']-int(mp*1.5)))
            c['理智值'] -= int(mp*1.5)
        if c['理智值']<0: c['理智值'] = 0
        a.t()

        #回复系药剂效果
        if 'hf' in c['药物效果']:
            if c['药物效果']['hf']>0:
                recover = 100*c['药物效果']['hf']
                c['体力值'] = min(c['最大体力值'], int(recover+c['体力值']))
                a.t('由于药剂效果，体力回复了:+{}->{}'.format(recover, c['体力值']))

def sum_pp(c,l):
    for i in range(0,3):
        c['待处理体力变化'][i] += l[i]
