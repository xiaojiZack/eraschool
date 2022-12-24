import erajs.api as a
import random
from erb.系统相关.调教相关.memory_cal import all_cal
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

        def determine_participants():
            a.divider()
            a.t('要选择哪些学生参加本课程？')
            a.mode('grid',6)
            a.tmp()['调教数据']={}
            a.tmp()['调教数据']['参与者'] = []
            a.tmp()['调教数据']['参与者'].append(a.sav()['character_list']['主角'])
            cl = a.sav()['character_list']['学生']
            for i in cl:
                c = cl[i]
                a.b(c['名字'], a.goto, detail_character, c)
                a.t()
                if c['性别'] == '男性':
                    a.t('♂')
                elif c['性别'] == '女性':
                    a.t('♀')
                else:
                    a.t('♀♂')
                a.t()
                a.t('体力:')
                a.progress(c['体力值'],c['最大体力值'], [{'width': '100px'}, {}])
                a.t('({}/{})'.format(c['体力值'],c['最大体力值']))
                a.t()
                a.t('理智:')
                a.progress(c['理智值'],c['最大理智值'], [{'width': '100px'}, {}])
                a.t('({}/{})'.format(c['理智值'],c['最大理智值']))
                a.t()
                course_effect = cal_course_effect(c, course_tag, course_difficulity)
                effect_type = {'color':'#000'}
                if course_effect == 'C':
                    effect_type = {'color':'#778899'}
                elif course_effect == 'B':
                    effect_type = {'color':'#FFFF00'}
                elif course_effect == 'A':
                    effect_type = {'color':'#008000'}
                elif course_effect == 'S':
                    effect_type = {'color':'#FFC1C1'}
                elif course_effect == 'SS':
                    effect_type = {'color':'#FF00FF'}
                elif course_effect == 'SSS':
                    effect_type = {'color':'#FF0000'}
                a.t('预估表现:')
                a.t('{}'.format(course_effect), style = effect_type)
                a.t()
                a.b('决定',determine,c, material_determine['效果'],course_effect)
                a.t()

        a.page()
        a.mode()
        determine_details()
        determine_participants()

    def determine(c, effect, effect_type):
        #结算效果
        dic = {'SSS':5,'SS':4,'S':3,'A':2,'B':1,'C':0}
        el = dic[effect_type]
        effect_type_level = [0.5, 1, 1.5, 2, 3, 5]
        for i in effect:
            if i == '随机技术':
                tech_list = ['腰技经验','舌技经验','指技经验','魔乳经验','足技经验']
                for j in range(effect['随机技术']):
                    c['待处理经验'][random.choice(tech_list)] += 1
            elif i =='体力变化':
                c['待处理体力变化'] = effect[i]*effect_type_level[el]
            elif not '经验' in i:
                c['调教记忆'][i] += effect[i]*effect_type_level[el]
            else:
                c['待处理经验'][i] += effect[i]*effect_type_level[el]

        all_cal(c)
        end_cal(c)
        a.back()

    a.tmp()['储存选择'] = 0
    a.tmp()['选择对象'] = '普通AV'
    a.goto(plan)


