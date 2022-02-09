import erajs.api as a

def check_doing_list(active,passive,com):
    t = a.tmp()['执行列表']
    if [active['CharacterId'],passive['CharacterId'],com] in a.tmp()['执行列表']:
        return True
    else: return False

def append_doing_list(active,passive,com):
    if check_doing_list(active,passive,com):
        return False
    else:
        a.tmp()['执行列表'].append([active['CharacterId'],passive['CharacterId'],com])

def remove_doing_list(active,passive,com):
    if check_doing_list(active,passive,com):
        a.tmp()['执行列表'].remove([active['CharacterId'],passive['CharacterId'],com])
    else:
        return False