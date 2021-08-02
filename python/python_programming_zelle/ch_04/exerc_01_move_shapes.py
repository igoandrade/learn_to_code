"""
Programa: exerc_01_move_shapes.py

Enunciado:
    1. Alter the program from the last discussion question in the following ways:
        (a) Make it draw squares instead of circles.
        (b) Have each successive click draw an additional square on the screen
        (rather than moving the existing one).
        (c) Print a message on the window "Click again to quit" after the loop,
        and wait for a final click before closing the window.
"""
from graphics import *

def main():
    win = GraphWin()

    shape = Rectangle(Point(80,80), Point(120,120))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        new_shape = shape.clone()
        p = win.getMouse()
        c = new_shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        new_shape.move(dx,dy)
        new_shape.draw(win)
    
    Text(Point(100,190), "Clique de novo para sair").draw(win)
    win.getMouse()
    win.close()

main()