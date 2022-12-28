import erajs.api as a
import random
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.教学.plan组件 import check_tech, determine_participants
from erb.系统相关.调教相关.教学.课程效果计算 import cal_course_effect
from erb.系统相关.调教相关.记忆结算 import end_cal
from erb.系统相关.页面.check_character import detail_character

def plan5():
    def plan():
        course_tag = []
        course_difficulity = 0
        
        #去除不可执行的部分
        type_list = list(material_list.keys())
        for i in type_list:
            if material_list[i]['施行需求'] == False:
                material_list.pop(i)
        
        if len(material_list) == 0:
            a.msg('无可用计划')
            a.back()
            return False
        
        if '储存选择' in a.tmp().keys():
            material_index = a.tmp()['储存选择']
        else:
            material_index = 0
        if '选择对象' in a.tmp().keys():
            material_determine = material_list[a.tmp()['选择对象']]
        else:
            material_determine = material_list[list(material_list.keys())[0]]

        course_tag = material_determine['tag']
        course_difficulity = material_determine['难度']

        def determine_details():
            def AV_selection(selection):
                a.tmp()['储存选择'] = selection['index']
                a.tmp()['选择对象'] = selection['value']
                a.repeat()

            a.divider('课程细节')
            a.t('选择哪种？')
            a.t()
            a.radio(list(material_list.keys()), AV_selection, material_index)
            a.t()
            a.t('花费:{}'.format(material_determine['花费']))
            a.t()
            a.t('课程tag:{}'.format(course_tag))
            a.t()
            a.t('难度:{}'.format(course_difficulity))
            a.t()
            a.t('课程说明:{}'.format(material_determine['说明']))


        a.page()
        a.mode()
        determine_details()
        determine_participants(course_tag, course_difficulity,material_determine)
    
    material_list = {}
    material_list['健身操'] = {
        '花费':{
            '金钱':0,
        },
        '效果':{
            '体力变化':[0,200,0],
            '体力增长':50
        },
        '施行需求':check_tech(['无']),
        '难度':0,
        'tag':[],
        '说明':'',
        '能否施行':True
    }
    material_list['跑步'] = {
        '花费':{
            '金钱':0,
        },
        '效果':{
            '体力变化':[100,800,0],
            '体力增长':200
        },
        '施行需求':check_tech(['课程组件:跑步','操场']),
        '难度':0,
        'tag':[],
        '说明':'',
        '能否施行':True
    }
    material_list['游泳'] = {
        '花费':{
            '金钱':0,
        },
        '效果':{
            '体力变化':[300,1000,0],
            '体力增长':400
        },
        '施行需求':check_tech(['课程组件:游泳','泳池']),
        '难度':0,
        'tag':[],
        '说明':'',
        '能否施行':True
    }

    a.tmp()['储存选择'] = 0
    a.tmp()['选择对象'] = list(material_list.keys())[0]
    a.goto(plan)

