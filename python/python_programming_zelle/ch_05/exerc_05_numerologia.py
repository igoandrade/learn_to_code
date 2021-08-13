"""
Programa: exerc_05_numerologia.py
Autor: Igo da Costa Andrade
Enunciado:
    5. Numerologists claim to be able to determine a person's character traits
    based on the "numeric value" of a name. The value of a name is determined 
    by summing up the values of the letters of the name where "a" is
    1' "b" is 2' "c" is 3' up to "z" being 26. For example' the name "Zelle"
    would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a
    very auspicious number, by the way). Write a program that calculates the
    numeric value of a single name provided as input.
"""

def numeric_value(str_input):
    num_value_list = [ord(char)-64 for char in str_input.upper()]
    return sum(num_value_list)

def main():
    print("\nEste programa calcula o valor numérico de um nome fornecido pelo usuário.")
    nome = input("\nDigite o seu primeiro nome: ")
    print(f"\nO valor numperico de {nome} é: {numeric_value(nome)}.")

if __name__=="__main__":
    main()