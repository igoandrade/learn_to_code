"""
Programa: exerc_11_five_click_house.py
Autor: Igo da Costa Andrade

Enunciado:

"""

from graphics import *

def clicou_retangulo(x,y, x_inf=0.5, y_inf=2, x_sup=9.5, y_sup=9.5):
    return (x>x_inf and x<x_sup) and (y>y_inf and y<y_sup)

def clicou_sair(x,y):
    return clicou_retangulo(x,y, x_inf=5, y_inf=0.5, x_sup=9.5, y_sup=1.5)



def main():
    tela = GraphWin("Five-click House")
    tela.setCoords(0.0, 0.0, 10.0, 10.0)

    botao_sair = Text(Point(7.5, 1), 'Sair')
    botao_sair.draw(tela)
    Rectangle(Point(5,0.5), Point(9.5, 1.5)).draw(tela)

    area_trabalho = Rectangle(Point(0.5,2), Point(9.5, 9.5))
    area_trabalho.setFill('white')
    area_trabalho.draw(tela)


    parede_x1, parede_y1 = pega_coordenadas(tela)
    parede_x2, parede_y2 = pega_coordenadas(tela)

    parede = Rectangle(Point(parede_x1, parede_y1), Point(parede_x2, parede_y2))
    parede.draw(tela)

    largura_parede = parede_x2 - parede_x1
    largura_porta = largura_parede/5
    largura_janela = largura_porta/2

    x3 , y3 = pega_coordenadas(tela)
    while not clicou_retangulo(x3,y3, parede_x1, parede_y1, parede_x2, parede_y2):
        x3 , y3 = pega_coordenadas(tela)
    porta_x1 = x3 - largura_porta/2
    porta_x2 = x3 + largura_porta/2

    while porta_x1 <= parede_x1 or porta_x2 >= parede_x2:
        x3 , y3 = pega_coordenadas(tela)
        while not clicou_retangulo(x3,y3, parede_x1, parede_y1, parede_x2, parede_y2):
            x3 , y3 = pega_coordenadas(tela)
        porta_x1 = x3 - largura_porta/2
        porta_x2 = x3 + largura_porta/2
    
    porta_y1 = parede_y1
    porta_y2 = y3

    porta = Rectangle(Point(porta_x1, porta_y1), Point(porta_x2, porta_y2))
    porta.draw(tela)

    x4 , y4 = pega_coordenadas(tela)


    janela_x1 = x4 - largura_janela/2
    janela_y1 = y4 - largura_janela/2

    janela_x2 = x4 + largura_janela/2
    janela_y2 = y4 + largura_janela/2

    janela_parede = not clicou_retangulo(janela_x1, janela_y1, parede_x1, parede_y1, parede_x2, parede_y2) or not clicou_retangulo(janela_x2, janela_y2, parede_x1, parede_y1, parede_x2, parede_y2)
    janela_porta = clicou_retangulo(janela_x1, janela_y1, porta_x1, porta_y1, porta_x2, porta_y2) or clicou_retangulo(janela_x2, janela_y2, porta_x1, porta_y1, porta_x2, porta_y2)
    while janela_parede or janela_porta:
        x4 , y4 = pega_coordenadas(tela)
        janela_x1 = x4 - largura_janela/2
        janela_y1 = y4 - largura_janela/2

        janela_x2 = x4 + largura_janela/2
        janela_y2 = y4 + largura_janela/2
        janela_parede = not clicou_retangulo(janela_x1, janela_y1, parede_x1, parede_y1, parede_x2, parede_y2) or not clicou_retangulo(janela_x2, janela_y2, parede_x1, parede_y1, parede_x2, parede_y2)
        janela_porta = clicou_retangulo(janela_x1, janela_y1, porta_x1, porta_y1, porta_x2, porta_y2) or clicou_retangulo(janela_x2, janela_y2, porta_x1, porta_y1, porta_x2, porta_y2)



    janela = Rectangle(Point(janela_x1, janela_y1), Point(janela_x2, janela_y2))
    janela.draw(tela)

    x5 , y5 = pega_coordenadas(tela)
    while y5 <= parede_y2 or x5 <=parede_x1 or x5 >= parede_x2:
        x5 , y5 = pega_coordenadas(tela)
    telhado_x1 = x5
    telhado_y1 = y5

    telhado_x2 = parede_x1
    telhado_y2 = parede_y2

    telhado_x3 = parede_x2
    telhado_y3 = parede_y2

    telhado = Polygon(Point(telhado_x1, telhado_y1), Point(telhado_x2, telhado_y2), Point(telhado_x3, telhado_y3))
    telhado.draw(tela)

    tela.getMouse()
    tela.close()

def pega_coordenadas(tela):
    p = tela.getMouse()
    x, y = p.getX(), p.getY()

    while not clicou_retangulo(x,y):
        p = tela.getMouse()
        x, y = p.getX(), p.getY()
    
    return x,y


"""
    pontos_casa = []
    n = 0

    while n < 5:
        p = tela.getMouse()
        x, y = p.getX(), p.getY()
        if clicou_retangulo(x,y):
            pontos_casa.append([x,y])
            n += 1
        elif clicou_sair(x,y):
            tela.close()

    parede_x1 = pontos_casa[0][0]
    parede_y1 = pontos_casa[0][1]

    parede_x2 = pontos_casa[1][0]
    parede_y2 = pontos_casa[1][1]

    largura_parede = parede_x2 - parede_x1
    largura_porta = largura_parede/5
    largura_janela = largura_porta/2

    porta_x1 = pontos_casa[2][0] - largura_porta/2
    porta_y1 = pontos_casa[0][1]

    porta_x2 = pontos_casa[2][0] + largura_porta/2
    porta_y2 = pontos_casa[2][1]

    janela_x1 = pontos_casa[3][0] - largura_janela/2
    janela_y1 = pontos_casa[3][1] - largura_janela/2

    janela_x2 = pontos_casa[3][0] + largura_janela/2
    janela_y2 = pontos_casa[3][1] + largura_janela/2

    telhado_x1 = pontos_casa[4][0]
    telhado_y1 = pontos_casa[4][1]

    telhado_x2 = parede_x1
    telhado_y2 = parede_y2

    telhado_x3 = parede_x2
    telhado_y3 = parede_y2

    parede = Rectangle(Point(parede_x1, parede_y1), Point(parede_x2, parede_y2))
    parede.draw(tela)
    porta = Rectangle(Point(porta_x1, porta_y1), Point(porta_x2, porta_y2))
    porta.draw(tela)
    janela = Rectangle(Point(janela_x1, janela_y1), Point(janela_x2, janela_y2))
    janela.draw(tela)
    telhado = Polygon(Point(telhado_x1, telhado_y1), Point(telhado_x2, telhado_y2), Point(telhado_x3, telhado_y3))
    telhado.draw(tela)

    tela.getMouse()
    tela.close()

"""
        



if __name__=="__main__":
    main()