import erajs.api as a
import random
from erb.系统相关.调教相关.memory_cal import all_cal
from erb.系统相关.调教相关.教学.plan组件 import check_tech, determine_participants
from erb.系统相关.调教相关.教学.课程效果计算 import cal_course_effect
from erb.系统相关.调教相关.记忆结算 import end_cal
from erb.系统相关.页面.check_character import detail_character

def plan4():
    def plan():
        course_tag = []
        course_difficulity = 0
        #放置课程使用的材料， 包含使用花费、效果。自主制作的材料由外界函数取得
        #TODO
        material_list = {}
        material_list['女仆侍奉'] = {
            '名称':'女仆侍奉',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':100,
                '屈服':500,
                '习得':250,
                '主导':1000,
                '羞耻':500,
                '恭顺':1000,
                '反感':100,
                '体力变化':[0,400,10],
                '随机技术':1,
            },
            '施行需求':check_tech(['课程组件:女仆侍奉']),
            '难度':15,
            'tag':['主导'],
            '说明':'仅仅只是要求装扮成女仆进行日常的打扫活动。',
            '能否施行':True
        }
        material_list['榨精侍奉'] = {
            '名称':'榨精侍奉',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':0,
                '习得':0,
                '羞耻':0,
                '恭顺':0,
                '反感':0,
                '体力变化':[0,0,0],
                '随机技术':0,
                '催眠':0,
            },
            '施行需求':check_tech(['课程组件:榨精侍奉']),
            '难度':0,
            'tag':[],
            '说明':'灌输性奴观念，扭曲常识，合理化性行为',
            '能否施行':True
        }
        
        #去除不可执行的部分
        iter_i = list(material_list.keys()).copy()
        for i in iter_i:
            if material_list[i]['施行需求'] == False:
                material_list.pop(i)
        
        if len(material_list) == 0:
            a.msg('无可用计划')
            a.back()
            return False
        
        if '储存选择' in a.tmp().keys():
            material_index = a.tmp()['储存选择']
            a.tmp()['选择对象'] = list(material_list.keys())[material_index]
        else:
            material_index = 0
            a.tmp()['选择对象'] = list(material_list.keys())[0]
        if '选择对象' in a.tmp().keys():
            material_determine = material_list[a.tmp()['选择对象']]
        else:
            material_determine = material_list[list(material_list.keys())[0]]

        def determine_details(material_determine):
            def AV_selection(selection):
                a.tmp()['储存选择'] = selection['index']
                a.tmp()['选择对象'] = selection['value']
                a.repeat()

            a.divider('课程细节')
            a.t('选择哪种？')
            a.t()
            a.radio(list(material_list.keys()), AV_selection, material_index)
            a.t()
            if a.tmp()['选择对象'] == '榨精侍奉':
                material_determine = design_class()
            a.t()
            a.t('花费:{}'.format(material_determine['花费']))
            a.t()
            a.t('课程tag:{}'.format(material_determine['tag']))
            a.t()
            a.t('难度:{}'.format(material_determine['难度']))
            a.t()
            a.t('课程说明:{}'.format(material_determine['说明']))
            return material_determine
        
        a.page()
        a.mode()
        material_determine = determine_details(material_determine)
        course_difficulity = material_determine['难度']
        course_tag = material_determine['tag']
        determine_participants(course_tag, course_difficulity,material_determine)
    a.goto(plan)


