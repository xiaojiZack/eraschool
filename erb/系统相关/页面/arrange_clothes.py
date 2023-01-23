import erajs.api as a
from erb.系统相关.调教相关.服装.服装 import cal_accpection, check_cloth_allow, cloth_rate_color, init_cloth, updata_cloth

def arrange_clothes_page(c):
    #更换衣物页面
    updata_cloth(c)
    a.cls()
    a.page()
    a.mode('line',1)
    clothes = c['衣物']
    for cloth_type in clothes:
        a.t('{}:'.format(cloth_type))
        if '配件' in cloth_type:
            for cloth in clothes[cloth_type]:
                a.b(cloth['名称'],remove_equipment,c,cloth_type,cloth['名称'])
                a.t(' ')
            a.b("[+]",a.goto,add_equipment,c,cloth_type)
        else:
            if clothes[cloth_type] == {}: a.b('[  ]',a.goto,change_clothes,c,cloth_type)
            else:a.b('{}'.format(clothes[cloth_type]['名称']),a.goto,change_clothes,c,cloth_type)
        a.t()
    a.divider()
    a.t('色情度:{}'.format(c['衣物效果']['色情度']), style=cloth_rate_color(c))
    a.t()
    a.t('羞耻度:{}'.format(c['衣物效果']['羞耻度']), style=cloth_rate_color(c))
    a.t()
    a.t('接受值:{}'.format(cal_accpection(c)))
    a.t()
    for bt in ['阴部','胸部','肛门']:
        a.t('{}:'.format(bt))
        if c['衣物效果']['关键部位'][bt]: a.t('可见',style={'color':'#FFC1C1'})
        else: a.t('不可见')
        a.t()
    a.divider()
    if cal_accpection(c) >= c['衣物效果']['羞耻度']:
        a.b('决定',a.back)
    else:
        a.b('{}不愿意穿上这套衣服'.format(c['名字']))

def change_clothes(c, cloth_type):
    def change_button(cloth_name):
        if cloth_name == '': c['衣物'][cloth_type] = {}
        else: 
            new_cloth = init_cloth(cloth_name)
            c['衣物'][cloth_type] = new_cloth
            cost_item(new_cloth)
            remove_conflict(c['衣物'],cloth_type)
        a.back()
    
    #替换某部分的衣服
    cloth_data = a.dat()['cloth_item'][cloth_type]

    a.page()
    a.mode()
    a.b('不穿', change_button, '')
    a.t()
    for cloth in cloth_data:
        if check_cloth_allow(c,init_cloth(cloth)):
            a.b(cloth, change_button, cloth)
        else:
            a.b(cloth)
        a.t()
    
    a.divider()
    a.b('放弃更改',a.back)

def remove_conflict(cloth_list, new_cloth_type):
    #去除冲突衣物
    if new_cloth_type == '贴身全身':
        cloth_list['上衣'] = {}
        cloth_list['下衣'] = {}
        cloth_list['贴身上衣'] = {}
        cloth_list['贴身下衣'] = {}
    if new_cloth_type == '全身':
        cloth_list['上衣'] = {}
        cloth_list['下衣'] = {}
    if new_cloth_type == '上衣':
        cloth_list['贴身全身'] = {}
        cloth_list['全身'] = {}
    if new_cloth_type == '下衣':
        cloth_list['贴身全身'] = {}
        cloth_list['全身'] = {}
    if new_cloth_type == '贴身上衣':
        cloth_list['贴身全身'] = {}
    if new_cloth_type == '贴身下衣':
        cloth_list['贴身全身'] = {}

def add_equipment(c, cloth_type):
    #增加配件
    def add_button(cloth_name):
        new_cloth = init_cloth(cloth_name)
        c['衣物'][cloth_type].append(new_cloth) 
        cost_item(new_cloth)
        remove_conflict(c['衣物'],cloth_type)
        a.back()
    
    def check_repeat(cloth):
        for equiped_cloth in c['衣物'][cloth_type]:
            if equiped_cloth['名称'] == cloth:
                return True
        return False

    cloth_data = a.dat()['cloth_item'][cloth_type]
    a.page()
    a.mode()
    for cloth in cloth_data:
        if not check_repeat(cloth) and check_cloth_allow(c,init_cloth(cloth)):
            a.b(cloth, add_button, cloth)
            a.t()
    
    a.divider()
    a.b('放弃更改',a.back)

def remove_equipment(c, cloth_type, cloth_name):
    cloth_list = c['衣物'][cloth_type].copy()
    for cloth in cloth_list:
        if cloth['名称'] == cloth_name:
            recycle_item(cloth)
            c['衣物'][cloth_type].remove(cloth)
            a.repeat()
            return True

def cost_item(cloth):
    #消耗道具
    if cloth['前置']['道具'] == '':
        pass
    else:
        a.sav()['物品'][cloth['前置']['道具']] -= 1

def recycle_item(cloth):
    #回收道具
    if cloth['前置']['道具'] == '':
        pass
    else:
        a.sav()['物品'][cloth['前置']['道具']] += 1