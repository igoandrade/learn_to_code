
from graphics import *
import cmath
import math

def raiz_complexa(z, n):
    rho, theta = cmath.polar(z)
    raizes = []
    for k in range(n):
        raiz = rho**(1/n) * complex(math.cos((theta + 2*k*math.pi)/n), math.sin((theta + 2*k*math.pi)/n))
        raizes.append(raiz)
    return raizes

def desenha_eixo(janela, p1, p2, tipo = "x", passo = 1, label = "x"):
    tipo = tipo.lower()
    if tipo not in ['x', 'y']:
        print("Erro")
        return None
    elif tipo == 'x':
        l_inf, l_sup = min(p1.getX(), p2.getX()), max(p1.getX(), p2.getX())
    else:
        l_inf, l_sup = min(p1.getY(), p2.getY()), max(p1.getY(), p2.getY())
    eixo = Line(p1, p2)
    eixo.setArrow('last')
    eixo.draw(janela)               
    if tipo == 'x':
        Text(Point(l_sup+.1, -.15), label).draw(janela)
    else:
        Text(Point(.3, l_sup), label).draw(janela)

def main():
    janela = GraphWin("Raízes complexas", 400, 400)
    janela.setBackground('white')
    janela.setCoords(-2, -2, 2, 2)

    desenha_eixo(janela, Point(-1.5,0), Point(1.5,0), tipo='x', label="Re (z)")
    Text(Point(1.1, -.15), "+1").draw(janela)
    Text(Point(-1.1, -.15), "-1").draw(janela)
    desenha_eixo(janela, Point(0,-1.5), Point(0,1.5), tipo='y', label="Im (z)")

    circ = Circle(Point(0,0), 1).draw(janela)

    raizes = raiz_complexa(1, 6)
    for r in raizes:
        x, y = r.real, r.imag
        p = Point(x,y)
        circ = Circle(p, .05)
        circ.setFill('blue')
        circ.setOutline('blue')
        circ.draw(janela)


    p = janela.getMouse()
    janela.close()

if __name__=="__main__":
    main()
