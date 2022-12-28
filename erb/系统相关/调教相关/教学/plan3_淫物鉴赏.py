import erajs.api as a
import random
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.教学.plan组件 import determine_participants
from erb.系统相关.调教相关.教学.课程效果计算 import cal_course_effect
from erb.系统相关.调教相关.记忆结算 import end_cal
from erb.系统相关.页面.check_character import detail_character
def plan3():
    def plan():
        course_tag = []
        course_difficulity = 0
        #放置课程使用的材料， 包含使用花费、效果。自主拍摄的制作的材料由外界函数取得
        #TODO
        material_list = {}
        material_list['普通AV'] = {
            '花费':{
                '金钱':100,
            },
            '效果':{
                '欲情':1000,
                '习得':1000,
                '羞耻':1000,
                '反感':100,
                '体力变化':[0,50,5],
                '随机技术':5,
            },
            '难度':0,
            'tag':[],
            '说明':'与学生共同观赏一些从市面上随便买的一些AV,有些看封面就知道没啥意思。'
        }
        material_list['热门AV'] = {
            '花费':{
                '金钱':1000,
            },
            '效果':{
                '欲情':5000,
                '习得':5000,
                '羞耻':5000,
                '反感':100,
                '体力变化':[0,50,5],
                '随机技术':20,
            },
            '难度':0,
            'tag':[],
            '说明':'与学生共同观赏一些目前市面上流行的AV，至少封面看起来不错。'
        }
        material_index = a.tmp()['储存选择']
        material_determine = material_list[a.tmp()['选择对象']]
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


    a.tmp()['储存选择'] = 0
    a.tmp()['选择对象'] = '普通AV'
    a.goto(plan)


