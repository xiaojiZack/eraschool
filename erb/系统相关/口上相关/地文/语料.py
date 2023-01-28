from random import random
import erajs.api as a
import random

def c(l):
    if l != []:
        return random.choice(l)
    else:
        return None

def search_quaility(c,target):
    for i in c['属性']:
        for j in c['属性'][i]:
            if j == target:
                return True
    return False

def addlist(l,nw):
    for i in nw:
        l.append(i)

def toufa(p):
    #word为名词，describe为形容词
    words = []
    describe = ['']
    words.append('头发')
    w = c(words)
    d = c(describe)
    return d+w

def lian(p):
    words = ['脸蛋','面部']
    describe = ['']
    w = c(words)
    d = c(describe)
    return d+w

def xiong(p):
    words = ['胸部','乳房']
    describe = ['']
    if search_quaility(p,'贫乳'):
        addlist(describe,['贫瘠的','平坦的','光滑的'])
    elif search_quaility(p,'美乳'):
        addlist(describe,['微隆的','小巧的','可以一手掌握的'])
    elif search_quaility(p,'巨乳'):
        addlist(describe,['巨大的','丰满的','诱人的'])
    elif search_quaility(p,'超乳'):
        addlist(describe,['硕大的','膨大的','沉重的','木瓜大小的'])
    elif search_quaility(p,'魔乳'):
        addlist(describe,['极大的','几乎触地的'])
    w = c(words)
    d = c(describe)
    return d+w

def shou(p):
    words = ['手']
    describe = ['']
    w = c(words)
    d = c(describe)
    return d+w

def yinjing(p):
    if p['性别'] != '女性':
        words = ['阴茎','鸡鸡','肉棒']
        describe = ['']
        if search_quaility(p,'迷你根'):
            addlist(describe,['极小的','迷你尺寸的','小指节大小的'])
        elif search_quaility(p,'小根'):
            addlist(describe,['稍小的','尺寸温柔的','小小的','可爱的'])
        elif search_quaility(p,'普通根'):
            addlist(describe,['完美的','平均尺寸的'])
        elif search_quaility(p,'巨根'):
            addlist(describe,['大于一般尺寸的','巨大的','粗大的','大'])
        elif search_quaility(p,'马根'):
            addlist(describe,['手臂粗的','凶恶的','爆筋的','又粗又长的','马'])
        elif search_quaility(p,'龙根'):
            addlist(describe,['尺寸极其夸张的','如女性腰粗的','不可思议的'])
    #脏污
    #穿环
    w = c(words)
    d = c(describe)
    return d+w

#TODO 描述较少
def yinhe(p):
    words = ['阴核']
    describe = ['','']
    
    w = c(words)
    d = c(describe)
    return d+w

#阴部和阴道的区别在于一个是注重描述外部，一个则是注重描述内部
def yinbu(p):
    words = ['阴部','蜜壶','花蕊','私处','温柔乡','女阴']
    describe = ['']
    if search_quaility(p,'白虎'):
        addlist(describe,['光滑的','美丽的'])
        addlist(words, ['一线天','馒头穴'])
    if search_quaility(p,'处女'):
        describe = ['尚未开封的','未尝过男人滋味的','纯洁的']
        addlist(words, ['处女穴'])
    if search_quaility(p,'小只') or search_quaility(p,'小孩体型'):
        addlist(describe,['幼小的','小小的','稚嫩的'])
        addlist(words, ['幼女穴'])
    #脏污
    #穿环
    #漏精
    #纹身
    w = c(words)
    d = c(describe)
    return d+w

def yindao(p):
    words = ['阴道','肉腔','肉壶','肉穴']
    describe = ['','','正在蠕动的']
    
    w = c(words)
    d = c(describe)
    return d+w

#肠道注重描述内部
def changdao(P):
    words = ['肠道','屁穴','肠穴']
    describe = ['','','正在蠕动的']
    
    w = c(words)
    d = c(describe)
    return d+w

def duzi(p):
    words = ['肚子','下腹']
    describe = ['紧致的','柔软的','']
    if search_quaility(p,'妊娠'):
        describe = ['怀有身孕的','鼓鼓的','孕育着生命的','被种付的','怀孕的','']
        addlist(words,['孕肚','孕袋'])
        if search_quaility(p,'临盆'):
            addlist(describe,['临盆的','临产的','圆滚的'])
    if search_quaility(p,'寄生') or search_quaility(p,'怀卵'):
        addlist(describe,['被种下异物的','鼓鼓的','有东西在里面蠕动的',''])
        addlist(words,['苗床','孕袋'])
    if search_quaility(p,'乌贼肚'):
        addlist(describe,['肉肉的','有着完美弧线的'])
    #装满液体
    #脏污
    #淫纹
    #涂鸦
    w = c(words)
    d = c(describe)
    return d+w

def pigu(p):
    words = ['屁股','肉臀']
    describe = ['','']
    if search_quaility(p,'小尻'):
        addlist(describe,['瘦小的','小小的'])
    elif search_quaility(p,'美尻'):
        addlist(describe,['匀称的','可爱的','完美的'])
    elif search_quaility(p,'桃尻'):
        addlist(describe,['硕大的','多肉的'])
    elif search_quaility(p,'巨尻'):
        addlist(describe,['大于一般尺寸的','巨大的','硕大的'])
    #涂鸦
    w = c(words)
    d = c(describe)
    return d+w

def niaodao(P):
    words = ['尿道']
    describe = ['','']
    
    w = c(words)
    d = c(describe)
    return d+w

#TODO 描述较少
def gangmen(p):
    words = ['肛门','菊穴','后穴']
    describe = ['','']
    
    w = c(words)
    d = c(describe)
    return d+w

def shenti(p):
    words = ['身体','胴体']
    describe = ['','']
    if search_quaility(p,'高大'):
        addlist(describe,['高大的'])
    elif search_quaility(p,'小只'):
        addlist(describe,['萝莉体型的','可爱的'])
    elif search_quaility(p,'小孩体型'):
        addlist(describe,['小学生般的','幼小的'])
    elif search_quaility(p,'幼儿体型'):
        addlist(describe,['幼儿般','婴儿般',''])
    #涂鸦
    w = c(words)
    d = c(describe)
    return d+w