def design_class():
    #详细设定榨精侍奉的具体教学内容，返回需要的花费和tag、难度

    def change_select(selection):
        #修改选择内容
        a.tmp()['存储选择_榨精侍奉_主题'] = selection['index']
        a.repeat()

    def change_teching_method(selection):
        a.tmp()['存储选择_榨精侍奉_教育方式'] = selection['index']
        a.repeat()

    def change_material(select_material, method):
        #根据选择的教学方式改变选择的材料

        for i in method:
            #名称改变部分
            select_material['名称'] = select_material['名称']+'-'+method['名称']
            #数值改变部分
            if i == '花费' or i=='效果':
                for j in method[i]:
                    if j in select_material[i].keys():
                        if j == '体力变化':
                            for k in range(0,3):
                                select_material[i][j][k] = max(0, select_material[i][j][k]+method[i][j][k])
                        else:
                            select_material[i][j] = max(0, select_material[i][j]+method[i][j])
            
            elif i=='难度':
                select_material[i] = max(0,select_material[i]+method[i])

            #词条增减部分
            elif i == '增加tag':
                for j in method[i]:
                    if not j in select_material['tag']:
                        select_material['tag'].append(j)
            elif i == '删除tag':
                for j in method[i]:
                    if j in select_material['tag']:
                        select_material['tag'].remove(j)
            elif i == '新增施行需求':
                select_material['施行需求'] = select_material['施行需求'] and method['新增施行需求']

        return select_material

    a.divider('课程细节')
    a.t('具体需要指导哪种侍奉方法？')
    a.t()

    types_list = {
                  '手交':{
                    '名称':'手交',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':2000,
                        '习得':2000,
                        '羞耻':1000,
                        '恭顺':1000,
                        '屈服':1000,
                        '主导':1000,
                        '反感':500,
                        '体力变化':[0,500,10],
                        '指技经验':10,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':20,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                    },
                  '足交':{
                    '名称':'足交',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':2000,
                        '习得':3000,
                        '羞耻':2000,
                        '恭顺':2000,
                        '屈服':2000,
                        '主导':2000,
                        '反感':700,
                        '体力变化':[0,650,15],
                        '足技经验':10,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':22,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                    },
                  '口交':{
                    '名称':'口交',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '快M':1000,
                        '欲情':3000,
                        '习得':5000,
                        '羞耻':3000,
                        '恭顺':2000,
                        '屈服':4000,
                        '主导':3000,
                        '反感':1000,
                        '体力变化':[0,700,45],
                        '舌技经验':10,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':35,
                    'tag':['精液','脏污','主导','M'],
                    '说明':'',
                    '能否施行':True
                  },
                  '乳交':{
                    '名称':'乳交',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '快B':1000,
                        '欲情':5000,
                        '习得':5000,
                        '羞耻':4000,
                        '恭顺':3000,
                        '屈服':5000,
                        '主导':4000,
                        '反感':2000,
                        '体力变化':[0,800,55],
                        '魔乳经验':10,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':45,
                    'tag':['精液','脏污','主导','B'],
                    '说明':'',
                    '能否施行':True
                  },
                  '素股':{
                    '名称':'素股',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '快C':2000,
                        '欲情':4000,
                        '习得':5000,
                        '羞耻':6000,
                        '恭顺':6000,
                        '屈服':5000,
                        '主导':8000,
                        '反感':5000,
                        '体力变化':[0,1000,80],
                        '腰技经验':5,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':50,
                    'tag':['精液','脏污','主导','C'],
                    '说明':'',
                    '能否施行':True
                  },
                  '骑乘':{
                    '名称':'骑乘',
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':3000,
                        '习得':2000,
                        '羞耻':1000,
                        '恭顺':6000,
                        '屈服':5000,
                        '主导':8000,
                        '反感':5000,
                        '体力变化':[0,1200,100],
                        '腰技经验':10,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':60,
                    'tag':['精液','脏污','主导','V','处女破坏'],
                    '说明':'',
                    '能否施行':True
                  }
                  }
    if '存储选择_榨精侍奉_主题'in a.tmp().keys():
        select_index = a.tmp()['存储选择_榨精侍奉_主题']
    else:
        select_index = 0

    a.radio(list(types_list.keys()), change_select, select_index)
    a.t()
    select_material = types_list[list(types_list.keys())[select_index]]

    teching_type = {
        '理论':{
            '名称':'理论',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':-1000,
                '习得':-1000,
                '羞耻':-1000,
                '恭顺':-1000,
                '反感':-1000,
                '屈服':-2000,
                '体力变化':[0,-200,-100],
                '随机技术':0,
                '催眠':1,
            },
            '新增施行需求':check_tech(['无']),
            '难度':-5,
            '新增tag':[],
            '删除tag':['精液','脏污','主导'],
        },
        '假阳具练习':{
            '名称':'假阳具练习',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':0,
                '习得':0,
                '羞耻':0,
                '恭顺':0,
                '反感':0,
                '体力变化':[0,0,0],
                '随机技术':0,
                '催眠':0,
            },
            '新增施行需求':check_tech(['无']),
            '难度':0,
            '新增tag':['主导'],
            '删除tag':['精液','脏污'],
        },
        '实际练习':{
            '名称':'实际练习',
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':1000,
                '习得':2000,
                '羞耻':2000,
                '恭顺':1000,
                '反感':2000,
                '体力变化':[0,200,100],
                '随机技术':0,
                '催眠':0,
            },
            '新增施行需求':check_tech(['无']),
            '难度':20,
            '新增tag':['精液','脏污','主导'],
            '删除tag':[],
        },
    }
    if '存储选择_榨精侍奉_教育方式' in a.tmp().keys():
        select_method_index = a.tmp()['存储选择_榨精侍奉_教育方式']
    else:
        select_method_index = 0
    
    a.t('选择教学方式')
    a.t()
    a.radio(list(teching_type.keys()), change_teching_method, select_method_index)
    a.t()

    select_method = teching_type[list(teching_type.keys())[select_method_index]]
    final_material = change_material(select_material, select_method)

    return final_material