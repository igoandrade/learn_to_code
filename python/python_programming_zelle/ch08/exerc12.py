"""
Write a program that graphically plots a regression line-that is, the line
with the best fit through a collection of points. First ask the user to specify
the data points by clicking on them in a graphics window. To find the end
of input, place a small rectangle labeled "Done" in the lower-left comer of
the window; the program will stop gathering points when the user clicks
inside that rectangle.

As the user clicks on points, the program should draw them in the
graphics window and keep track of the count of input values and the running sum of x, y, x2, and xy values. When the user clicks inside the "Done"
rectangle, the program then computes the value of y (using the equations
above) corresponding to the x values at the left and right edges of the
window to compute the endpoints of the regression line spanning the window. Mer the line is drawn, the program will pause for another mouse
click before closing the window and quitting.
"""

from graphics import *

def desenha_eixos(janela, dq):
    Line(Point(-dq,0), Point(dq,0)).draw(janela)
    for i in range(2, dq, 2):
        positivo = Text(Point(i, -.7), f"{i:^3d}")
        positivo.setSize(9)
        positivo.draw(janela)
        Line(Point(i, -.2), Point(i, .2)).draw(janela)
        negativo = Text(Point(-i, -.7), f"{-i:^3d}")
        negativo.setSize(9)
        negativo.draw(janela)
        Line(Point(-i, -.2), Point(-i, .2)).draw(janela)


    Line(Point(0,-dq), Point(0,dq)).draw(janela)
    for i in range(2, dq, 2):
        positivo = Text(Point(-.7,i), f"{i:^3d}")
        positivo.setSize(9)
        positivo.draw(janela)
        Line(Point(-.2, i), Point(.2, i)).draw(janela)
        negativo = Text(Point(-.7, -i), f"{-i:>3d}")
        negativo.setSize(9)
        negativo.draw(janela)
        Line(Point(-.2, -i), Point(.2, -i)).draw(janela)

def desenha_retangulo(janela, Pc, dx, dy, cor="white", texto=""):
    x, y = Pc.getX(), Pc.getY()
    p1 = Point(x-dx, y-dy)
    p2 = Point(x+dx, y+dy)
    retangulo = Rectangle(p1, p2)
    retangulo.setFill(cor)
    retangulo.draw(janela)
    Text(Pc, text=texto).draw(janela)
    return retangulo

def clicou_retangulo(p, retangulo):
    x, y = p.getX(), p.getY()
    p1, p2 = retangulo.getP1(), retangulo.getP2()
    x_min, x_max = min(p1.getX(), p2.getX()), max(p1.getX(), p2.getX())
    y_min, y_max = min(p1.getY(), p2.getY()), max(p1.getY(), p2.getY())
    
    if ((x_min < x < x_max) and (y_min < y < y_max)):
        return True
    else:
        return False

def desenha_ponto(janela, p, size=0.2, cor='black'):
    c = Circle(p, size)
    c.setOutline(cor)
    c.setFill(cor)
    c.draw(janela)

def reta_regressao(X, Y):
    if len(X) != len(Y):
        return None
    else:
        n = len(X)
        x_medio = sum(X)/n
        y_medio = sum(Y)/n
        somaXY = sum([X[i] * Y[i]  for i in range(n)])
        somaXX = sum([X[i] * X[i]  for i in range(n)])
        m = (somaXY - n*x_medio*y_medio)/(somaXX - n*x_medio*x_medio)
    return x_medio, y_medio, m

def desenha_reta_regressao(X,Y, janela, dq, cor="black"):
    x_m, y_m, m = reta_regressao(X, Y)
    x1 = min(X)
    y1 = y_m + m * (x1 - x_m)
    if (y1 < -dq):
        y1 = -dq
        x1 = (y1 - y_m)/m + x_m
    x2 = max(X)
    y2 = y_m + m * (x2 - x_m)
    if (y2 > dq):
        y2 = dq
        x2 = (y2 - y_m)/m + x_m
    p1, p2 = Point(x1, y1), Point(x2, y2)
    reta = Line(p1, p2)
    reta.setFill(cor)
    reta.draw(janela)


def main():
    dq = 11
    Pc = Point(0,0)
    largura, altura = 500, 400
    titulo = "Reta de Regressão por Mínimos Quadrados"
    janela = GraphWin(title=titulo, width=largura, height=altura)

    dy = 15
    fator = altura / dy
    dx = largura / fator

    y_min, y_max = -dy, +dy
    x_min, x_max = -dq-1, 2*dx-dq-1
    janela.setCoords(x_min, y_min, x_max, y_max)

    
    quadro_branco = desenha_retangulo(janela, Pc, dx=dq, dy=dq)
    desenha_eixos(janela, dq)



    dx_sair, dy_sair = 3, 1
    x_sair, y_sair = dq-dx_sair, -dy+2*dy_sair
    p_sair = Point(x_sair, y_sair)
    btn_sair = desenha_retangulo(janela, p_sair, dx_sair, dy_sair, cor='LightGray', texto="Sair")

    dx_limpar, dy_limpar = 3, 1
    x_limpar, y_limpar = 0, -dy+2*dy_limpar
    p_limpar = Point(x_limpar, y_limpar)
    btn_limpar = desenha_retangulo(janela, p_limpar, dx_limpar, dy_limpar, cor='LightGray', texto="Limpar")

    dx_plotar, dy_plotar = 3, 1
    x_plotar, y_plotar = -dq+dx_plotar, -dy+2*dy_plotar
    p_plotar = Point(x_plotar, y_plotar)
    btn_plotar = desenha_retangulo(janela, p_plotar, dx_plotar, dy_plotar, cor='LightGray', texto="Plotar")

    equacao = Text(Point(dq + .5*(x_max-dq), dq-1), "")
    equacao.draw(janela)

    p = Point(0,0)
    X = []
    Y = []
    while True:
        p = janela.getMouse()
        if clicou_retangulo(p, btn_sair):
            break
        if clicou_retangulo(p, btn_limpar):
            quadro_branco = desenha_retangulo(janela, Pc, dx=dq, dy=dq)
            desenha_eixos(janela, dq)
            equacao.setText("")
            X = []
            Y = []
        if (clicou_retangulo(p, btn_plotar) and len(X) > 1):
            desenha_reta_regressao(X, Y, janela, dq)
            x_m, y_m, m = reta_regressao(X, Y)
            if x_m >= 0:
                str_x_m = f" + {x_m:.1f}"
            else:
                str_x_m = f" - {abs(x_m):.1f}"
            if y_m >= 0:
                str_y_m = f" + {y_m:.1f}"
            else:
                str_y_m = f"{y_m:.1f}"
            if m >= 0:
                str_m = f" + {m:.1f}"
            else:
                str_m = f" - {abs(m):.1f}"
            equacao.setText(f"y = {str_y_m}{str_m}(x{str_x_m})")
            X = []
            Y = []
        if clicou_retangulo(p, quadro_branco):
            if len(X)==0:
                quadro_branco = desenha_retangulo(janela, Pc, dx=dq, dy=dq)
                desenha_eixos(janela, dq) 
                equacao.setText("")               
            X.append(p.getX())
            Y.append(p.getY())
            desenha_ponto(janela, p, size=.18, cor="red")
    janela.close()



    






if __name__=="__main__":
    main()