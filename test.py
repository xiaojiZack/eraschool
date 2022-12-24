import cx_Freeze
import erajs.api as a
import funcs as f
from erb.系统相关.页面.game_start import game_start

a.init()
a.cls()

a.footer('@xiaoji')
a.goto(game_start)