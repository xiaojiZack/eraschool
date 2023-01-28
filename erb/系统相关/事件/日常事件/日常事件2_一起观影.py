import erajs.api as a
from erb.系统相关.调教相关.memory_cal import memory_cal
from erb.系统相关.调教相关.液体 import eject_liquid, inject_liquid
from funcs import get_leading_character, get_student_list
from random import choice

def try_trigger2(c):
    flag = True
    #好感度>100
    if c['好感度']<800:
        flag = False
    if c['刻印']['反发刻印']>0:
        flag = False
    if '狂乱' in c['属性']['个性'] or '崩坏' in c['属性']['个性']:
        flag = False
    return flag

def check_building():
    f = False
    for building in a.sav()['校内建筑列表']:
        if '影视厅' == building['名称']:
            f = True
    return f

def try_event2():
    if check_building() == False:
        return False
    student_list = get_student_list()
    can_trigger_students = []
    for student_id in student_list:
        student = student_list[student_id]
        if try_trigger2(student):
            can_trigger_students.append(student_id)
    if can_trigger_students == []:
        return False
    else:
        student_id = choice(can_trigger_students)
        student = student_list[student_id]
        performance2(student)
        return True

def what_movie(c):
    #判断是什么类型的电影和事件
    movie = "正常观影"
    if c['开发']['欲望'] >=4 and c['开发']['露出癖'] >=2:
        #色色事件
        if c['开发']['M感觉'] >= 2 and (c['开发']['精液成瘾']>=2 or c['开发']['侍奉欲望']>=3):
            movie = "偷偷口交"
        if c['开发']['M感觉'] >= 3 and (c['开发']['精液成瘾']>=3 or c['开发']['侍奉欲望']>=4):
            movie = "全程口交"
        if (c['开发']['V感觉'] >= 3 or c['开发']['A感觉'] >= 3) and c['开发']['精液成瘾']>=3:
            movie = "偷偷性交"
        if (c['开发']['V感觉'] >= 4 or c['开发']['A感觉'] >= 4) and (c['开发']['精液成瘾']>=3 or c['开发']['露出癖'] >=3):
            movie = "全程性交"
    else:
        if (c['好感度']>1000): movie = "爱情影片"
        if (c['开发']['欲望']>2): movie = "黄片"
    return movie

