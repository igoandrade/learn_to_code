"""
Programa: exerc_15_plot_scores.py
Autor: Igo da Costa Andrade
Enunciado: 
    15. Write a program to plot a horizontal bar chart of student exam scores.
    Your program should get input from a file. The first line of the file contains
    the count of the number of students in the file, and each subsequent line
    contains a student's last name followed by a score in the range 0-100.
    Your program should draw a horizontal rectangle for each student where
    the length of the bar represents the student's score. The bars should all
    line up on their left-hand edges. Hint: Use the number of students to
    determine the size of the window and its coordinates. Bonus: label the
    bars at the left end with the students' names.
"""

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
    Line(Point(0, 1.0), Point(10, 1.0)).draw(win)
    for i in range(0,11,2):
        Line(Point(i, 1.0), Point(i, .75)).draw(win)
        Text(Point(i, .5), f"{i}").draw(win)


def main():
    largura_tela = 400
    altura_tela = 500
    janela = GraphWin("Bar Chart of Student Exam Scores", largura_tela, altura_tela)
    janela.setCoords(-6.5, 12, 12.5, -2.5)

    inputTXT = Text(Point(-1.75, -2), "Caminho do arquivo: ")
    inputTXT.setStyle('bold')
    inputTXT.draw(janela)

    desenha_quadro(janela, Point(-6.0, 0.0), Point(12.0, 10.0))

    inputBox = Entry(Point(1.25, -1.0), 32)
    inputBox.draw(janela)

    botao_ok = Text(Point(10.5, -1.0), 'OK')
    botao_ok.setStyle("bold")
    botao_ok.draw(janela)
    pt_ok_1 = Point(9, -1.3)
    pt_ok_2 = Point(12, -.7)
    Rectangle(pt_ok_1, pt_ok_2).draw(janela)

    botao_limpar = Text(Point(-4.5, 11), 'Limpar')
    botao_limpar.setStyle("bold")
    botao_limpar.draw(janela)
    pt_limpar_1 = Point(-6, 10.7)
    pt_limpar_2 = Point(-3, 11.3)
    Rectangle(pt_limpar_1, pt_limpar_2).draw(janela)

    botao_sair = Text(Point(10.5, 11), 'Sair')
    botao_sair.setStyle("bold")
    botao_sair.draw(janela)
    pt_sair_1 = Point(9, 10.7)
    pt_sair_2 = Point(12, 11.3)
    Rectangle(pt_sair_1, pt_sair_2).draw(janela)

    
    
    sair = False
    while not sair:
        p = janela.getMouse()
        if clicou_retangulo(p, pt_sair_1, pt_sair_2):
            sair = True
        elif clicou_retangulo(p, pt_ok_1, pt_ok_2):
            fileName = inputBox.getText()
            try:
                inFile = open(fileName, "r")
                desenha_quadro(janela, Point(-6.0, 0.0), Point(12.0, 10.0))
                y_notas = 1.5
                x_notas = -3
                for linha in inFile.readlines()[1:]:
                    aluno, nota = linha.split()
                    aluno = aluno.strip().capitalize()
                    nota = float(nota)
                    alunoTXT = Text(Point(x_notas, y_notas), f"{aluno:<10s}")
                    alunoTXT.setStyle('bold')
                    alunoTXT.draw(janela)
                    notaRetangulo = Rectangle(Point(0, y_notas-.25), Point(nota/10, y_notas+.25))
                    notaRetangulo.setFill('gray')
                    notaRetangulo.draw(janela)
                    y_notas += .75
                inFile.close()
            except:
                pass
        elif clicou_retangulo(p, pt_limpar_1, pt_limpar_2):
            inputBox.setText("")
            desenha_quadro(janela, Point(-6.0, 0.0), Point(12.0, 10.0))



    janela.close()



if __name__=="__main__":
    main()