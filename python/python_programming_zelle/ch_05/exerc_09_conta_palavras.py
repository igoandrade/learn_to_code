"""
Programa: exerc_09_conta_palavras.py
Autor: Igo da Costa Andrade
Enunciado:
    9. Write a program that counts the number of words in a sentence entered
    by the user.
"""

def conta_palavras(sentenca):
    return len(sentenca.split())

def main():
    sentenca = input("\nDigite uma sentença: ")
    qnt_palavras = conta_palavras(sentenca)
    print(f"\nA sentença digitada tem {qnt_palavras} palavras.")

if __name__=="__main__":
    main()