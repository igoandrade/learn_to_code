"""
Programa: exerc_06_slope.py
Autor   : Igo da Costa Andrade
    Two points in a plane are specified using the coordinates (x1,y1) and
    (x2,y2). Write a program that calculates the slope of a line through two
    (non-vertical) points entered by the user.

    slope = (y2-y1)/(x2-x1)
"""

def calcula_slope(x1, y1, x2, y2):
    try:
        slope = (y2-y1)/(x2-x1)
        return slope
    except ZeroDivisionError:
        print(f"Os pontos ({x1}, {y1}) e ({x2}, {y2}) estão sobre uma reta vertical.")
        return None

def main():
    num_colunas = 50
    print(num_colunas*"=")
    x1, y1 = tuple(float(num) for num in input("Digite as coordenadas do ponto (x1, y1): ").split(','))
    x2, y2 = tuple(float(num) for num in input("Digite as coordenadas do ponto (x2, y2): ").split(','))
    slope = calcula_slope(x1, y1, x2, y2)
    print(num_colunas*"-")
    if slope != None:
        print(f"slope = {slope:.2f}")
    print(num_colunas*"=")


if __name__=="__main__":
    main()