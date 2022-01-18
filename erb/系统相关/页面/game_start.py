import erajs.api as a
import funcs as f
import main_page

def game_start():
     
    a.page()
    a.mode('grid')
    a.t('game_start')
    a.t()
    a.b('开始',a.goto, game_init)

def game_init():
    save = a.sav()
    save = {}

    save['time'] = {
        'year':1, 'season':1,
        'week':1, 'day':1,
        'total_day':1
    }
    save['character_list'] = {
        "character_number":0
    }

    save['resource'] = {
        'money':0,  'semen':0,
        'lilim_liquid':0, 'life_energy':0,
    }

    save['achievement'] = {}
    save['item'] = {}
    save['building'] = {}
    save['tech'] = {}

    a.goto()
