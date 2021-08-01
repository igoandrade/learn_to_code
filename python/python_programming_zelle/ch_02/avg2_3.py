# avg2_3.py
#   Calcula a média de três notas de um exame
# autor: Igo da Costa Andrade

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

def main():
    num_colunas = 50
    print(num_colunas*"=")
    print("Este programa calcula a média de\ntrês notas de um exame fornecidas pelo usuário.")
    print(num_colunas*"-")
    nota1, nota2, nota3 = eval(input("Digite as três notas separadas por vírgula: "))
    media = calcula_media(nota1, nota2, nota3)
    print(f"\nResultado:")
    cabecalho = " 1ª Nota  2ª Nota  3ª Nota  Média "


    linha_notas = f" {nota1:>7.1f}  {nota2:>7.1f}  {nota3:>7.1f}  {media:>5.1f}"

    print(len(cabecalho)*"-")
    print(cabecalho)
    print(len(cabecalho)*"-")
    print(linha_notas)
    print(len(cabecalho)*"-")

    print(num_colunas*"=")

if __name__=="__main__":
    main()