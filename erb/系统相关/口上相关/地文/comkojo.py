import erajs.api as a
from erb.系统相关.口上相关.口上工具 import comadd, comdoing, comfail, comundo, pt, push_text
from erb.系统相关.口上相关.地文.语料 import changdao, duzi, gangmen, lian, niaodao, pigu, shenti, shou, xiong, yinbu, yindao, yinhe, yinjing

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
    if p!={}:
        pn = p['名字']
        pns = pn+'的'
    if at != {}:
        atn = at['名字']
        atns = atn+'的'

    #绝顶、射精、被射高潮
    if com == -1:
        pass

    #爱抚
    if com == 1:
        if(comadd(inf)):
            push_text(atn+'的手'+'攀上了'+pn +'的身体')
            pt()
        elif(comdoing(inf)):
            push_text(atn+'用手'+'轻柔地抚摸'+pn)
            pt()
        elif(comfail(inf)):
            push_text(pn+'架开了'+ atn + '的手',{'color':'#f00'})
            pt()
        elif(comundo(inf)):
            push_text(atn+'的手'+'离开了'+ pn +'的身体')
            pt()
    
    #胸爱抚
    elif com == 2:
        if comadd(inf):
            push_text(atn+'开始用'+shou(at)+'抚摸'+pn+'的'+xiong(p))
            pt()
        elif comdoing(inf):
            push_text(pn+'的'+xiong(p)+'在'+atn+'揉搓下变化着形状')
            pt()
        elif comfail(inf):
            push_text(pn+'架开了'+ atn + '抓向胸部的手',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'停止揉捏'+pn+'的'+xiong(p))
            pt()
    
    #肛门爱抚
    elif com == 3:
        if comadd(inf):
            push_text(atn+'用手指按揉'+pn+'的'+gangmen(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'的手指在'+pn+'的'+gangmen(p)+'边缘画着圈')
            pt()
        elif comfail(inf):
            push_text(pn+'扭开了'+pigu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'将手指从'+pn+'的'+pigu(p)+'缝中抽出来')
            pt()
    
    #舔弄V
    elif com == 4:
        if comadd(inf):
            push_text(atn+'把头埋进了'+pn+'的股间')
            pt()
        elif comdoing(inf):
            push_text(atn+'用舌头品尝着'+pn+'的'+yinbu(p))
            pt()
        elif comfail(inf):
            push_text(pn+'用手推开了'+atn+'的'+lian(at),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+'的股间抬起头来')
            pt()
    
    #手指插入V
    elif com == 5:
        if comadd(inf):
            push_text(atn+'把手指插进了'+pn+'的'+yinbu(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'的手指在'+pn+'的'+yinbu(p)+'里不停地抽插着')
            pt()
        elif comfail(inf):
            push_text(pn+'用手紧捂着'+yinbu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'把手指从'+pn+yinbu(p)+'中拔出来')
            pt()

    #手指插入A
    elif com == 6:
        if comadd(inf):
            push_text(atn+'把手指插进了'+pn+'的'+gangmen(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'的手指在'+pn+'的'+pigu(p)+'里不停地抽插着')
            pt()
        elif comfail(inf):
            push_text(pn+'用手紧捂着'+pigu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'把手指从'+pn+pigu(p)+'中拔出来')
            pt()
  
    #舔弄肛门
    elif com == 7:
        if comadd(inf):
            push_text(atn+'把'+lian(at)+'埋进了'+pn+'的'+pigu(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'用舌头品尝着'+pn+'的'+gangmen(p))
            pt()
        elif comfail(inf):
            push_text(pn+'用手推开了'+atn+'的'+lian(at),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+'的'+pigu(p)+'里抬起头来')
            pt()
    
    #阴部爱抚
    elif com == 8:
        if comadd(inf):
            push_text(atn+'把'+shou(at)+'伸向'+pn+'的'+yinhe(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'用'+shou(at)+'搓揉着'+pn+'的'+yinhe(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn+'的'+shou(at),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+'的'+'股间'+'抽出手来')
            pt()
    
    #展示阴道
    elif com == 9:
        if comadd(inf):
            push_text(pn+'听从命令，扒开了'+yinbu(p)+'向你展示了'+yindao(p))
            pt()
        elif comdoing(inf):
            push_text(pn+'展示着'+yindao(p))
            pt()
        elif comfail(inf):
            push_text(atn+'尝试命令'+pn+',但失败了',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'允许'+pn+'做别的事情')
            pt()
    
    #展示肛门
    elif com == 10:
        if comadd(inf):
            push_text(pn+'听从命令，扒开了'+pigu(p)+'向你展示了'+gangmen(p))
            pt()
        elif comdoing(inf):
            push_text(pn+'展示着'+gangmen(p))
            pt()
        elif comfail(inf):
            push_text(atn+'尝试命令'+pn+',但失败了',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'允许'+pn+'做别的事情')
            pt()
    
    #接吻
    elif com == 11:
        if comadd(inf):
            push_text(atn+'亲吻了'+pn)
            pt()
        elif comdoing(inf):
            push_text(atn+'与'+pn+'正交换着唾液')
            pt()
        elif comfail(inf):
            push_text(pn+'嫌恶地别开了'+lian(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'分开了亲吻的双唇，在两人唇间拉起了几道银丝。')
            pt()
    
    #自慰
    elif com == 12:
        if comadd(inf):
            push_text(atn+'命令'+pn+'开始自慰')
            pt()
        elif comdoing(inf):
            push_text(pn+'正在自慰')
            pt()
        elif comfail(inf):
            push_text(atn+'尝试命令'+pn+',但失败了',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止自慰')
            pt()

    #尿道指插入
    elif com == 13:
        if comadd(inf):
            push_text(atn+'把手指插进了'+pn+'的'+niaodao(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'的手指在'+pn+'的'+niaodao(p)+'里不停地抽插着')
            pt()
        elif comfail(inf):
            push_text(pn+'用手紧捂着'+niaodao(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'把手指从'+pn+niaodao(p)+'中拔出来')
            pt()
    
    #跳蛋
    elif com == 21:
        if comadd(inf):
            push_text(atn+'把跳蛋贴上'+pn+'的'+yinhe(p))
            pt()
        elif comdoing(inf):
            push_text('嗡鸣振动的跳蛋正紧贴着'+pn+'的'+yinhe(p))
            pt()
        elif comfail(inf):
            push_text(pn+'盯着跳蛋，用手紧捂着'+yinbu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'移开了跳蛋')
            pt()
    
    #跳蛋插入
    elif com == 22:
        if comadd(inf):
            push_text(atn+'把跳蛋塞进'+pn+'的'+yindao(p)+'后把开关跳到了最大')
            pt()
        elif comdoing(inf):
            push_text('几根电线深入'+pn+'的'+yindao(p)+'深处,'+pn+duzi(p)+'隐约凸显出了跳蛋的形状，小腹里嗡嗡作响')
            pt()
        elif comfail(inf):
            push_text(pn+'盯着跳蛋，用手紧捂着'+yinbu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+duzi(p)+'里拔出了跳蛋')
            pt()
    
    #跳蛋肛门插入
    elif com == 23:
        if comadd(inf):
            push_text(atn+'把跳蛋塞进'+pn+'的'+pigu(p)+'后把开关跳到了最大')
            pt()
        elif comdoing(inf):
            push_text('几根电线深入'+pn+'的'+gangmen(p)+'深处,'+pn+'的小腹里嗡嗡作响')
            pt()
        elif comfail(inf):
            push_text(pn+'盯着跳蛋，用手紧捂着'+pigu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+pigu(p)+'里拔出了跳蛋')
            pt()
    
    #电动按摩棒
    elif com == 24:
        if comadd(inf):
            push_text(atn+'把高速震动的电动按摩棒按压在'+pn+yinbu(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'正在用电动按摩棒玩弄着'+pn+yinhe(p))
            pt()
        elif comfail(inf):
            push_text(pn+'用手紧捂着'+yinbu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'收起了电动按摩棒')
            pt()
    
    #按摩棒
    elif com == 25:
        if comadd(inf):
            push_text(atn+'把形状凶恶的按摩棒深深地插入'+pn+yindao(p))
            pt()
        elif comdoing(inf):
            push_text(pn+duzi(p)+'隐约凸显出了按摩棒的形状，'+yindao(p)+'里按摩棒正扭动地变化形状')
            pt()
        elif comfail(inf):
            push_text(pn+'死盯着按摩棒，用手紧捂着'+yinbu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+yindao(p)+'深处抽出按摩棒，拉出了几道淫靡的银丝')
            pt()
    
    #肛用按摩棒
    elif com == 26:
        if comadd(inf):
            push_text(atn+'把形状凶恶的肛用按摩棒深深地插入'+pn+pigu(p))
            pt()
        elif comdoing(inf):
            push_text(pn+gangmen(p)+'里按摩棒正扭动地变化形状刺激着'+changdao(p))
            pt()
        elif comfail(inf):
            push_text(pn+'死盯着按摩棒，用手紧捂着'+pigu(p),{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从'+pn+gangmen(p)+'深处抽出肛用按摩棒，拉出了几道淫靡的银丝')
            pt()
    
    #阴蒂夹
    elif com == 27:
        if comadd(inf):
            push_text(atn+'把挂着跳蛋的夹子夹在了'+pn+'的'+yinhe(p)+'上')
            pt()
        elif comdoing(inf):
            push_text('嗡嗡作响的夹子正拉扯着'+pn+'的'+yinhe(p))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝戴上阴蒂夹',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'把阴蒂夹从'+pn+'的'+yinhe(p)+'取下')
            pt()
    
    #乳头夹
    elif com == 28:
        if comadd(inf):
            push_text(atn+'把挂着跳蛋的夹子夹在了'+pn+'的'+xiong(p)+'上')
            pt()
        elif comdoing(inf):
            push_text('嗡嗡作响的夹子正拉扯着'+pn+'的'+xiong(p))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝戴上乳头夹',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'把乳头夹从'+pn+'的'+xiong(p)+'取下')
            pt()
    
    #飞机杯
    elif com == 29:
        if comadd(inf):
            push_text(atn+'用紧致柔软的飞机杯吞吃了'+pn+'的'+yinjing(p))
            pt()
        elif comdoing(inf):
            push_text(atn+'正用飞机杯咕叽咕叽地榨取着'+pn)
            pt()
        elif comfail(inf):
            push_text(pn+'打掉了飞机杯',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text('\"噗呲\"地一声，'+atn+'分离了飞机杯与'+pn+'的'+yinjing(p))
            pt()
    
    #榨乳机
    elif com == 30:
        if comadd(inf):
            push_text(atn+'将榨乳器吸附在'+pn+'的'+xiong(p)+'上')
            pt()
        elif comdoing(inf):
            push_text('榨乳器轰鸣着榨取着'+pn+'的'+xiong(p))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝被榨乳',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'关上了榨乳机，\"噗呲\"地拿掉了榨乳器')
            pt()
    
    #绳缚
    elif com == 31:
        bound_type = p['标志']['受缚类型']
        if comadd(inf):
            if bound_type == 1:
                push_text(atn+'将'+pn+'的手腕和脚腕像带上镣铐般绑到一起')
            elif bound_type == 2:
                push_text(atn+'用龟甲缚将'+pn+'的双手绑到背后')
            elif bound_type == 3:
                push_text(atn+'将'+pn+'的四肢分别绑住四个床脚处,'+pn+'大字形地躺着任由摆布')
            elif bound_type == 4:
                push_text(atn+'将'+pn+'的四肢分别绑住四个床脚处,'+pn+'大字形地趴着任由摆布')
            elif bound_type == 5:
                push_text(atn+'从天花板上挂下绳子和镣铐，将'+pn+'的四肢像待宰的牲畜般吊起')
            elif bound_type == 6:
                push_text(atn+'把'+pn+'的双手绑缚，一只脚高高吊起，直到另一只脚勉强能触地')
            pt()

        elif comdoing(inf):
            if bound_type == 1:
                push_text(pn+'的手腕和脚腕像带上镣铐般绑到一起')
            elif bound_type == 2:
                push_text(pn+'被用龟甲缚束缚着')
            elif bound_type == 3:
                push_text(pn+'的四肢分别绑在四个床脚处,'+pn+'大字形地躺着任由摆布')
            elif bound_type == 4:
                push_text(pn+'的四肢分别绑在四个床脚处,'+pn+'大字形地趴着任由摆布')
            elif bound_type == 5:
                push_text(pn+'的四肢像待宰的牲畜般吊起')
            elif bound_type == 6:
                push_text(pn+'努力用单脚站立着，'+yinbu(p)+'正毫无遮掩地展示在外')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝被绑缚',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'给'+pn+'解开了绳子')
            pt()
    
    #口枷
    elif com == 32:
        if comadd(inf):
            push_text(atn+'给'+pn+'带上了口枷')
            pt()
        elif comdoing(inf):
            push_text('戴上了口枷的'+pn+'只能发出一些含糊不清的声音')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了口枷',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'取下了口枷')
            pt()
    
    #眼罩
    elif com == 33:
        if comadd(inf):
            push_text(atn+'给'+pn+'带上了眼罩')
            pt()
        elif comdoing(inf):
            push_text(pn+'被眼罩剥夺了视觉')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了眼罩',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'为'+pn+'取下了眼罩')
            pt()
    
    #导尿管
    elif com == 34:
        if comadd(inf):
            push_text(atn+'将导尿管插进了'+pn+'的尿道')
            pt()
        elif comdoing(inf):
            push_text(pn+'的尿道插着导尿管')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了导尿管',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'为'+pn+'取下了导尿管')
            pt()
    
    #肛门拉珠
    elif com == 35:
        if comadd(inf):
            push_text(atn+'一颗一颗地把硕大的肛门拉珠塞进了'+pn+'的'+gangmen(p))
            pt()
        elif comdoing(inf):
            push_text(pn+'的'+pigu(p)+'里垂下了一小节肛门拉珠')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝被塞进肛门拉珠',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'按住'+pn+'的'+pigu(p)+',扣住拉珠的拉环，随后一口气从'+changdao(p)+'里拔出了所有的肛门拉珠。拉珠上挂满了黏滑的肠液')
            pt()
    
    #A扩张气囊
    elif com == 36:
        if comadd(inf):
            push_text(atn+'把扩张气囊塞进了'+pn+'的'+gangmen(p))
            pt()
        elif comdoing(inf):
            push_text('扩张气囊的输气管从'+pn+'的'+pigu(p)+'垂下,'+pn+'的'+duzi(p)+'由于扩张气囊的缘故像孕妇一样高高隆起')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝被塞进肛门扩张气囊',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'按住'+pn+'的'+pigu(p)+',拔出了扩张气囊。被扩张开发而难以闭合的肛门像是大口喘气一般敞开蠕动着。')
            pt()
    
    #V扩张气囊
    elif com == 37:
        if comadd(inf):
            push_text(atn+'把扩张气囊塞进了'+pn+'的'+yindao(p))
            pt()
        elif comdoing(inf):
            push_text('扩张气囊的输气管从'+pn+'的'+yinbu(p)+'垂下,'+pn+'的'+duzi(p)+'由于扩张气囊的缘故像孕妇一样高高隆起')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝被塞进阴道扩张气囊',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'按住'+pn+'的'+yinbu(p)+',拔出了扩张气囊。被扩张开发而难以闭合的腔穴像是大口喘气一般敞开蠕动着。')
            pt()
    
    #正常位
    elif com == 50:
        if comadd(inf):
            push_text(atn+'将自己'+yinjing(at)+'对准'+pn+'的'+yinbu(p)+',随即将其插入了'+yindao(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'甩动着腰部，'+yinjing(at)+'抽插着'+pn+'的'+yinbu(p)+',发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'握住'+pn+'的'+duzi(p)+'两侧,拔出了'+yinjing(at))
            pt()
    
    #后背位
    elif com == 51:
        if comadd(inf):
            push_text(atn+'将自己'+yinjing(at)+'对准'+pn+'高高抬起的'+yinbu(p)+',随即将其插入了'+yindao(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'抓住高抬的屁股，甩动着腰部，'+yinjing(at)+'抽插着'+pn+'的'+yinbu(p)+',发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'握住'+pn+'的'+pigu(p)+'两侧,拔出了'+yinjing(at))
            pt()
    
    #屈居位
    elif com == 52:
        if comadd(inf):
            push_text(atn+'将'+pn+'的双腿扛到肩膀上，自己'+yinjing(at)+'对准'+pn+'垂直的'+yinbu(p)+',随即将其插入了'+yindao(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'以打桩的气势挥动着腰部，'+yinjing(at)+'冲击着'+pn+'的'+yinbu(p)+',发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'缓缓起身,拔出了'+yinjing(at))
            pt()
    
    #对面座位
    elif com == 53:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上，将'+yinjing(at)+'对准'+pn+'的'+yinbu(p)+'后,随抓住腰部即将其压入了'+yindao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'双手抓住'+pn+'的'+pigu(p)+',时而扭腰时而抽插地享用'+pn+'的'+yinbu(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #背面座位
    elif com == 54:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上坐下，将'+yinjing(at)+'对准'+pn+'的'+yinbu(p)+'后,随即抓住腰侧和大腿根部即将其压入了'+yindao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'抱住'+pn+',双手分别揉捏着'+xiong(p)+'和'+yinhe(p)+',时而扭腰时而抽插地享用'+pn+'的'+yinbu(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #骑乘位
    elif com == 55:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上，将'+yinjing(at)+'对准'+pn+'的'+yinbu(p)+'后,随即抓住腰侧和大腿根部即将其压入了'+yindao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'命令'+pn+'时而扭腰抽插时而套弄榨取着服侍自己肚内的'+yinjing(at))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #肛交正常位
    elif com == 56:
        if comadd(inf):
            push_text(atn+'将自己'+yinjing(at)+'对准'+pn+'的'+pigu(p)+',随即将其插入了'+gangmen(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'甩动着腰部，'+yinjing(at)+'抽插着'+pn+'的'+gangmen(p)+',发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'握住'+pn+'的'+duzi(p)+'两侧,拔出了'+yinjing(at))
            pt()
    
    #肛交后背位
    elif com == 57:
        if comadd(inf):
            push_text(atn+'将自己'+yinjing(at)+'对准'+pn+'高高抬起的'+pigu(p)+',随即将其插入了'+gangmen(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'抓住高抬的屁股和腰侧，甩动着'+yinjing(at)+'抽插着'+pn+'的'+pigu(p)+',发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'掰开'+pn+'的'+pigu(p)+',从'+changdao(p)+'深处拔出了'+yinjing(at))
            pt()
    
     #肛交屈居位
    elif com == 58:
        if comadd(inf):
            push_text(atn+'将'+pn+'的双腿扛到肩膀上，把自己'+yinjing(at)+'对准'+pn+'垂直的'+pigu(p)+',随即将其插入了'+gangmen(p)+'中')
            pt()
        elif comdoing(inf):
            push_text(atn+'以打桩的气势挥动着腰部，'+yinjing(at)+'冲击着'+pn+'的'+changdao(p)+'深处,发出啪啪的响声')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'缓缓起身,拔出了'+yinjing(at))
            pt()
    
    #肛交对面座位
    elif com == 59:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上坐下，将'+yinjing(at)+'对准'+pn+'的'+gangmen(p)+'后,随即抓住腰侧和大腿根部即将其压入了'+changdao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'双手抓住'+pn+'的'+pigu(p)+',时而扭腰时而抽插地享用'+pn+'的'+gangmen(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #肛交背面座位
    elif com == 60:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上坐下，将'+yinjing(at)+'对准'+pn+'的'+gangmen(p)+'后,随即抓住腰侧和大腿根部即将其压入了'+changdao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'抱住'+pn+',双手分别揉捏着'+xiong(p)+'和'+yinhe(p)+',时而扭腰时而抽插地享用'+pn+'的'+gangmen(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #肛交骑乘位
    elif com == 61:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱到自己身上，将'+yinjing(at)+'对准'+pn+'的'+gangmen(p)+'后,随即抓住腰侧和大腿根部即将其压入了'+changdao(p)+'深处')
            pt()
        elif comdoing(inf):
            push_text(atn+'命令'+pn+'时而扭腰抽插时而套弄榨取着服侍自己肠内的'+yinjing(p))
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'抱起'+pn+',拔出了自己'+yinjing(at))
            pt()
    
    #刺激G点
    elif com == 62:
        if comadd(inf):
            push_text(atn+'在抽插时开始尝试寻找'+pn+'的G点')
            pt()
        elif comdoing(inf):
            push_text(atn+'持续地刺激'+pn+'的G点')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'停止刺激G点')
            pt()
    
    #进攻子宫口
    elif com == 63:
        if comadd(inf):
            push_text(atn+'在每次抽插时深深地刺入'+pn+yinbu(p)+'，努力撞击着'+pn+'的子宫口')
            pt()
        elif comdoing(inf):
            push_text(atn+'持续地玩弄'+pn+'的子宫口')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'停止进攻子宫口')
            pt()
    
    #子宫插入
    elif com == 64:
        if comadd(inf):
            push_text(atn+'猛地一挺腰，贯穿了'+pn+'的子宫口')
            pt()
        elif comdoing(inf):
            push_text(atn+'享用着'+pn+'的子宫淫肉')
            pt()
        elif comfail(inf):
            push_text(pn+'推开了'+atn,{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'从子宫中拔出龟头，隐约听到'+pn+'的'+duzi(p)+'中传来\'噗\'的微响')
            pt()
        
    #手交
    elif com == 65:
        if comadd(inf):
            push_text(atn+'命令'+pn+'用手服侍自己的'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(atn+'享用着'+pn+'手交')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止手交')
            pt()
    
    #口交
    elif com == 66:
        if comadd(inf):
            push_text(atn+'命令'+pn+'用嘴服侍自己的'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(atn+'享用着'+pn+'口交')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止口交')
            pt()
    
    #乳交
    elif com == 67:
        if comadd(inf):
            push_text(atn+'要求'+pn+'用'+xiong(p)+'服侍自己的'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(atn+'享用着'+pn+xiong(p))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止乳交')
            pt()
    
    #乳交
    elif com == 67:
        if comadd(inf):
            push_text(atn+'要求'+pn+'用'+xiong(p)+'服侍自己的'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(atn+'享用着'+pn+xiong(p))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止乳交')
            pt()

    #乳夹口交
    elif com == 68:
        if comadd(inf):
            push_text(atn+'让'+pn+'用'+xiong(p)+'服侍自己的'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(atn+'的'+yinjing(at)+'被包裹在'+xiong(p)+'中,'+pn+'正用嘴舔舐着自乳沟中露出的龟头')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'命令'+pn+'停止乳夹口交')
            pt()
    
    #六九式
    elif com == 69:
        if comadd(inf):
            push_text(atn+'让'+pn+'倒过来躺在自己身上')
            pt()
        elif comdoing(inf):
            push_text(atn+'和'+pn+'互相舔舐对方的性器')
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'让'+pn+'停止六九式')
            pt()
    
    #素股
    elif com == 70:
        if comadd(inf):
            push_text(atn+'把'+pn+'抱过来坐在自己的'+yinjing(at)+'上')
            pt()
        elif comdoing(inf):
            push_text(atn+'正让'+pn+'用'+yinbu(p)+'摩擦'+yinjing(at))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'让'+pn+'停止素股')
            pt()
    
    #足交
    elif com == 71:
        if comadd(inf):
            push_text(atn+'要求'+pn+'用足来榨取'+yinjing(at))
            pt()
        elif comdoing(inf):
            push_text(pn+'正用双脚'+yinbu(p)+'摩擦着'+yinjing(at))
            pt()
        elif comfail(inf):
            push_text(pn+'拒绝了'+atn+'命令',{'color':'#f00'})
            pt()
        elif comundo(inf):
            push_text(atn+'让'+pn+'停止足交')
            pt()
    
    #润滑油
    elif com == 100:
        if comadd(inf):
            push_text(atn+'拧开一瓶润滑油，将其倒在'+pn+'的'+shenti(p)+'上')
            pt()
        elif comdoing(inf):
            pass
        elif comfail(inf):
            pass
        elif comundo(inf):
            pass
    
    #媚药
    elif com == 101:
        if comadd(inf):
            push_text(atn+'打开一瓶媚药，将其灌入'+pn+'的口内')
            pt()
        elif comdoing(inf):
            pass
        elif comfail(inf):
            pass
        elif comundo(inf):
            pass
    
    #注射药液
    elif com == 102:
        if comadd(inf):
            push_text(atn+'取出一支装满淫药的注射器，将其全部打进了'+pn+'的'+shenti(p)+'里')
            pt()
        elif comdoing(inf):
            pass
        elif comfail(inf):
            pass
        elif comundo(inf):
            pass

def get_attenders(at):
    if isinstance(at,list):
        return True
    else:
        return False
