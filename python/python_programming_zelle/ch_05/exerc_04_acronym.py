"""
Programa: exerc_04_acronym.py
Autor:  Igo da Costa Andrade
Enunciado:
    4. An acronym is a word formed by taking the first letters of the words in a
    phrase and making a word from them. For example, RAM is an acronym
    for "random access memory." Write a program that allows the user to
    type in a phrase and then outputs the acronym for that phrase. Note: The
    acronym should be all uppercase, even if the words in the phrase are not
    capitalized.
"""

def acronymizer(strInput):
    firsts =  [_[0] for _ in strInput.split()]
    return ''.join(firsts).upper()


def main():
    print("Esse programa converte uma frase informada pelo usuário no acrônimo equivalente.")
    strInput = input("\nDigite uma frase: ")
    acronym = acronymizer(strInput)
    print(f"\nO acrônimo equivalente à frase digitada é: {acronym}.")

if __name__=="__main__":
    main()