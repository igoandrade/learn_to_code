"""
Programa: exerc_04_lightning_strike.py
Autor   : Igo da Costa Andrdade
    Escreva um programa que determine a distância até a queda de 
    um raio com base no tempo decorrido entre o relâmpago e o som do trovão. 
    A velocidade do som é de aproximadamente 1100 pés / seg. E 1 milha é 5280 pés
"""
def calcula_distancia(tempo_decorrido, v_som = 1100):
    d = v_som * tempo_decorrido
    return d

def ft_to_miles(ft_value):
    mile_value = ft_value / 5280
    return mile_value


def main():
    num_colunas = 70
    print(num_colunas*"=")
    print("Este programa calcula a distância até a queda de um raio.")
    print(num_colunas*"-")
    tempo_decorrido = float(input("Informe o tempo em segundos entre o relâmpago e o som do trovão: "))
    distancia_pes = calcula_distancia(tempo_decorrido)
    distancia_milhas = ft_to_miles(distancia_pes)
    if (distancia_milhas >= 1):
        print(f"\nA distância até a queda do raio é {distancia_milhas:.1f} milhas.")
    else:
        print(f"\nA distância até a queda do raio é {distancia_pes:.1f} pés.")


    print(num_colunas*"=")

if __name__=="__main__":
    main()