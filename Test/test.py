import schemdraw
import schemdraw.elements as elm

elm.Resistor().label('R1')

d = schemdraw.Drawing()
d.add(elm.Resistor())
d.add(elm.Capacitor())
d.add(elm.Diode())
d.draw()