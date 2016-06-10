import turtle
octagon = turtle.Pen()

def MyOctagon(size, filled):
    if filled == True:
        octagon.begin_fill()
    for i in range(0,8):
        octagon.forward(size)
        octagon.left(45)
    if filled == True:
        octagon.end_fill()

octagon.color(0.75, 0.9, 0)
MyOctagon(50, True)
octagon.color(0, 0, 0)
MyOctagon(50, False)
