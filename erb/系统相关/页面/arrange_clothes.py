import erajs.api as a
from erb.系统相关.调教相关.服装.服装 import cal_accpection, cloth_rate_color, init_cloth, updata_cloth

def arrange_clothes_page(c):
    #更换衣物页面
    updata_cloth(c)
    a.page()
    a.mode('line',1)
    clothes = c['衣物']
    for cloth_type in clothes:
        a.t('{}:'.format(cloth_type))
        if clothes[cloth_type] == {}: a.b('没穿',a.goto,change_clothes,c,cloth_type)
        else:a.b('{}'.format(clothes[cloth_type]['名称']),a.goto,change_clothes,c,cloth_type)
        a.t()
    a.divider()
    a.t('色情度:{}'.format(c['衣物效果']['色情度']), style=cloth_rate_color(c))
    a.t()
    a.t('羞耻度:{}'.format(c['衣物效果']['羞耻度']), style=cloth_rate_color(c))
    a.t()
    a.t('接受值:{}'.format(cal_accpection(c)))
    a.divider()
    if cal_accpection(c) >= c['衣物效果']['羞耻度']:
        a.b('决定',a.back)
    else:
        a.b('{}不愿意穿上这套衣服'.format(c['名字']))

def change_clothes(c, cloth_type):
    def change_button(cloth_name):
        if cloth_name == '': c['衣物'][cloth_type] = {}
        else: 
            c['衣物'][cloth_type] = init_cloth(cloth_name)
            remove_conflict(c['衣物'],cloth_type)
        a.back()
    
    #替换某部分的衣服
    cloth_data = a.dat()['cloth_item'][cloth_type]

    a.page()
    a.mode()
    a.b('不穿', change_button, '')
    a.t()
    for cloth in cloth_data:
        a.b(cloth, change_button, cloth)
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

def change_equipment(c, cloth_type):
    #对于配件的调整
    pass