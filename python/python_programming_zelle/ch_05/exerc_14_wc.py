"""
Programa: exerc_14_wc.py
Autor: Igo da Costa Andradr
Enunciado:
    14. Word Count. A common utility on UniX/Linux systems is a small program
    called ''we." This program analyzes a file to determine the number of
    lines, words, and characters contained therein. Write your own version of
    we. The program should accept a file name as input and then print three
    numbers showing the count of lines, words, and characters in the file.
"""
def wc(file):
    textContent = ""
    numLines = 0
    for line in file.readlines():
        numLines += 1
        textContent += line
    numWords = len(textContent.split())
    numChar = sum([len(word.strip()) for word in textContent])
    return numLines, numWords, numChar


def main():
    num_cols = 60
    print(num_cols*"=")
    print("Word Count".center(num_cols))
    print(num_cols*"-")
    fileName = input("Digite o nome do arquivo: ")
    inFile = open(fileName, "r")
    numLines, numWords, numChar = wc(inFile)
    print(num_cols*"-")
    print("Estatísticas do arquivo:")
    print(f"\tNúmero de linhas: {numLines:>12d}")
    print(f"\tNúmero de palavras: {numWords:>10d}")
    print(f"\tNúmero de caracteres: {numChar:>8d}")
    print(num_cols*"=")

if __name__=="__main__":
    main()