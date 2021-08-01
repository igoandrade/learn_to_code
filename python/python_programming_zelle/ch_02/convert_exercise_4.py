# convert_exercise_4.py
#   Um programa que converte cinco temperaturas Celsius para Fahrenheit
# Autor: Igo da Costa Andrade

import convert


def main():
    print(65*"=")
    print("Este programa solicita do usuário cinco temperaturas em graus\nCelsius (°C) e converte os valores para graus Fahrenheit (°F).")
    
    for i in range(5):
        print(65*"-")
        print(f"{i+1}ª Temperatura:")
        convert.interface()
    print(65*"=")


if __name__=='__main__':
    main()