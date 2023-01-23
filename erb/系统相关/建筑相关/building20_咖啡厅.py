from math import ceil
from random import randint
import erajs.api as a
from erb.系统相关.人物相关.人物列表插件 import detail_character
from erb.系统相关.口上相关.地文.咖啡厅地文 import perform_bad, perform_good
from erb.系统相关.调教相关.memory_cal import memory_cal, pp_cal
from erb.系统相关.调教相关.服装.服装 import cal_mean_beauty

def exec20(building):
    #根据人物的色情度和人物技巧给予奖励
    LISTS = find_free_and_workers()
    worker = LISTS['worker']

    if len(worker) == 0:
        a.divider()
        a.t('咖啡厅本周似乎正在歇业。')
        return True
    
    mean_beauty = cal_mean_beauty(worker)

    def rate_performance_bouns():
        total_performance = 0
        for student_id in worker:
            student = worker[student_id]
            total_performance += student['开发']['侍奉欲望']
        return ceil(total_performance*10.0/3)/10.0
    
    def find_bad_worker():
        #找到表现最差的员工
        worest_service = 10e9
        worst_worker = []
        for student_id in worker:
            student = worker[student_id]
            point = student['衣物效果']['色情度']*student['开发']['侍奉欲望']
            if point<worest_service:
                worest_service = point
                worst_worker = student
        return worst_worker
    
    def find_good_worker():
        #找到表现最好的员工
        best_service = -10e9
        best_worker = []
        for student_id in worker:
            student = worker[student_id]
            point = student['衣物效果']['色情度']*student['开发']['侍奉欲望']
            if point>best_service:
                best_service = point
                best_worker = student
        return best_worker
    
    fame = a.sav()['学院名气度']
    #咖啡厅赚钱存在上限
    basic_point = min(fame+mean_beauty, 9500) + 500
    point = randint(ceil(basic_point*0.8),ceil(basic_point*1.2))
    gain_money = point*max(1,rate_performance_bouns())
    a.sav()['资源']['金钱'] += gain_money

    for student_id in worker:
        student = worker[student_id]
        m = student['待处理记忆']
        e = student['待处理经验']

        m['主导'] += 1000
        m['恭顺'] += 2000
        m['屈服'] += 2000
        m['羞耻'] += 500
        m['反感'] += 500
        m['侍奉快乐'] += 2
        e['侍奉经验'] += 5
        student['待处理体力变化'] = [200,1000,50]
        pp_cal(student)
        student = memory_cal(student)
        if student['体力值'] < 100:
            student['体力值'] = max(10,student['体力值'])
            student['工作状态'] = '空闲'
            a.msg('{}太累了，去休息了'.format(student['名字']))
        
    a.divider()
    if point<basic_point:
        perform_bad(find_bad_worker())
    else:
        perform_good(find_good_worker())
    a.t()
    a.t('咖啡厅本周赚取了{}G。'.format(gain_money))
    a.t()
    


def destory20(building):
    
    return True

def structure20(building={}):

    return True

def setting20(building):
    #数据
    LISTS = find_free_and_workers()
    worker = LISTS['worker']
    free = LISTS['free']

    def try_add(c):
        a.divider()
        a.mode()
        if len(worker)>=8:
            a.t('工作人员已满',wait=True)
        elif not check_allow_add(c):
            a.t('{}还不能胜任咖啡厅的工作!'.format(c['名字']),wait=True)
        else:
            c['工作状态'] = '咖啡厅'
        a.repeat()
    
    def try_delete(c):
        c['工作状态'] = '空闲'
        a.repeat()

    def show_list(cl,type):
        a.divider()
        a.mode('grid',7)
        #cl = a.sav()['character_list']['学生']
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
            a.progress(c['体力值'],c['最大体力值'], [{'width': '80px'}, {}])
            a.t()
            a.t('气:')
            a.progress(c['气力值'],c['最大气力值'], [{'width': '80px'}, {}])
            a.t()
            a.t('智:')
            a.progress(c['理智值'],c['最大理智值'], [{'width': '80px'}, {}])
            a.t()
            a.t('[{}]'.format(c['工作状态']))
            a.t()
            if type == 'worker':
                a.b('休息',try_delete,c)
            else:
                a.b('添加',try_add,c)
            a.t()

    def check_allow_add(c):
        #判断人物能否胜任工作
        #return True #debug用
        if c['好感度']<100 or c['开发']['服从']<=1 or c['体力值']<1000:
            return False
        if c['侍奉快乐']>50:
            return True
        elif c['侍奉快乐']>10 and c['好感度']>200:
            return True
        elif c['开发']['服从']>=3 or c['开发']['欲望']>=4:
            return True
        return False
    
    #设置页面
    a.page()
    a.mode('grid',1)
    a.h('咖啡厅工作配置')
    a.divider('目前工作人员')
    a.mode()
    show_list(worker,'worker')
    a.divider('可选工作人员')
    show_list(free,'free')
    
    a.divider()
    a.mode()
    a.b('返回',a.back)

def find_free_and_workers():
    #找到目前空闲的人和在咖啡馆工作的人
    free_list = {}
    worker_list = {}
    student_list = a.sav()['character_list']['学生']
    for student_id in student_list:
        student = student_list[student_id]
        if student['工作状态'] == '空闲':
            free_list[student_id] = student
        elif student['工作状态'] == '咖啡厅':
            worker_list[student_id] = student
    
    return {'free':free_list,'worker':worker_list}


