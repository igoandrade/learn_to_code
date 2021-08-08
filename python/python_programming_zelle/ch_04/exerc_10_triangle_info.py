"""
Programa: exerc_10_triangle_info.py
Autor: Igo da Costa Andrade
Enunciado:
    10. Triangle Information.
        Same as the previous problem, but with three clicks for the vertices of
        a triangle.
        Formulas: For perimeter, see length from the Line Segment problem.
            area = sqrt((s - a)(s - b)(s - c)) where a, b, and c are the lengths of
        the sides and 
            s = (a+b+c)/2
"""

import math
from tkinter import TkVersion
from graphics import *

def clicou_retangulo(p=Point(0,0), x_inf=-9.5, y_inf=-9.5, x_sup=9.5, y_sup=9.5):
    x, y = p.getX(), p.getY()
    return (x>x_inf and x<x_sup) and (y>y_inf and y<y_sup)

def clicou_sair(p=Point(0,0)):
    return clicou_retangulo(p, x_inf=6.5, y_inf=-14.5, x_sup=9.5, y_sup=-13.5)

def clicou_limpar(p=Point(0,0)):
    return clicou_retangulo(p, x_inf=-9.5, y_inf=-14.5, x_sup=-6.5, y_sup=-13.5)

def desenha_ponto(win, p=Point(0,0), desenha=False):
    ponto = Circle(p, .1)
    ponto.setFill('black')
    if desenha:
        ponto.draw(win)
    return ponto

def desenha_triangulo(win, p1=Point(-1,0), p2=Point(1,0), p3=Point(0,1), desenha=False):
    triangulo = Polygon(p1, p2, p3)
    triangulo.setFill('violet')
    if desenha:
        triangulo.draw(win)
    return triangulo


def desenha_area_trabalho(win):
    area_trabalho = Rectangle(Point(-9.5, -9.5), Point(9.5, 9.5))
    area_trabalho.setFill('white')
    area_trabalho.draw(win)

def calcula_comprimento(p1=Point(0,0), p2=Point(0,0)):
    x1, y1, x2, y2 = p1.getX(), p1.getY(), p2.getX(), p2.getY()
    dx = x2 - x1
    dy = y2 - y1
    comprimento = math.sqrt(dx**2 + dy**2)
    return comprimento

def calcula_area(triangulo):
    p1, p2, p3 = triangulo.getPoints()
    a = calcula_comprimento(p1, p2)
    b = calcula_comprimento(p1, p3)
    c = calcula_comprimento(p2, p3)
    s = (a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
    


def main():
    largura_janela = 400
    altura_janela = 500
    janela = GraphWin("Triangle information", largura_janela, altura_janela)
    janela.setCoords(-10.0, -15.0, 10.0, 10.0)

    desenha_area_trabalho(janela)

    botao_sair = Text(Point(8, -14), 'Sair')
    botao_sair.setStyle("bold")
    botao_sair.draw(janela)
    Rectangle(Point(6.5,-14.5), Point(9.5, -13.5)).draw(janela)

    botao_limpar = Text(Point(-8, -14), 'Limpar')
    botao_limpar.setStyle("bold")
    botao_limpar.draw(janela)
    Rectangle(Point(-9.5,-14.5), Point(-6.5, -13.5)).draw(janela)

    perimetro_txt = Text(Point(0, -11), "").draw(janela)
    area_txt = Text(Point(0, -12), "").draw(janela)

    ponto_1 = desenha_ponto(janela)
    ponto_2 = desenha_ponto(janela)
    ponto_3 = desenha_ponto(janela)
    triangulo = desenha_triangulo(janela)

    lista_pontos = []
    sair = False
    while not sair:
        p = janela.getMouse()
        if clicou_sair(p):
            sair = True
        elif clicou_retangulo(p):
            lista_pontos.append(p)
            desenha_ponto(janela, p, True)
        elif clicou_limpar(p):
            ponto_1.undraw()
            ponto_2.undraw()
            ponto_3.undraw()
            triangulo.undraw()
            lista_pontos = []
            desenha_area_trabalho(janela)
            perimetro_txt.setText("")
            area_txt.setText("")
        
        if len(lista_pontos) == 3:
            p1, p2, p3 = lista_pontos
            ponto_1 = desenha_ponto(janela, p1, True)
            ponto_2 = desenha_ponto(janela, p2, True)
            ponto_3 = desenha_ponto(janela, p3, True)
            triangulo = desenha_triangulo(janela, p1, p2, p3, True)

            perimetro = calcula_comprimento(p1,p2) + calcula_comprimento(p2,p3) + calcula_comprimento(p3, p1)
            area = calcula_area(triangulo)
            perimetro_txt.setText("perímetro: " + str (round(perimetro, 3)))
            area_txt.setText("área:     " + str(round(area, 3)))
            lista_pontos = []

        





    janela.close()



if __name__=="__main__":
    main()