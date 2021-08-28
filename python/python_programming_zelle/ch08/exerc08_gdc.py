"""
The greatest common divisor (GCD) of two values can be computed using
Euclid's algorithm. Starting with the values m and n, we repeatedly apply
the formula: m, n = n , m % n until n is 0. At that point, m is the GCD of
the original m and n. Write a program that finds the GCD of two numbers
using this algorithm.
"""

def gcd(m, n):
    m, n = max(m, n), min(m, n)
    while (n != 0):
        m, n = n , m % n
    return m

def valida_entrada(str_input, q = 2, sep = ','):
    if sep not in str_input:
        return False
    else:
        str_lista = [i.strip() for i in str_input.split(sep)]
        l = len(str_lista)
        if (l != q):
            return False
        else:
            for s in str_lista:
                if s == '':
                    return False
    return True


def main():
    l = 60
    print(l * "=")
    print(" Greatest Common Divisor (GCD) ".center(l))
    print(l * "-")
    str_input = input("Informe dois números inteiros separados por vírgula: ")
    while (not valida_entrada(str_input)):
        print("\nOps! Entrada inválida!")
        str_input = input("Informe dois números inteiros separados por vírgula: ")
 
    m, n = [int(i.strip()) for i in str_input.split(sep=',')]
    print(l * "-")
    gcd_mn = gcd(m, n)
    print(f"GCD{m, n} = {gcd_mn}".center(l))
    print(l * "=")
    


if __name__=="__main__":
    main()