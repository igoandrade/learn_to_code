"""
Programa: exerc_08.py
Autor: Igo da Costa Andrade
Enunciado:
    8. Line Segment Information.
    This program allows the user to draw a line segment and then displays
    some graphical and textual information about the line segment.
        Input: Two mouse clicks for the end points of the line segment.
        Output: Draw the midpoint of the segment in cyan.
            Draw the line.
            Print the length and the slope of the line.
        Formulas:  
            dx = x2 - x1
            dy = y2 -y1
            slope = dy/dx
            length = sqrt(dx**2 + dy**2)
"""

import math
from graphics import *

def main():
    largura_janela = 400
    altura_janela = 400
    janela = GraphWin("Line Segment Information", largura_janela, altura_janela)
    janela.setCoords(-10.0, -10.0, 10.0, 10.0)

    botao_limpar_tela = Text(Point(-5, -9), 'Limpar')
    botao_limpar_tela.draw(janela)
    Rectangle(Point(-7,-9.5), Point(-3, -8.5)).draw(janela)

    botao_sair = Text(Point(5, -9), 'Sair')
    botao_sair.draw(janela)
    Rectangle(Point(3.5,-9.5), Point(6.5, -8.5)).draw(janela)

    area_trabalho = Rectangle(Point(-9.5,-7), Point(9.5, 9.5))
    area_trabalho.setFill('white')
    area_trabalho.draw(janela)

    slope_txt = Text(Point(-7, -7.5), f"{'Slope: ':<15s}").draw(janela)
    len_txt = Text(Point(0, -7.5), f"{'Length: ':>15s}").draw(janela)



    continua_programa = True
    while continua_programa:
        p1 = janela.getMouse()
        x1, y1 = p1.getX(), p1.getY()
        if (clicou_sair(x1,y1)):
            continua_programa = False
        else:
            p2 = janela.getMouse()
            x2, y2 = p2.getX(), p2.getY()
            if (clicou_sair(x2,y2)):
                continua_programa = False
        
        if clicou_retangulo(x1,y1) and clicou_retangulo(x2,y2):
            linha = Line(p1, p2)
            linha.draw(janela)

            x_medio, y_medio = (x1+x2)/2, (y1+y2)/2
            p_medio = Circle(Point(x_medio, y_medio), .3)
            p_medio.setFill('cyan')
            p_medio.draw(janela)
            
            dx, dy = x2 - x1, y2 - y1
            if dx != 0:
                slope = dy/dx
                txt = "Slope: " + str(round(slope, 1)) 
            else:
                txt = 'Slope: INF'
            slope_txt.setText(f"{txt:<15s}")

            length = math.sqrt(dx**2 + dy**2)
            txt = "Length: " + str(round(length, 1))
            len_txt.setText(f"{txt:>15s}")
   
    janela.close()


def clicou_retangulo(x,y, x_inf=-9.5, y_inf=-7, x_sup=9.5, y_sup=9.5):
    return (x>x_inf and x<x_sup) and (y>y_inf and y<y_sup)

def clicou_sair(x,y):
    return clicou_retangulo(x,y, x_inf=3.5, y_inf=-9.5, x_sup=6.5, y_sup=-8.5)

def clicou_limpar(x,y):
    return clicou_retangulo(x,y, x_inf=-7, y_inf=-9.5, x_sup=-3, y_sup=-8.5)




if __name__=="__main__":
    main()