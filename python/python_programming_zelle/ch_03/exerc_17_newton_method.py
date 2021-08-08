"""
Programa: exerc_17_newton_method.py
Autor: Igo da Ccsta Andrade

    You have seen that the math library contains a function that computes
    the square root of numbers. In this exercise, you are to write your own
    algorithm for computing square roots. One way to solve this problem
    is to use a guess-and-check approach. You first guess what the square
    root might be, and then see how close your guess is. You can use this
    information to make another guess and continue guessing until you have
    found the square root (or a close approximation to it). One particularly
    good way of making guesses is to use Newton's method. Suppose x is the
    number we want the root of, and guess is the current guessed answer. The
    guess can be improved by using computing the next guess as:

        (guess + x/guess)/2

    Write a program that implements Newton's method. The program
    should prompt the user for the value to find the square root of (x) and
    the number of times to improve the guess. Starting with a guess value
    of x/2, your program should loop the specified number of times applying
    Newton's method and report the final value of guess. You should also
    subtract your estimate from the value of math.sqrt (x) to show how close
    it is.
"""

import math

def newton_sqrt(x, n):
    raiz = x/2
    if n==0:
        pass
    else:
        for i in range(n):
            raiz = (raiz + x/raiz)/2
    return raiz


def main():
    num_colunas=80
    print(num_colunas*'=')
    print('Este programa aplica o método de Newton para\ncalcular a raiz quadrada de um número real x.')
    print(num_colunas*'-')
    x = float(input("Digite o valor do número cuja raiz quadrada vc quer saber.\n\tx: "))
    n = int(input("Digite a quantidade de iterações do programa.\n\tn: "))
    raiz_aprox = newton_sqrt(x,n)
    raiz_exata = math.sqrt(x)
    erro = abs(raiz_aprox - raiz_exata)
    erro_rel = erro/raiz_exata * 100
    print(f"{'n':>3s} | {'Raiz aproximada':>15s} | {'Raiz exata':>15} | {'Erro Abs.':>13s} | {'Erro Rel. (%)':>13s}")
    print(f"{n:>3d} | {raiz_aprox:>15.10f} | {raiz_exata:>15.10f} | {erro:>13.8f} | {erro_rel:>13.8f}")
    print(num_colunas*'=')


if __name__=='__main__':
    main()