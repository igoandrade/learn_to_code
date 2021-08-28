"""
The Goldbach conjecture asserts that every even number is the sum of two
prime numbers. Write a program that gets a number from the user, checks
to make sure that it is even, and then finds two prime numbers that add
up to the number.
"""

def eh_primo(n):
    if n < 2:
        return False
    lim = round(n**.5)
    for i in range(2, lim + 1):
        if n % i == 0:
            return False
    return True

def lista_primos(n):
    primos = []
    for p in range(2, n):
        if eh_primo(p):
            primos.append(p)
    return primos

def goldbach_conjecture(n):
    if n % 2 == 0:
        pares = []
        primos = lista_primos(n)
        l = len(primos)
        for i in range(l):
            for j in range(i, l):
                a, b = primos[i], primos[j]
                if ((a + b) == n):
                    pares.append([a, b])
        return pares
    else:
        return None

def conta_digitos(n):
    d = 0
    while n > 0:
        n //= 10
        d += 1
    return d 

def main():
    l = 45
    print(l * "=")
    print(" Conjectura de Goldbach ".center(l, "-"))
    print(l * "=")
    n = int(input("Digite um número inteiro positivo: "))
    while (n <= 0):
        print("\nOps! Entrada inválida!!")
        n = int(input("Digite um número inteiro positivo: "))
    print(l * "-")
    d = conta_digitos(n)
    if (n % 2 == 0):
        pares = goldbach_conjecture(n)
        for par in pares:
            a, b = par[0], par[1]
            print(f"{n} = {a:>{d}d} + {b:>{d}d}".center(l))
    print(l * "=")

if __name__=="__main__":
    main()