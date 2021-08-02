"""
Programa: exerc_04_winter_scene.py
Autor: Igo da Costa Andrade
Enunciado:
    4. Write a program that draws a winter scene with a Christmas tree and a snowman.
"""

from graphics import *

def main():
    largura_janela = 320
    altura_janela = 240
    janela = GraphWin("Winter Scene", largura_janela, altura_janela)
    janela.setCoords(0.0, 0.0, 4.0, 3.0)

    x0 = 1.
    y0 = .5
    d = .7
    h = 1
    tronco = Polygon(Point(x0-.2*d, y0), Point(x0+.2*d, y0), Point(x0+.4*d, y0-.5*h), Point(x0-.4*d, y0-.5*h))
    tronco.setFill('brown')
    tronco.setOutline('brown')
    tronco.draw(janela)
    for i in range(3):
        P1 = Point(x0 - d, y0)
        P2 = Point(x0 + d, y0)
        P3 = Point(x0, y0 + h)
        y0 += .7 * h
        d *= 0.7
        h *= .7
        copa = Polygon(P1, P2, P3)
        copa.setFill('green')
        copa.setOutline('green')
        copa.draw(janela)

    
    x0 = 2
    y0 = .5
    raio = y0
    escala = 0.7
    for i in range(2):
        circ = Circle(Point(x0,y0), raio)
        circ.setFill('white')
        circ.setOutline('gray')
        circ.draw(janela)
        raio *= escala
        y0 += 2*raio
    
    nariz = Circle(circ.getCenter(), .15 * circ.getRadius())
    nariz.setFill('orange')
    nariz.draw(janela)

    olho_direito = nariz.clone()
    olho_direito.setFill('black')
    olho_direito.move(.12,.12)
    olho_direito.draw(janela)

    olho_esquerdo = nariz.clone()
    olho_esquerdo.setFill('black')
    olho_esquerdo.move(-.12,.12)
    olho_esquerdo.draw(janela)






    janela.getMouse()
    janela.close()

if __name__=="__main__":
    main()