import erajs.api as a
from erb.系统相关.口上相关.口上调用 import comkojo
from erb.系统相关.调教相关.体力衰减 import sum_pp
from erb.系统相关.调教相关.命令.下一回合 import singal_step
from erb.系统相关.调教相关.命令.执行列表增减 import append_doing_list, check_doing_list
from erb.系统相关.调教相关.液体 import inject_liquid
from funcs import unwait, wait
from ..com_check import obey_check
from ...人物相关.character_class import search_quaility as sq

comid = 102
def com102(active,passive):
    
    aname = active['名字']
    pname = passive['名字']
    com_trait = ['药物']
    am = active['待处理记忆']
    ae = active['待处理经验']
    pm = passive['待处理记忆']
    pe = passive['待处理经验']

    f = False
    
    def design_page(active,passive):
        #具体设定注射细节，包括使用的药物、注射的位置
        drug_list = []
        body_part = ''
        can_add_drug = ['媚药','利尿剂','排卵诱发剂']
        for drug in can_add_drug:
            if a.sav()['道具'][drug] <1:
                can_add_drug.remove(drug)
        can_add_body_part = ['血液','阴道','子宫','乳房','尿道'] #阴核和阴茎待做

        def select_drug(selection):
            drug_list = [selection['value']]

        def select_body_part(selection):
            body_part = selection['value']
        
        a.page()
        a.mode()
        a.divider('使用药物')
        a.t()
        a.radio(can_add_drug, select_drug)
        a.t()
        a.divider('注射部位')
        a.radio(can_add_body_part,select_body_part)
        a.t()
        a.b('决定', inject, drug_list, body_part)
        wait()
    
    def inject(drug_list, body_part):
        if drug_list == [] or body_part == '':
            a.msg('请选择要注射的液体和药物')
        else:
            inject_liquid(passive, body_part, drug_list)
            unwait()

    if obey_check(100,active,passive,com_trait):
        design_page()
        pm['恐惧'] += 10000
        pm['药毒'] += 10000
        pm['反感'] += 10000
        pm['屈服'] += 5000
        pm['欲情'] += 500
        pe['药物经验'] += 5
        comkojo(active,passive,comid,{'com':'add'})
    else:
        comkojo(active,passive,comid,{'com':'fail'})
        pm['反感'] += 8000
        pm['好感度'] += -5

        f = False

    return f
