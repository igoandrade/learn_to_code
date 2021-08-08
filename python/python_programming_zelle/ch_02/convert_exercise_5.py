# convert_exercise_5.py
#   Imprime uma tabela de equivalência de temperaturas Celsius 
#   e temperaturas Fahrenheit de 10 graus de 0°C até 100°C
# autor: Igo da Costa Andrade

import convert

def main():
    num_colunas = 50
    print(num_colunas * "=")
    print("Este programa imprime uma tabela de equivalência\nde temperaturas Celsius e temperaturas Fahrenheit\nde 10 graus de 0°C até 100°C")
    print(num_colunas * "-")
    print(f"{'Celsius (°C)':>20s} {'Fahrenheit (°F)':>20s}")
    for c in range(0,101,10):
        f = convert.celsius_to_fahrenheit(c)
        print(f"{c:>20.1f} {f:>20.1f}")
    print(num_colunas * "=")

if __name__=="__main__":
    main()

