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
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':10,
                '习得':200,
                '羞耻':500,
                '恭顺':1000,
                '反感':50,
                '体力变化':[0,100,10],
                '随机技术':1,
            },
            '施行需求':check_tech(['课程组件:女仆侍奉']),
            '难度':0,
            'tag':[],
            '说明':'仅仅只是要求装扮成女仆进行日常的打扫活动。',
            '能否施行':True
        }
        material_list['榨精侍奉'] = {
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':0,
                '习得':0,
                '羞耻':0,
                '恭顺':0,
                '反感':0,
                '体力变化':[0,10,10],
                '随机技术':0,
                '催眠':0,
            },
            '施行需求':check_tech(['无']),
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
        
        a.page()
        a.mode()
        determine_details()
        determine_participants(course_tag, course_difficulity,material_determine)
    if not '课程组件:常识变更' in a.sav()['科技']:
        a.sav()['科技'].append('课程组件:常识变更')
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
                select_material['施行需求'] = select_material['施行需求']*method['新增施行需求']

        return select_material

    a.divider('课程细节')
    a.t('具体需要指导哪种侍奉方法？')
    a.t()

    types_list = {'无':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                    },
                    '施行需求':check_tech(['无']),
                    '难度':0,
                    'tag':[],
                    '说明':'',
                    '能否施行':True
                    },
                  '手交':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '指技经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                    },
                  '足交':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '足技经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                    },
                  '口交':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '舌技经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                  },
                  '乳交':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '魔乳经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                  },
                  '素股':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '腰技经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
                    '说明':'',
                    '能否施行':True
                  },
                  '骑乘':{
                    '花费':{
                    '金钱':0,
                    },
                    '效果':{
                        '欲情':200,
                        '习得':200,
                        '羞耻':100,
                        '恭顺':100,
                        '反感':50,
                        '体力变化':[0,10,10],
                        '腰技经验':1,
                    },
                    '施行需求':check_tech(['无']),
                    '难度':10,
                    'tag':['精液','脏污','主导'],
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
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':-10,
                '习得':-10,
                '羞耻':-10,
                '恭顺':-10,
                '反感':-10,
                '体力变化':[0,10,10],
                '随机技术':0,
                '催眠':0,
            },
            '新增施行需求':check_tech(['无']),
            '难度':-5,
            '新增tag':[],
            '删除tag':['精液','脏污','主导'],
        },
        '假阳具练习':{
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':0,
                '习得':0,
                '羞耻':0,
                '恭顺':0,
                '反感':-10,
                '体力变化':[0,10,10],
                '随机技术':0,
                '催眠':0,
            },
            '新增施行需求':check_tech(['无']),
            '难度':-5,
            '新增tag':['主导'],
            '删除tag':['精液','脏污'],
        },
        '实际练习':{
            '花费':{
                '金钱':0,
            },
            '效果':{
                '欲情':0,
                '习得':0,
                '羞耻':0,
                '恭顺':0,
                '反感':0,
                '体力变化':[0,10,10],
                '随机技术':0,
                '催眠':0,
            },
            '新增施行需求':check_tech(['无']),
            '难度':0,
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