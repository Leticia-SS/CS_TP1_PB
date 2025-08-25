import time

def imprimir_string(strings):
    for string in strings:
        print(string)

def ler_arquivo_txt(nome_arquivo):
    strings = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                strings.append(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado")

    return strings

nome_arquivo = "output.txt"
lista = ler_arquivo_txt(nome_arquivo)

# imprimir_string(lista)

def escrever_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for item in lista:
            arquivo.write(str(item) + "\n")














