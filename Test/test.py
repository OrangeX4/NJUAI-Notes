import matplotlib
matplotlib.use('TkAgg')
from schemdraw import elements as elm
from schemdraw import Drawing, logic

d = Drawing()
d += (A := elm.Line().down().label('A', 'right'))

d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()

d += elm.Line().right().at(A.end)
d += logic.Not().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d += elm.Line().down()
d.draw()