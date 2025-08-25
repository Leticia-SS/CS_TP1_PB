def imprimir_string(strings):
    for string in strings:
        print(string)

def let_arquivo_txt(nome_arquivo):
    strings = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                strings.append(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado")

    return strings

nome_arquivo = "output.txt"
strings = let_arquivo_txt(nome_arquivo)

imprimir_string(strings)

