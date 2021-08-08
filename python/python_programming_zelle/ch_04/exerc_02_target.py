""""
Programa: exerc_02_target.py
Autor: Igo da Costa Andrade
Enunciado:
    2. An archery target consists of a central circle of yellow surrounded by concentric rings of red, blue, black and white. Each ring has the same width,
    which is the same as the radius of the yellow circle. Write a program
    that draws such a target. Hint: Objects drawn later will appear on top of
    objects drawn earlier
"""

from graphics import *

def main():
    largura_janela = 320
    altura_janela = 240
    janela = GraphWin("Tiro ao alvo", largura_janela, altura_janela)
    #janela.setCoords(0.0, 0.0, 4.0, 3.0)
    
    x_centro = largura_janela/2
    y_centro = altura_janela/2
    centro = Point(x_centro, y_centro)
    cores = ['yellow', 'red', 'blue', 'black', 'white']
    cores.reverse()
    qtd_circulos = len(cores)
    raio = .8 * min(largura_janela, altura_janela) / 2
    dr = raio / qtd_circulos

    for cor in cores:
        circulo = Circle(centro, raio)
        circulo.setFill(cor)
        circulo.setOutline(cor)
        circulo.draw(janela)
        raio -= dr
    
    janela.getMouse()
    janela.close()

if __name__=="__main__":
    main()