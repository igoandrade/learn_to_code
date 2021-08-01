"""
Programa: exerc_08_gregorian_epact.py
Autor:    Igo da Costa Andrade
    The Gregorian epact is the number of days between January 1st and the
    previous new moon. This value is used to figure out the date of Easter. It
    is calculated by these formulas (using int arithmetic):
        C = year // 100
        epact = ((8+C//4)-C+((8C+13)//25)+11(year%19))%30
    Write a program that prompts the user for a 4-digit year and then outputs
    the value of the epact.
"""


def calcula_epact(ano):
    C = ano//100
    epact = ((8+C//4)-C+((8*C+13)//25)+11*(ano%19))%30
    return epact


def main():
    num_colunas=50
    print(num_colunas*"=")
    print("Este programa calcula o valor do epact*.\n\t(* Número de dias entre o dia\n\t1º de janeiro e a lua nota anterior.)")
    print(num_colunas*"-")
    ano = int(input("Informe um ano com 4 dígitos: "))
    epact = calcula_epact(ano)
    print(f"Epact para o ano {ano}: {epact} dias")
    print(num_colunas*"=")


if __name__=="__main__":
    main()