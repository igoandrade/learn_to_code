"""
Enunciado:
    16. Write a program to draw a quiz score histogram. Your program should
    read data from a file. Each line of the file contains a number in the range
    0-10. Your program must count the number of occurrences of each score
    and then draw a vertical bar chart with a bar for each possible score (0-
    10) with a height corresponding to the count of that score. For example,
    if 15 students got an 8, then the height of the bar for 8 should be 15.
    Hint: Use a list that stores the count for each possible score.
"""
import math
from graphics import *

def clicou_retangulo(p, p1,  p2):
    x, y = p.getX(), p.getY()
    x_inf=p1.getX() 
    y_inf=p1.getY()
    x_sup=p2.getX()
    y_sup=p2.getY()
    return (x>x_inf and x<x_sup) and (y>y_inf and y<y_sup)


def desenha_quadro(win, p1, p2):
    retangulo = Rectangle(p1, p2)
    retangulo.setFill('white')
    retangulo.draw(win)
    Line(Point(-.5,0), Point(-.5,10)).draw(win)
    Line(Point(-.5,0), Point(-.75, 0)).draw(win)
    Line(Point(-.5,10), Point(-.75, 10)).draw(win)
    for i in range(11):
        Text(Point(i, -.5), f"{i}").draw(win)

def desenha_botao(win, p1, p2, str_texto):
    retangulo = Rectangle(p1, p2)
    pCentro = retangulo.getCenter()
    botao = Text(pCentro, str_texto)
    botao.setStyle("bold")

    retangulo.draw(win)
    botao.draw(win)

def le_arquivo(fileName):
    lista_frequencias = 11 * [0]
    inFile = open(fileName, "r")
    for linha in inFile.readlines():
        num = int(linha.strip())
        try:
            lista_frequencias[num] += 1
        except:
            pass
    return lista_frequencias


def main():
    largura_janela = 600
    altura_janela = 400
    janela = GraphWin("Histogram", largura_janela, altura_janela)
    janela.setCoords(-2.5, -3.0, 12.5, 14.0)

    pt_quadro_1, pt_quadro_2 = Point(-2.0, -1.0), Point(12.0, 11.0)
    desenha_quadro(janela, pt_quadro_1, pt_quadro_2)

    inputLabel = Text(Point(.8, 13.0), "Digite o caminho do arquivo: ")
    inputLabel.setStyle('bold')
    inputLabel.draw(janela)

    inputBox = Entry(Point(3.25, 12.0), 46)
    inputBox.draw(janela)

    pt_ok_1 = Point(9, 11.5)
    pt_ok_2 = Point(12, 12.5)
    desenha_botao(janela, pt_ok_1, pt_ok_2, "OK")

    pt_limpar_1 = Point(-2.0, -2.5)
    pt_limpar_2 = Point(1.0, -1.5)
    desenha_botao(janela, pt_limpar_1, pt_limpar_2, "Limpar")

    pt_sair_1 = Point(9, -2.5)
    pt_sair_2 = Point(12, -1.5)
    desenha_botao(janela, pt_sair_1, pt_sair_2, "Sair")

    sair = False
    while not sair:
        p = janela.getMouse()
        if clicou_retangulo(p, pt_sair_1, pt_sair_2):
            sair = True
        elif clicou_retangulo(p, pt_ok_1, pt_ok_2):
            try:
                fileName = inputBox.getText()
                desenha_quadro(janela, pt_quadro_1, pt_quadro_2)
                frequencia_notas = le_arquivo(fileName)
                total = sum(frequencia_notas)
                escala = math.ceil(10*max(frequencia_notas)/total)
                for i in range(escala+1):
                    y = 10*i/escala
                    Line(Point(-.5,y), Point(-.75, y)).draw(janela)
                    Text(Point(-1.25, y), f"{10*i:>3d} %").draw(janela)
                for n in range(11):
                    if frequencia_notas[n] != 0:
                        altura_barra = 100*frequencia_notas[n]/(escala*total)
                        p1 = Point(n-.25, 0)
                        p2 = Point(n+.25, altura_barra)
                        barra = Rectangle(p1, p2)
                        barra.setFill('lightgrey')
                        barra.draw(janela)
            except:
                pass

        elif clicou_retangulo(p, pt_limpar_1, pt_limpar_2):
            inputBox.setText("")
            desenha_quadro(janela, pt_quadro_1, pt_quadro_2)


    janela.close()

if __name__=="__main__":
    main()