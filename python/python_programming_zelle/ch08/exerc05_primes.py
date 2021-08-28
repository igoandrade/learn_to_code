"""
A positive whole number n > 2 is prime if no number between 2 and sqrt(n)
(inclusive) evenly divides n. Write a program that accepts a value of n as
input and determines if the value is prime. If n is not prime, your program
should quit as soon as it finds a value that evenly divides n.
"""


def is_prime(n):
    if n < 2:
        return False
    lim = round(n**.5)
    for i in range(2, lim + 1):
        if n % i == 0:
            return False
    return True

def fatores_primos(n):
    lim = round(n**.5)
    fatores = []
    f = 2
    p = 0
    while (n > 1 and f <= lim + 1):
        if (is_prime(f) and n % f == 0):
            while (n % f == 0):
                n /= f
                p += 1
        if (p > 0):
            fatores.append([f, p])
        f += 1
        p = 0
            
    return fatores


def main():
    print()
    print(" Números Primos ".center(50, "=").center(52, "*"))
    n = int(input("Digite um número inteiro maior que 1: "))
    while (n < 2):
        print("\nOps! Entrada inválida!")
        n = int(input("Digite um número inteiro maior que 1: "))
    print(52 * "-")
    if is_prime(n):
        print(f"O número {n} é primo.")
    else:
        print(f"O número {n} não é primo.")
        fatoracao = f"{n} = "
        fatores = fatores_primos(n)
        for fator in fatores:
            if fator[1] == 1:
                fatoracao += f"{fator[0]}"
            else:
                fatoracao += f"({fator[0]}^{fator[1]})"

            if fator != fatores[-1]:
                fatoracao += " x "
        print(fatoracao)
    print(52 * "=")


if __name__=="__main__":
    main()