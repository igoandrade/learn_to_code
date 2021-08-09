"""
Programa: exerc_06_numerologia2.py
Autor: Igo da Costa Andrade
Enunciado:
    6. Expand your solution to the previous problem to allow the calculation of
    a complete name such as '3"ohn Marvin Zelle" or '3"ohn Jacob Jingleheimer
    Smith." The total value is just the sum of the numeric values of all the
    names.
"""

from exerc_05_numerologia import numeric_value

def main():
    print(numeric_value('igo'))
    print("\nEste programa calcula o valor numérico de um nome fornecido pelo usuário.")
    nome_completo = input("\nDigite o seu nome: ")
    soma = sum([numeric_value(_) for _ in nome_completo.split()])
    print(f"\nO valor numérico de {nome_completo} é: {soma}.")


if __name__=="__main__":
    main()

