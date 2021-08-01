# convert.py
#   Um programa que converte temperatura Celsius para Fahrenheit
# Autor: Igo da Costa Andrade

def celsius_to_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit

def interface():
    celsius = float(input("Qual a temperatura em Celsius? "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"\nA temperatura é {fahrenheit:>.1f} graus Fahrenheit.")


def main():
    print(65*"=")
    print("Este programa solicita do usuário uma temperatura em graus\nCelsius (°C) e converte esse valor para graus Fahrenheit (°F).")
    print(65*"-")
    interface()
    print(65*"=")


if __name__=='__main__':
    main()