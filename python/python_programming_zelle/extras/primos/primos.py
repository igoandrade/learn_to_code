import time

def ehPrimo(n):
    if n < 2:
        return False
    else:
        i = 2
        while (i < n/i):
            if (n%i == 0):
                return False
            i += 1
    return True




n = 100000001
print("===== Primeiro Teste ======")
inicio = time.time()
for i in range(n):
    if (ehPrimo(i)):
        print(i)
fim = time.time()
t1 = fim - inicio

print("===== Resultado ======")
print("ehPrimo")
print(f"{t1:>7.4f}")

