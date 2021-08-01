"""
Programa: exerc_15_pi.py
Autor   : Igo da Costa Andrade
    Write a program that approximates the value of pi by summing the terms
    of this series: 4/1- 4/3+4/5- 4/7+4/9- 4/11+. . . The program should
    prompt the user for n, the number of terms to sum, and then output the
    sum of the first n terms of this series. Have your program subtract the
    approximation from the value of math.pi to see how accurate it is.
"""

import math

def aproxima_pi(n):
    soma_pi = 0
    for i in range(1,n+1):
        denominador = 2*i-1
        soma_pi += 4/denominador * (-1)**(i-1)
    return soma_pi


def main():
    num_colunas=80
    print(num_colunas*"=")
    print("Este programa calcula o valor aproximado de pi (3.14...) por meio de série:\n\t4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...")
    print(num_colunas*"-")
    n = int(input("Digite a quantidade de termos da série\nn: "))
    pi_aprox = aproxima_pi(n)
    pi_exato = math.pi
    erro = abs(pi_exato - pi_aprox)
    erro_rel = erro/pi_exato * 100
    print(f"{'n':>3s} | {'Pi aproximado':>15s} | {'Pi exato':>15s} | {'Erro Abs.':>9s} | {'Erro Rel. (%)':>13s}")
    print(f"{n:>3d} | {pi_aprox:>15.13f} | {pi_exato:>15.13f} | {erro:>9.4f} | {erro_rel:>13.4f}")
    print(num_colunas*"=")

if __name__=="__main__":
    main()