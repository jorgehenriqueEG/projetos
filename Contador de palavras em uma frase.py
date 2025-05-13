def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    total_palavras = contar_palavras(frase)
    print(f"A frase contém {total_palavras} palavras.")