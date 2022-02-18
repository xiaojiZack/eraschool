import erajs.api as a
from erb.系统相关.事件.event_1_入学 import event1
from erb.系统相关.页面.main_page import main_page

def event0():
    def opening():
        a.cls()
        a.page()
        a.t('一段开幕')
        a.t()
        event1()
        a.goto(main_page)
    def passopening():
        event1()
        a.goto(main_page)

    a.cls()
    a.page()
    a.t('要观看开幕吗？')
    a.t()
    a.b('是',opening)
    a.t()
    a.b('否',passopening)