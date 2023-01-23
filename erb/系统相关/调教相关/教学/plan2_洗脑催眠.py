import erajs.api as a
import random
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.教学.plan组件 import check_tech, determine_participants
from erb.系统相关.调教相关.教学.课程效果计算 import cal_course_effect
from erb.系统相关.调教相关.记忆结算 import end_cal
from erb.系统相关.页面.check_character import detail_character

def plan2():
    def plan():
        course_tag = []
        course_difficulity = 0
        #放置课程使用的材料， 包含使用花费、效果。自主制作的材料由外界函数取得
        #TODO
        material_list = {}
        material_list['性知识讲解'] = {
            '名称':'性知识讲解',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':1000,
                '习得':2000,
                '羞耻':1000,
                '反感':100,
                '体力变化':[0,100,10],
                '随机技术':1,
                '催眠':1,
            },
            '施行需求':check_tech(['课程组件:性知识讲解']),
            '难度':5,
            'tag':[],
            '说明':'普通地科普性知识，但是在一些细节上有微妙的不同。',
            '能否施行':True
        }
        material_list['常识变更'] = {
            '名称':'常识变更',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':3000,
                '习得':3000,
                '羞耻':2000,
                '屈服':2000,
                '恭顺':2000,
                '反感':500,
                '体力变化':[0,200,50],
                '随机技术':0,
                '催眠':2,
            },
            '施行需求':check_tech(['课程组件:常识变更']),
            '难度':20,
            'tag':[],
            '说明':'灌输性奴观念，扭曲常识，合理化性行为',
            '能否施行':True
        }
        material_list['催眠'] = {
            '名称':'催眠',
            '花费':{
                '金钱':5000,
            },
            '效果':{
                '欲情':20000,
                '习得':1000,
                '羞耻':1000,
                '屈服':8000,
                '恭顺':5000,
                '反感':50,
                '体力变化':[0,300,200],
                '随机技术':0,
                '催眠':10,
            },
            '施行需求':check_tech(['课程组件:催眠']),
            '难度':30,
            'tag':[],
            '说明':'‘催眠什么的怎么可能是真的嘛’',
            '能否施行':True
        }
        #去除不可执行的部分
        for i in ['性知识讲解','常识变更','催眠']:
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
    if not '课程组件:常识变更' in a.sav()['科技']:
        a.sav()['科技'].append('课程组件:常识变更')
    a.tmp()['储存选择'] = 0
    a.tmp()['选择对象'] = "常识变更"
    a.goto(plan)
