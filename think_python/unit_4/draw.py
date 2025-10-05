""" import jupyturtle

# print(display)
jupyturtle.make_turtle()
jupyturtle.forward(100)

jupyturtle.show()
# display(jupyturtle.get_turtle())
from IPython.display import display
 """

import jupyturtle

jupyturtle.make_turtle()
jupyturtle.forward(100)

# Guardar como archivo HTML
with open('turtle_drawing.html', 'w') as f:
    f.write(jupyturtle.get_SVG().data)
