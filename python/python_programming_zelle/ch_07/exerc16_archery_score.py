"""
Archery Scorer. Write a program that draws an archery target (see Programming Exercise 2 from Chapter 4) and allow the user to click five times to represent arrows shot at the target. Using five-band scoring, a bulls-eye (yellow) is worth 9 points and each ring is worth 2 fewer points down to 1 for white. The program should output a score for each click and keep track of a running sum for the entire series.
"""

from graphics import *

def desenha_retangulo(janela, cx, cy, dx, dy, cor_fundo="white", cor_borda="black", texto=""):
    p1 = Point(cx-dx, cy-dy)
    p2 = Point(cx+dx, cy+dy)
    retangulo = Rectangle(p1, p2)
    retangulo.setFill(cor_fundo)
    retangulo.setOutline(cor_borda)
    retangulo.draw(janela)
    centro = retangulo.getCenter()
    Text(centro, texto).draw(janela)
    return retangulo

def desenha_alvo(janela, raio, cores):
    centro = Point(0,0)
    dr = raio / len(cores)
    for cor in cores:
        circulo = Circle(centro, raio)
        circulo.setFill(cor)
        circulo.draw(janela)
        raio -= dr

def calcula_pontos(p, raio_alvo, num_setores):
    dr = raio_alvo / num_setores
    pontos = 0
    x, y = p.getX(), p.getY()
    d = (x**2 + y**2)**0.5
    for i in range(num_setores):
        if (d >= i * dr and d < (i+1)*dr):
            pontos = 9 - 2*i
            break
    return pontos

def clicou_retangulo(p, retangulo):
    x, y = p.getX(), p.getY()
    p1, p2 = retangulo.getP1(), retangulo.getP2()
    x1, x2 = min(p1.getX(), p2.getX()), max(p1.getX(), p2.getX())
    y1, y2 = min(p1.getY(), p2.getY()), max(p1.getY(), p2.getY())
    if ((x1 < x and x < x2) and (y1 < y and y < y2)):
        return True
    else:
        return False


def main():
    largura_tela = 300
    altura_tela = 400
    
    janela = GraphWin("Archery Scorer", largura_tela, altura_tela)
    janela.setCoords(-12, -20, 12, 12)
    
    quadro_branco = desenha_retangulo(janela, cx=0, cy=0, dx=11, dy=11, cor_fundo="white", cor_borda="black", texto="")

    posY_linha = -12
    for i in range(3):
        p1 = Point(-11, posY_linha)
        p2 = Point(11, posY_linha)
        Line(p1, p2).draw(janela)
        posY_linha -= 2

    Text(Point(-8,-13), "Jogada").draw(janela)
    Text(Point(-8,-15), "Pontos").draw(janela)
    for i in range(5):
        Text(Point(-4+2*i,-13), str(i+1)+"ª").draw(janela)
    Text(Point(8,-13), "Total").draw(janela)
    label_p1 = Text(Point(-4,-15), "").draw(janela)
    label_p2 = Text(Point(-2,-15), "").draw(janela)
    label_p3 = Text(Point(+0,-15), "").draw(janela)
    label_p4 = Text(Point(+2,-15), "").draw(janela)
    label_p5 = Text(Point(+4,-15), "").draw(janela)
    label_total = Text(Point(+8,-15), "0").draw(janela)
    labels = [label_p1, label_p2, label_p3, label_p4, label_p5, label_total]

    btn_sair = desenha_retangulo(janela, cx=8, cy=-18, dx=3, dy=1, cor_fundo="LightGrey", cor_borda="black", texto="Sair")
    btn_limpar = desenha_retangulo(janela, cx=-8, cy=-18, dx=3, dy=1, cor_fundo="LightGrey", cor_borda="black", texto="Limpar")

    raio_alvo = 10
    cores = ['yellow', 'red', 'blue', 'black', 'white']
    num_setores = len(cores)
    desenha_alvo(janela, raio_alvo, cores)

    n = 0
    total_pontos = 0
    sair = False
    while (not sair):
        p = janela.getMouse()

        if (clicou_retangulo(p, quadro_branco)):
            if (n < 5):
                pontos = calcula_pontos(p, raio_alvo, num_setores)
                total_pontos += pontos
                labels[n].setText(str(pontos))
                labels[-1].setText(str(total_pontos))
                n += 1
        elif (clicou_retangulo(p, btn_limpar)):
            n = 0
            total_pontos = 0
            for i in range(6):
                labels[i].setText('')
        elif (clicou_retangulo(p, btn_sair)):
            sair = True

    janela.close()

if __name__=="__main__":
    main()