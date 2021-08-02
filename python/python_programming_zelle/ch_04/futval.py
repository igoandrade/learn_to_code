
import math
from graphics import *

def future_value(principal, taxa, tempo):
    fv = principal * (1 + taxa/100) ** tempo
    return fv


def main():
    num_colunas = 50
    print(num_colunas*'=')
    print("Este programa calcula o valor futuro de um\ncapital incial (C) incvestido a uma taxa (i)\ndurante o período de tempo (n)")
    print(num_colunas*'-')
    principal = float(input("Informe o valor do capital inicial em reais (R$).\n\tC: "))
    taxa = float(input("Informe a taxa de capitalização (%).\n\ti: "))
    tempo = int(input("Informe o período do investimento am anos.\n\tn: "))
    print()
    print("Ano | Valor Futuro")
    lista_valor_futuro = []
    for i in range(tempo+1):
        valor_futuro = future_value(principal, taxa, i)
        lista_valor_futuro.append(valor_futuro)
        print(f"{i:>3d} | R$ {valor_futuro:>9.2f}")
    print(num_colunas*'=')
    
    valor_minimo = min(lista_valor_futuro)
    valor_maximo = max(lista_valor_futuro)
    largura_janela = 320
    altura_janela = 240
    fator_reducao = 0.8
    
    pos_inicial_x = .05 * largura_janela
    pos_inicial_y = .9 * altura_janela
    largura_barra = (.85 * largura_janela - 3*pos_inicial_x) / tempo
    janela = GraphWin('Investiment Growth Chart', largura_janela, altura_janela)
    valor_maximo_K = valor_maximo
    fator_mult = 1
    while valor_maximo_K >= 100:
        valor_maximo_K /= 10
        fator_mult *= 10
    valor_maximo_K = (1+int(valor_maximo_K)//25) * 2.5
    fator_mult *= 10

    passo_legenda = valor_maximo_K /5
    for i in range(6):
        legenda = passo_legenda * i
        y = pos_inicial_y - legenda/valor_maximo_K * altura_janela * fator_reducao
        label = Text(Point(pos_inicial_x, y), f"{legenda:>5.1f}")
        label.draw(janela)
    label = Text(Point(largura_janela/2, y), f"Em {int(fator_mult/1000)} mil reais")
    label.draw(janela)
    for n in range(tempo+1):
        altura_barra = lista_valor_futuro[n]/(fator_mult*valor_maximo_K) * altura_janela * fator_reducao
        x1 = 3* pos_inicial_x + largura_barra*n
        x2 = 3* pos_inicial_x + largura_barra*(n+1)
        rect = Rectangle(Point(x1,pos_inicial_y), Point(x2, pos_inicial_y-altura_barra))
        rect.setFill('green')
        rect.setOutline('black')
        rect.draw(janela)



    input("Pressione <Enter> para sair: ")
    janela.close()



if __name__=="__main__":
    main()