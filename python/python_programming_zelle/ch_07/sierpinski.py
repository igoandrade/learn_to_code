from tkinter.constants import VERTICAL
from graphics import *
from math import sqrt
import random

def desenha_retangulo(janela, cx=0, cy=0, dx=3, dy=1, cor='white', texto=''):
    p0 = Point(cx, cy)
    p1 = Point(cx-dx, cy-dy)
    p2 = Point(cx+dx, cy+dy)
    retangulo = Rectangle(p1, p2)
    retangulo.setFill(cor)
    retangulo.draw(janela)
    Text(p0, texto).draw(janela)
    return retangulo

def clicou_retangulo(p, retangulo):
    x, y = p.getX(), p.getY()
    C = retangulo.getCenter()
    cx, cy = C.getX(), C.getY()
    p1, p2 = retangulo.getP1(), retangulo.getP2()
    x1, x2 = min(p1.getX(), p2.getX()), max(p1.getX(), p2.getX())
    y1, y2 = min(p1.getY(), p2.getY()), max(p1.getY(), p2.getY())
    if ((x1 < x < x2) and (y1 < y < y2)):
        return True
    else:
        return False

def clicou_sair(janela, p, btn_sair):
    if (clicou_retangulo(p, btn_sair)):
        janela.close()


def criar_triangulo(janela, cx=0, cy=0, dx_quadro=20, dy_quadro=20):
    lado = min(dx_quadro, 2*sqrt(3)*(dy_quadro)/2) - 2
    altura = lado * sqrt(3)/2
    x1, y1 = cx-lado/2, cy-altura/2
    x2, y2 = cx+lado/2, cy-altura/2
    x3, y3 = 0, cy+altura/2

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    x, y = x1, y1
    vertices = [p1, p2, p3]
    for i in range(10000):
        v = random.choice(vertices)
        vx, vy = v.getX(), v.getY()
        x = (x+vx)/2
        y = (y+vy)/2
        p = Point(x,y)
        c = Circle(p, 0.00001)
        if (y < altura/2):
            if (x < lado/2):
                c.setFill('green')
                c.setOutline('green')
            else:
                c.setFill('red')
                c.setOutline('red')  
        else:
            c.setFill('blue')
            c.setOutline('blue')
        c.draw(janela)   



def criar_tapete(janela, cx=0, cy=0, dx_quadro=20, dy_quadro=20):
    lado = 0.9 * min(dx_quadro, dy_quadro)
    x1, y1 = cx-lado/2, cy-lado/2
    x2, y2 = cx+lado/2, cy-lado/2
    x3, y3 = cx+lado/2, cy+lado/2
    x4, y4 = cx-lado/2, cy+lado/2
    

    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    p3 = Point(x3,y3)
    p4 = Point(x4,y4)

    vertices = [p1, p2, p3, p4]
    Polygon(vertices).draw(janela)
    x, y = x1, y1
    for i in range(10000):
        v = random.choice(vertices)
        vx, vy = v.getX(), v.getY()
        x = (x+vx)/3
        y = (y+vy)/3
        p = Point(x,y)
        c = Circle(p, 0.00001)
        c.setFill('black')
        c.draw(janela)

def main():
    altura, largura = 560, 480
    janela = GraphWin("Fractais de Sierpinski", largura, altura)
    janela.setCoords(-11, -14, 11, 11)

    quadro = desenha_retangulo(janela, dx=10, dy=10, cor='white', texto='')
    btn_triangulo = desenha_retangulo(janela, cx=-8, cy=-12, dx=2, dy=1, cor='LightGray', texto='Triângulo')
    btn_tapete = desenha_retangulo(janela, cx=-3, cy=-12, dx=2, dy=1, cor='LightGray', texto='Tapete')
    btn_limpar = desenha_retangulo(janela, cx=3, cy=-12, dx=2, dy=1, cor='LightGray', texto='Limpar')
    btn_sair = desenha_retangulo(janela, cx=8, cy=-12, dx=2, dy=1, cor='LightGray', texto='Sair')

    try:
        p = janela.getMouse()
        while (not clicou_retangulo(p, btn_sair)):
            if (clicou_retangulo(p, btn_triangulo)):
                quadro = desenha_retangulo(janela, dx=10, dy=10, cor='white', texto='')
                criar_triangulo(janela, cx=0, cy=0, dx_quadro=20, dy_quadro=20)
            elif (clicou_retangulo(p, btn_tapete)):
                quadro = desenha_retangulo(janela, dx=10, dy=10, cor='white', texto='')
                criar_tapete(janela, cx=0, cy=0, dx_quadro=20, dy_quadro=20)
            elif (clicou_retangulo(p, btn_limpar)):
                quadro = desenha_retangulo(janela, dx=10, dy=10, cor='white', texto='')
            p = janela.getMouse()
        janela.close()
    except:
        pass


if __name__=="__main__":
    main()