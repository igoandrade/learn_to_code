"""
Programa: exerc_16_fibonacci.py
Autor   : Igo da Costa Andrade
    A Fibonacci sequence is a sequence of numbers where each successive
    number is the sum of the previous two. The classic Fibonacci sequence
    begins: 1, 1, 2, 3, 5, 8, 13, . . .. Write a program that computes the nth
    Fibonacci number where n is a value input by the user. For example, if
    n = 6, then the result is 8.
"""
def fibonacci(n):
    if n==1 or n==2:
        fib=1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
    return fib

def main():
    num_colunas=50
    print(num_colunas*"=")
    print("Este programa calcula o n-ésimo termo da seguência de Fibonacci:\n\t1, 1, 2, 3, 5, 8, 13, ...")
    print(num_colunas*"-")
    n = int(input('Digite n: '))
    while n<=0:
        print('Digite um número maior ou igual a 1.')
        n = int(input('Digite n: '))

    fib = fibonacci(n)
    print(f"O {n}º termo da sequência de Fibonacci é {fib}.")
    print(num_colunas*"=")

if __name__=="__main__":
    main()