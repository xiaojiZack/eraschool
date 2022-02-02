from cmath import log10
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
        pp = pp *1.2
        ep = ep *1.2
    if sq(c,'癔病'):
        mp = mp *1.2
    m = c['待处理记忆']
    t = log10(max(m['苦痛']/100,1))
    if m['苦痛']>100:
        pp = pp*(1+0.2*int(log10(m['苦痛']/100+1)))
        ep = ep*(1+0.2*int(log10(m['苦痛']/100+1)))
    if m['恐惧']+m['反感']>100:
        mp = mp*(1+0.2*int(log10((m['恐惧']+m['反感'])/100+1)))
    
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
            c['体力值'] += c['气力值']*1.5
            a.t(' 气力值不足,体力减少{}'.format(c['气力值']*1.5))
            c['气力值'] = 0
        a.t()
        if (c['气力值']>0):
            a.t('理智:{}-{} = {}'.format(c['理智值'],ep,c['理智值']-ep))
            c['理智值'] -= mp
        elif (c['气力值'] == 0):
            a.t('理智:{}-{} = {}（气力不足)'.format(c['理智值'],ep,c['理智值']-ep))
            c['理智值'] -= mp*1.2
        a.t()
