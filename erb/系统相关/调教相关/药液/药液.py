
from math import ceil


drug_element_list = {
    '媚药':{
        'cy':0.9,
        'cc':0.05,
        'mz':0,
        'hf':0,
        'ln':0.05,
        'yd':1
    },
    '利尿剂':{
        'cy':0,
        'cc':0,
        'mz':0,
        'hf':0,
        'ln':1,
        'yd':0.8
    },
    '避孕药':{
        'cy':0,
        'cc':-10,
        'mz':0,
        'hf':0,
        'ln':0,
        'yd':0
    },
    '强精剂':{
        'cy':0.05,
        'cc':0,
        'mz':0,
        'hf':0.5,
        'ln':0.05,
        'yd':0.2
    },
    '排卵促进剂':{
        'cy':0.1,
        'cc':0.9,
        'mz':0,
        'hf':0,
        'ln':0,
        'yd':1
    },
    '肌肉松弛剂':{
        'cy':-0.5,
        'cc':0,
        'mz':0.5,
        'hf':0,
        'ln':0,
        'yd':1
    },
    '精液':{
        'cy':0.05,
        'cc':0.02,
        'mz':0,
        'hf':0,
        'ln':0,
        'yd':0
    },
    '强媚药':{
        'cy':2,
        'cc':0.4,
        'mz':0.4,
        'hf':0,
        'ln':0.4,
        'yd':2.5
    },
    '体力剂':{
        'cy':0,
        'cc':0,
        'mz':0,
        'hf':1,
        'ln':0,
        'yd':0.2
    }
}

body_part_absorb_effect = {
    '血液':{
        'cy':1.2,
        'cc':1.2,
        'mz':1.2,
        'hf':1.2,
        'ln':1.2,
        'yd':1.2,
        'drain':1   #过夜排出率
    },
    '子宫':{
        'cy_V':3,
        'cy_W':3,
        'cc':3,
        'mz_V':2,
        'mz_W':2,
        'mz':0.5,
        'hf':0.5,
        'ln':0.5,
        'yd':2,
        'drain':0.5   #过夜排出率
    },
    '尿道':{
        'cy_U':2,
        'cy_C':2,
        'cc':0.5,
        'mz_U':2,
        'mz_C':2,
        'mz':0.5,
        'hf':0.5,
        'ln':3,
        'yd':2,
        'drain':0.8   #过夜排出率
    },
    '肠道':{
        'cy_A':2,
        'cc':3,
        'mz_A':2,
        'mz':0.5,
        'hf':2,
        'ln':0.5,
        'yd':2,
        'drain':0.8   #过夜排出率
    },
    '乳房':{
        'cy_B':2,
        'cc':1.5,
        'mz_B':2,
        'mz':0.5,
        'hf':0.5,
        'ln':0.5,
        'yd':2,
        'drain':0.5   #过夜排出率
    },
    '胃':{
        'cy_M':1,
        'cc':0.5,
        'mz':0.5,
        'hf':1,
        'ln':0.5,
        'yd':1,
        'drain':1   #过夜排出率
    }
}

def effect_absorb(drug_list, body_part, weight):
#计算某部位内药物的具体成分效果
    drug_effects = {
        'cy':0,
        'cc':0,
        'mz':0,
        'hf':0,
        'ln':0,
        'yd':0
    }
     #计算药物元素体积
    for drug in drug_list:
        if drug in drug_element_list.keys():
            element_rate = drug_element_list[drug]
            for element in element_rate:
                drug_effects[element] += drug_list[drug]*element_rate[element]/(weight/60/50) #60kg,50ml为基准

    #增加吸收部位系数,将实际效果写到effects里
    effects = {}
    absorb_coeff = body_part_absorb_effect[body_part]
    for element in drug_effects:
        for coeff in absorb_coeff:
            if element in coeff:
                if coeff in effects.keys():
                    effects[coeff] += drug_effects[element]*absorb_coeff[coeff]
                else:
                    effects[coeff] = drug_effects[element]*absorb_coeff[coeff]
    
    return effects

def update_drug(p):
    #更新人物体内药剂产生的效果
    b = p['身体信息']
    body_parts = ['血液','肠道','胃','尿道','子宫','乳房']
    drugs_effects = {}
    for bp in body_parts:
        drugs_list = p['身体信息'][bp]['内容液体']
        effects = effect_absorb(drugs_list,bp,b['具体体重'])
        for i in effects:
            if i in drugs_effects.keys():
                drugs_effects[i] += effects[i]
            else:
                drugs_effects[i] = effects[i]
        liquid_list = p['身体信息'][bp]['内容液体']
        new_volume = 0

        liquid_type_list = list(liquid_list.keys()).copy()
        for d in liquid_type_list:
            new_volume += liquid_list[d]
            if liquid_list[d] <=0:
                liquid_list.pop(d)
        p['身体信息'][bp]['内容总量'] = new_volume
    
    p['药物效果'] = drugs_effects

def drain_drugs(p):
    #过夜流失药物
    b = p['身体信息']
    body_parts = ['血液','肠道','胃','尿道','子宫','乳房']

    for bp in body_parts:
        total_volume = 0
        drug_lists = b[bp]['内容液体']
        for drugs in drug_lists:
            drug_lists[drugs] -= ceil(drug_lists[drugs]*body_part_absorb_effect[bp]['drain'])
            drug_lists[drugs] = max(0,drug_lists[drugs])
            total_volume += drug_lists[drugs]
        
        b[bp]['内容总量'] = total_volume
        b[bp]['内容液体'] = drug_lists
