"""
Programa: exerc_10_comprimento_medio.py
Autor: Igo da Costa Andrade
Enunciado:
    10. Write a program that calculates the average word length in a sentence
    entered by the user.
"""

def avg_words_length(sentenca):
    words_length = [len(_.strip()) for _ in sentenca.split()]
    return sum(words_length)/len(words_length)

def main():
    sentenca = input("\nDigite uma sentença: ")
    avg_palavras = avg_words_length(sentenca)
    print(f"\nA sentença digitada tem em média {avg_palavras:.2f} palavras.")

if __name__=="__main__":
    main()
