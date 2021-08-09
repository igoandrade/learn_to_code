"""
Programa: exerc_07_caesar_cipher.py
Autor: Igo da Costa Andrade
Enunciado:
    7. A Caesar cipher is a simple substitution cipher based on the idea of shifting
    each letter of the plaintext message a fixed number (called the key) of
    positions in the alphabet. For example, if the key value is 2, the word
    "Sourpuss" would be encoded as "Uqwtrwuu." The original message can
    be recovered by "reencoding" it using the negative of the key.
    Write a program that can encode and decode Caesar ciphers. The input to the program will be a string of plaintext and the value of the key.
    The output will be an encoded message where each character in the original message is replaced by shifting it key characters in the Unicode character set. For example, if ch is a character in the string and key is the
    amount to shift, then the character that replaces ch can be calculated as:
    chr (ord (ch) + key) .
"""

def caesar_cipher(str_input, key):
    str_lista = str_input.split()
    str_lista_criptografada = []
    for palavra in str_lista:
        palavra_criptografada = ""
        for caractere in palavra.lower():
            caractere_criptogradado = chr((ord(caractere)-97+key)%26 + 97)
            palavra_criptografada += caractere_criptogradado
        str_lista_criptografada.append(palavra_criptografada)
    return " ".join(str_lista_criptografada)
        



def main():
    print("\nEste programa usa a Cifra de César para\ncodificar/decodificar uma mensagem informada pelo usuário.")
    mensagem = input("\nDigite a mensagem: ")
    key = int(input("\nDigite a chave do código: "))
    opcao = input("\nEscolha:\n\t1 - codificar a mensagem\n\t2 - decodificar a mensagem ")
    while opcao != '1' and opcao != '2':
        print("Opcação inválida!")
        opcao = input("\nEscolha:\n\t1 - codificar a mensagem\n\t2 - decodificar a mensagem ")
    if opcao == '1':
        comp = "codificação"
    else:
        comp = "decodificação"
        key = -key
    
    mensagem_saida = caesar_cipher(mensagem, key)

    print(f"\nResultado da {comp}:\n\n\t{mensagem_saida}")



if __name__=='__main__':
    main()