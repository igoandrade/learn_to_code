"""
Write a program to animate a circle bouncing around a window. The basic
idea is to start the circle somewhere in the interior of the window. Use
variables dx and dy (both initialized to 1) to control the movement of the
circle. Use a large counted loop (say 10000 iterations), and each time
through the loop move the circle using dx anddy . When the x-value of the
center of the circle gets too high (it hits the edge), change dx to -1. When
it gets too low, change dx back to 1. Use a similar approach fordy .

Note: Your animation will probably run too fast. You can slow it down
by using update from the graphics library with a rate parameters. For
example, this loop will be limited to going around at a rate of 30 times per
second:
"""

from graphics import *
from random import randint, random

def move_bola(bola, limite, dx, dy):
    centro = bola.getCenter()
    raio = bola.getRadius()
    x0, y0 = centro.getX(), centro.getY()
    x0 += dx 
    y0 += dy
    bola.move(dx, dy)
    if ((abs(x0)+raio) >= limite):
        dx *= -1
    if ((abs(y0)+raio) >= limite):
        dy *= -1
    update(5) 
    return dx, dy   


def main():
    altura = 400
    largura = 400
    janela = GraphWin("Animation circle bouncing", largura, altura)
    janela.setCoords(-11, -11, 11, 11)

    quadro = Rectangle(Point(-10, -10), Point(10, 10))
    quadro.setFill('white')
    quadro.draw(janela)

    raio = 1
    limite = 10
    x0, y0 = randint(-limite+raio, limite-raio), randint(-limite+raio, limite-raio)
    dx, dy = 1, 1
    bola = Circle(Point(x0, y0), raio)
    bola.setFill('black')
    bola.draw(janela)

    for t in range(1000):
        dx, dy = move_bola(bola, limite, dx, dy)

    p = janela.getMouse()

    janela.close()

if __name__=="__main__":
    main()