""""
Programa: exerc_07_circle_intersertion.py
Autor: Igo da Costa Andrade

Enunciado:
    7. Circle Intersection.
    Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
        Input: Radius of the circle and they-intercept of the line.
        Output: Draw a circle centered at (0, 0) with the given radius in a window
        with coordinates running from -10,-10 to 10,10.
        Draw a horizontal line across the window with the giveny-intercept.
        Draw the two points of intersection in red.
        Print out the x values of the points of intersection.
        Formula: x = +/- sqrt(r**2 - y**2)
"""

from graphics import *
import math

def desenha_inputText(janela, texto, pos_x=-5, pos_y=9, largura=4, dx=2):
    inputText = Text(Point(pos_x,pos_y), f"{texto:<10s}").draw(janela)
    inputText = Entry(Point(pos_x+dx, pos_y), largura)
    inputText.setText('0.0')
    inputText.draw(janela)    
    return inputText

def calcula_intersecao(raio, y):
    d = raio**2 - y**2
    if d>0:
        x1 = -math.sqrt(d)
        x2 = +math.sqrt(d)
        return x1, x2
    elif d==0:
        return 0
    else:
        print("Não existem pontos de intersecção.")
        return None



def main():
    largura_janela = 400
    altura_janela = 400
    janela = GraphWin("Circle Intersection", largura_janela, altura_janela)
    janela.setCoords(-10.0, -10.0, 10.0, 10.0)

    inputText_raio = desenha_inputText(janela, texto='Raio r:', pos_x=-8, pos_y=9, largura=3, dx=2)
    inputText_ordenada = desenha_inputText(janela, texto='Ordenada y:', pos_x=-2, pos_y=9, largura=3, dx=3.25)

    botao_inserir_dados = Text(Point(6, 9), 'Inserir Dados')
    botao_inserir_dados.draw(janela)
    Rectangle(Point(3,8.5), Point(9, 9.5)).draw(janela)

    botao_sair = Text(Point(7, -9), 'Sair')
    botao_sair.draw(janela)
    Rectangle(Point(6,-9.5), Point(8, -8.5)).draw(janela)

    label = Text(Point(-3,-9), "")
    label.draw(janela)

    p = janela.getMouse()
    x, y = p.getX(), p.getY()
    clicou_inserir_dados = (x>3 and x<9) and (y>8.5 and y<9.5)
    clicou_sair = (x>6 and x<8) and (y>-9.5 and y<-8.5)

    while not(clicou_inserir_dados) and not(clicou_sair):
        p = janela.getMouse()
        x, y = p.getX(), p.getY()
        clicou_inserir_dados = (x>3 and x<9) and (y>8.5 and y<9.5)
        clicou_sair = (x>6 and x<8) and (y>-9.5 and y<-8.5)
    circ = Circle(Point(0,0), 0)
    linha = Line(Point(0,0), Point(1,1))
    P = Circle(Point(0,0), .2)
    P1 = Circle(Point(0,0), .2)
    P2 = Circle(Point(0,0), .2)
    while (clicou_inserir_dados) or not(clicou_sair):
        if (clicou_inserir_dados):
            circ.undraw()
            linha.undraw()
            P.undraw()
            P1.undraw()
            P2.undraw()
            label.setText("")

            raio = float(inputText_raio.getText())
            y = float(inputText_ordenada.getText())

            circ = Circle(Point(0,0), raio)
            circ.draw(janela)

            linha = Line(Point(-9, y), Point(9, y))
            linha.draw(janela)

            d = raio**2 - y**2
            if d>0:
                x1 = -math.sqrt(d)
                x2 = math.sqrt(d)
                P1 = Circle(Point(x1, y), .2)
                P1.setFill('red')
                P1.setOutline('red')
                P1.draw(janela)
                
                P2 = Circle(Point(x2, y), .2)
                P2.setFill('red')
                P2.setOutline('red')
                P2.draw(janela)
                label.setText(f"Intersecção: x1 = {x1:5.1f} e x2 = {x2:4.1f}")   
            elif d==0:
                x = 0
                P = Circle(Point(x, y), .2)
                P.setFill('red')
                P.setOutline('red')
                P.draw(janela)
                label.setText(f"Intersecção: x = {x:5.1f}")   
            else:
                label.setText("Não existem pontos de intersecção")

        p = janela.getMouse()
        x, y = p.getX(), p.getY()
        clicou_inserir_dados = (x>3 and x<9) and (y>8.5 and y<9.5)
        clicou_sair = (x>6 and x<8) and (y>-9.5 and y<-8.5)
    
    if clicou_sair:
        janela.close()



if __name__=="__main__":
    main()