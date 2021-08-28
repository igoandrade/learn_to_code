"""
Write a program that computes the fuel efficiency of a multi-leg journey.
The program will first prompt for the starting odometer reading and then
get information about a series of legs. For each leg, the user enters the
current odometer reading and the amount of gas used (separated by a
space) . The user signals the end of the trip with a blank line. The program
should print out the miles per gallon achieved on each leg and the total
MPG for the trip.
"""

def valida_entrada(entrada, q = 2, sep=" "):
    entrada = entrada.strip()
    if entrada == "":
        return entrada
    else:
        lista = [i.strip() for i in entrada.split(sep) if i.strip() != ""]
        if (len(lista) != q):
            return None
        else:
            return [float(i) for i in lista]


def main():
    l = 75
    print(l * "=")
    print(" Eficiência de combustível ". center(l, "-") + "\n")
    km_inicial = float(input("Informe a quilometragem inicial: "))
    n = 1
    km = []
    gas = []
    entrada = valida_entrada(input(f"\nTrecho nº {n:>2d}:\n\tInforme a leitura atual do odômetro e a quantidade de gasolina\n\tusada nesse percurso (separados por espaço): "))
    while entrada != "":
        while entrada == None:
            print("\nOps!! Entrada inválida!")
            entrada = valida_entrada(input(f"Trecho nº {n:>2d}:\n\tInforme a leitura atual do odômetro e a quantidade de gasolina\n\tusada nesse percurso (separados por espaço): "))        
        km.append(entrada[0])
        gas.append(entrada[1])
        n += 1
        entrada = valida_entrada(input(f"Trecho nº {n:>2d}:\n\tInforme a leitura atual do odômetro e a quantidade de gasolina\n\tusada nesse percurso (separados por espaço): "))
    print("\n" + " Resultados ".center(l, "-"))
    dx = [o - km_inicial for o in km]
    mpg = [dx[i]/gas[i] for i in range(len(dx))]

    print(f" Trecho | Odômetro (m) | Dist. Perc. (m) | Consumo (g) | Eficiência (mpg) ".center(l))
    print(l * "-")
    print(f" {0:^6d} | {km_inicial:>12.2f} | {'-':>15s} | {'-':>11s} | {'-':>16s} ".center(l))
    for i in range(len(dx)):
        print(f" {i+1:^6d} | {km[i]:>12.2f} | {dx[i]:>15.2f} | {gas[i]:>11.2f} | {mpg[i]:>16.2f} ".center(l))
    print(l * "=")




if __name__=="__main__":
    main()