def performance2(c):
    movie = what_movie(c)
    if '臆病' in c['属性']['个性'] or '自卑' in c['属性']['个性']:
        a.t('{}低着头，双手交叉地来到你面前，扭捏的问你有没有兴趣一起去看电影。'.format(c['名字']))
        a.t('想着是对方鼓起勇气的请求就同意了。',wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('两人好好地欣赏了电影。')
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}似乎被影片的内容深深打动了。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('{}全程都捂着眼睛--或者说假装捂着眼睛。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}像是终于下定决心一般,一边偷瞄你的反应一边一点点拉开了你的裤子,确认没人注意之后俯下了身子。'.format(c['名字']),wait=True)
            a.t('你舒服地享用了{}的口交。'.format(c['名字']),wait=True)
            a.t('事后{}像是谢罪一般一个劲的道歉。'.format(c['名字']),wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后呼吸声一直很重。'.format(c['名字']))
            a.t('电影开始以后担心的询问身体状况，却被对方贴着耳朵小声恳求给予肉棒。'.format(c['名字']),wait=True)
            a.t('总之是一边全程享受着{}跪在股间的服务一边品鉴了一部好电影。'.format(c['名字']),wait=True)
            a.t('即使是等到灯打开的时候{}还在沉迷于饮用精液。'.format(c['名字']),wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}的呼吸声有点重。'.format(c['名字']))
            a.t('结果在电影到一半的时候被支支吾吾地哭着请求陪同去厕所。',wait=True)
            a.t('怀着担心的心情就答应了请求。走到一半的时候{}却开始一直道歉，大概搞明白了意思，其实是想要的不得了。'.format(c['名字']),wait=True)
            a.t('痛快地做了一次以后俩人偷偷溜回了影视厅。',wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后突然小声恳求坐在你身上。'.format(c['名字']))
            a.t('出于好奇心答应了下来之后。{}露出如蒙大赦的表情一边小心翼翼地解开了你的裤子坐在了你的肉棒上。'.format(c['名字']),wait=True)
            a.t('{}像是一个大型抱枕被你抱住，慢慢地扭腰或者上下抽插着。电影的声音里开始混杂着淫乱的娇喘和水声。')
            a.t('除了完全没有享受到影片这一点之外，你充分地享用了{}'.format(c['名字']))
            
    elif '反抗' in c['属性']['个性'] or '高傲' in c['属性']['个性']:
        a.t('{}今天傲慢地要求你陪同去看电影。'.format(c['名字']))
        a.t('看着对方盛气凌人的样子总之还是同意了。',wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('两人好好地欣赏了电影。')
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}似乎被影片的内容深深打动了。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('{}全程红着脸硬着头皮看完了。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}开始眺望四周，确认没人注意之后傲慢地要求你取出肉棒。'.format(c['名字']),wait=True)
            a.t('之后{}便俯下身子后开始用嘴熟练的榨取精液。'.format(c['名字']))
            a.t('事后{}擦了擦嘴就坐回去了，甚至没帮你把裤子拉回去。'.format(c['名字']),wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后呼吸声一直很重。'.format(c['名字']))
            a.t('电影开始以后担心的询问身体状况，却被对方一把拉下裤子。'.format(c['名字']))
            a.t('总之是一边全程忍受着{}跪在股间的榨取一边品鉴了一部好电影。'.format(c['名字']),wait=True)
            a.t('即使是等到灯打开的时候{}还在沉迷于饮用精液。'.format(c['名字']),wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}的呼吸声有点重。'.format(c['名字']))
            a.t('结果在电影到一半的时候被拽着起来去了外边。',wait=True)
            a.t('走到一半的时候{}却拐进了一个小道，回头气势凌人地要求脱下衣服。'.format(c['名字']),wait=True)
            a.t('总之痛快地做了一次以后俩人偷偷溜回了影视厅。'.format(c['名字']),wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后直接坐在了你身上。'.format(c['名字']))
            a.t('一把把你的肉棒吞进肉穴中后，{}像是自慰一般自顾自地扭动腰肢榨取肉棒。'.format(c['名字']),wait=True)
            a.t('不仅完全没有好好看电影，还被{}当作自慰工具使用了。'.format(c['名字']))
    elif '无节操' in c['属性']['个性'] or '坦率' in c['属性']['个性']:
        a.t('{}今天高兴地举着两张票，问你有没有心情一块去看电影。'.format(c['名字']))
        a.t('看着对方高兴的样子同意了请求。',wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('两人好好地欣赏了电影。')
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}似乎被影片的内容深深打动了。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('{}不好意思地道歉后两人看完了全程。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}开始眺望四周，确认没人注意之后请求你取出肉棒。'.format(c['名字']),wait=True)
            a.t('之后{}便俯下身子后开始用嘴熟练的榨取精液。'.format(c['名字']))
            a.t('事后{}擦了擦嘴表达了感谢。'.format(c['名字']),wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后呼吸声一直很重。'.format(c['名字']))
            a.t('电影开始以后担心的询问身体状况，却被对方坦诚地请求给予肉棒。',wait=True)
            a.t('总之是一边全程享受着{}的口穴一边品鉴了一部好电影。'.format(c['名字']),wait=True)
            a.t('之后{}顶着一副被充分使用的肉便器的表情一边感谢了肉棒。'.format(c['名字']),wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}的呼吸声有点重。'.format(c['名字']))
            a.t('结果在电影到一半的时候被直接请求去来一发。',wait=True)
            a.t('按照{}的想法中出了一次后总算是平息了饥渴。'.format(c['名字']),wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后坦率地问道能不能坐在了你身上。'.format(c['名字']))
            a.t('同意了之后便把你的肉棒吞进肉穴中，{}一边发出娇喘一边开玩笑表示影视厅的坐垫真不错。'.format(c['名字']),wait=True)
            a.t('你在中出几次把{}弄得一团糟后完全没能好好看完电影。'.format(c['名字']))
    elif '孩子气' in c['属性']['个性'] or '傲娇' in c['属性']['个性']:
        a.t('{}今天举着两张票，“本小姐大发慈悲”地命令你陪同去看电影。'.format(c['名字']))
        a.t('看着对方闪烁着期待的眼神想了想还是同意了请求。',wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('两人好好地欣赏了电影。')
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}似乎被影片的内容深深打动了。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('{}露出一副尴尬到不行的表情，最后还是红着脸颤抖着看完了影片。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}开始眺望四周，确认没人注意之后一副"你就高兴吧"的表情一边拉开了你裤子的拉链。'.format(c['名字']),wait=True)
            a.t('之后{}便俯下身子后开始用嘴熟练的榨取精液。'.format(c['名字']))
            a.t('事后{}也一直在说什么“才不是为了你”之类的话。'.format(c['名字']),wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后呼吸声一直很重。'.format(c['名字']))
            a.t('电影开始以后担心的询问身体状况，一番扭扭捏捏的对话后对方终于一副绷不住的样子小声求你脱下裤子。'.format(c['名字']),wait=True)
            a.t('{}将肉棒吞入口中以后就乖多了。'.format(c['名字']),wait=True)
            a.t('电影结束以后{}还在含着肉棒迷迷糊糊地说着什么。'.format(c['名字']),wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}心跳的很快。'.format(c['名字']))
            a.t('在电影放到一半的时候{}拉着你出了门。一边说着‘看你憋得那么难受’之类的话一边伸手解开你的裤子。',wait=True)
            a.t('总之痛快地做了一次以后俩人偷偷溜回了影视厅。',wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后就坐在了你的身上，‘才不是很想和你做呢’这样说着红着脸把你的肉棒吞进身体里。'.format(c['名字']))
            a.t('实际上在中出过一次以后{}就变得安静下来了，只有偶尔能听到努力压抑的呻吟声。'.format(c['名字']),wait=True)
            a.t('之后谈到的时候{}一直红着脸拼命否定着。'.format(c['名字']))
    #elif '顺从' in c['属性']['个性'] or '无节操' in c['属性']['个性']: 
    elif '好色' in c['属性']['个性'] or '小恶魔' in c['属性']['个性']:
        a.t('{}今天拿着两张票抓着你的胳膊问你想不想去看电影。'.format(c['名字']))
        a.t('{}有意无意地夹杂着黄色笑话挑逗着让你同意了请求。'.format(c['名字']),wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('{}似乎一副因为没有被你乘机袭击而感到遗憾的样子。'.format(c['名字']))
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}因为没有关键的床戏而大发不满。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('出来后{}津津有味地跟你交流感想。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}一副无聊至极的表情，随后顺手拉开了你裤子的拉链。'.format(c['名字']),wait=True)
            a.t('片刻后在电影里开始混入吸吮肉棒和吞咽精液的响动。')
            a.t('做了一次以后{}狡黠地露出了一副‘多谢款待’的表情。'.format(c['名字']),wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后就一直有意无意地触摸你的下体。'.format(c['名字']))
            a.t('电影开始后{}终于忍不住开始把头埋在你的股间。'.format(c['名字']),wait=True)
            a.t('你在观影全程享受着升天般的服侍，{}也因为被当成精液便池欢喜的不行。'.format(c['名字']),wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}的脸有些微红，而且从刚才开始就一直在做故意向耳朵吹气、抱着手臂撒娇这些诱惑的行动。'.format(c['名字']))
            a.t('果然在电影放到一半的时候{}拉着你出了门。找了个角落后一边轻咬你的耳朵一边从你的裤子中取出阳物。'.format(c['名字']),wait=True)
            a.t('按照{}的心意狠狠中出以后两人偷偷回到了座位上。'.format(c['名字']),wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后就坐在了你的身上，把你的肉棒吞进体内。'.format(c['名字']))
            a.t('比起精彩的电影桥段，{}显然更加中意肉棒在体内的触感。'.format(c['名字']))
            a.t('在电影结束的时候{}已经因为被不停中出几个小时弄得有些神志不清了。'.format(c['名字']),wait=True)
    else:
        a.t('{}今天拿着两张票问你想不想去看电影。'.format(c['名字']))
        a.t('想着没什么要忙的，你同意了请求。',wait=True)
        a.t()
        if movie == '正常观影':
            a.t('来到电影院后发现今天上映的是一部{}。'.format(choice(['科幻片','人文片','纪录片','动作片'])))
            a.t('两人好好地欣赏了电影。')
        if movie == '爱情影片':
            a.t('来到电影院后发现今天上映的是一部爱情片。')
            a.t('{}似乎被影片的内容深深打动了。'.format(c['名字']))
        if movie == '黄片':
            a.t('来到电影院后才发现今天上映的是一部AV。')
            a.t('{}红着脸看完了影片。'.format(c['名字']))
        if movie == '偷偷口交':
            a.t('{}今天一副心神不宁的样子，眼睛一直不在影片上，而是不时瞟着你的股间。'.format(c['名字']))
            a.t('影片播到一半的时候{}开始眺望四周，确认没人注意之后拉开了你裤子的拉链。'.format(c['名字']),wait=True)
            a.t('之后{}便俯下身子后开始用嘴熟练的服侍肉棒。'.format(c['名字']))
            a.t('在嘴里中出了一次以后似乎清爽了很多。',wait=True)
        if movie == '全程口交':
            a.t('总感觉{}在进入影视厅后呼吸声一直很重。'.format(c['名字']))
            a.t('电影开始以后担心的询问身体状况，对方小声地提出了想口交的请求。'.format(c['名字']),wait=True)
            a.t('同意后{}就拉开了你的裤子，跪下将头埋在你的股间。'.format(c['名字']),wait=True)
            a.t('结果似乎沉迷于口交直到电影放完了还不肯松嘴。',wait=True)
        if movie == '偷偷性交':
            a.t('总感觉{}在呼吸声有点重。'.format(c['名字']))
            a.t('在电影放到一半的时候{}拉着你出了门。带着你躲到一个阴暗处后就急急忙忙地解开了你的裤子。',wait=True)
            a.t('总之痛快地做了一次以后俩人偷偷溜回了影视厅。',wait=True)
        if movie == '全程性交':
            a.t('{}在电影开始后就坐在了你的身上把你的肉棒吞进身体里。'.format(c['名字']))
            a.t('无意识着扭着腰呻吟的{}感受着肚内的阳物，似乎完全无法专心观影。'.format(c['名字']),wait=True)
            a.t('电影结束时，{}靠在你身上抚摸着装满精种的肚子露出了一脸幸福的表情。'.format(c['名字']),wait=True)
    
    m = c['待处理记忆']
    e = c['待处理经验']
    if movie == '正常观影':
        m['羞耻'] += 1000
        m['好感度'] += 50
    if movie == '爱情影片':
        m['好感度'] += 100
        m['恭顺'] += 3000
        m['欲情'] += 2000
        m['羞耻'] += 2000
    if movie == '黄片':
        m['好感度'] += 75
        m['恭顺'] += 1000
        m['欲情'] += 5000
        m['羞耻'] += 3000
    if movie == '偷偷口交':
        m['好感度'] += 100
        m['侍奉快乐'] += 10
        m['恭顺'] += 3000
        m['屈服'] += 3000
        m['欲情'] += 3000
        m['羞耻'] += 4000
        count = 1+c['开发']['喉名器度']*c['开发']['舌技']
        e['饮精经验'] += count
        e['精液经验'] += count
        a.t('在{}口中射精了{}次。'.format(c['名字'],count))
        e['口交经验'] += 1
        e['舌技经验'] += 1
        e['露出经验'] += 5
        e['侍奉经验'] += 1
        liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
        inject_liquid(c,'口',liquid_list)
    if movie == '全程口交':
        m['好感度'] += 400
        m['侍奉快乐'] += 50
        m['恭顺'] += 10000
        m['屈服'] += 10000
        m['欲情'] += 10000
        m['羞耻'] += 10000
        count = 5*(1+c['开发']['喉名器度']*c['开发']['舌技'])
        e['饮精经验'] += count
        e['精液经验'] += count
        a.t('在{}口中射精了{}次。'.format(c['名字'],count))
        e['口交经验'] += 10
        e['舌技经验'] += 10
        e['露出经验'] += 25
        e['侍奉经验'] += 10
        liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
        inject_liquid(c,'口',liquid_list)
    if movie == '偷偷性交':
        m['好感度'] += 200
        m['侍奉快乐'] += 20
        m['恭顺'] += 4000
        m['屈服'] += 4000
        m['欲情'] += 4000
        m['羞耻'] += 5000
        e['露出经验'] += 10
        e['侍奉经验'] += 1
        if c['经验']['V经验']>0 and not c['性别'] == '女性':
            count = 1+c['开发']['V名器度']*c['开发']['腰技']
            e['腔射经验'] += count
            e['精液经验'] += count
            a.t('在{}的腔内射精了{}次'.format(c['名字'],count))
            liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
            inject_liquid(c,'阴道',liquid_list)
        else:
            count = 1+c['开发']['A名器度']*c['开发']['腰技']
            e['肛射经验'] += count
            e['精液经验'] += count
            a.t('在{}的肠内射精了{}次'.format(c['名字'],count))
            liquid_list = eject_liquid(get_leading_character(),'阴茎',1+c['开发']['A名器度']*c['开发']['腰技'])
            inject_liquid(c,'肛门',liquid_list)
        e['腰技经验'] += 1
    if movie == '全程性交':
        m['好感度'] += 500
        m['侍奉快乐'] += 60
        m['恭顺'] += 20000
        m['屈服'] += 20000
        m['欲情'] += 20000
        m['羞耻'] += 20000
        e['露出经验'] += 30
        e['侍奉经验'] += 10
        if c['经验']['V经验']>0 and not c['性别'] == '女性':
            count = 5*(1+c['开发']['V名器度']*c['开发']['腰技'])
            e['腔射经验'] += count
            e['精液经验'] += count
            a.t('在{}的腔内射精了{}次'.format(c['名字'],count))
            liquid_list = eject_liquid(get_leading_character(),'阴茎',count)
            inject_liquid(c,'阴道',liquid_list)
        else:
            count = 5*(1+c['开发']['A名器度']*c['开发']['腰技'])
            e['肛射经验'] += count
            e['精液经验'] += count
            a.t('在{}的肠内射精了{}次'.format(c['名字'],count))
            liquid_list = eject_liquid(get_leading_character(),'阴茎',1+c['开发']['A名器度']*c['开发']['腰技'])
            inject_liquid(c,'肛门',liquid_list)
        e['腰技经验'] += 10
    c = memory_cal(c)