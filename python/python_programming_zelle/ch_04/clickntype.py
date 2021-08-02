from graphics import *

def main():
    win = GraphWin("Clique e Digite", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()

        label = Text(pt, key)
        label.draw(win)

main()