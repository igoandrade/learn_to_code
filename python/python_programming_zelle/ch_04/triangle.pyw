from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Clique em três pontos")
    message.draw(win)

    # Obter e desenhar os três vértices do triângulo
    vertices = []
    for i in range(3):
        p = win.getMouse()
        p.draw(win)
        vertices.append(p)
    p1, p2, p3 = vertices

    triangulo = Polygon(p1, p2, p3)
    triangulo.setFill('peachpuff')
    triangulo.setOutline('cyan')
    triangulo.draw(win)

    message.setText("Clique aqui para sair.")
    win.getMouse()

main()