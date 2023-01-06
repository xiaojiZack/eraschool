from operator import truediv
import erajs.api as a
from erb.系统相关.页面.day_pass import character_recover

def plan0():
    a.cls()
    a.page()
    a.t('随意度过了一段时间……',wait=True)
    character_recover()
    a.repeat()