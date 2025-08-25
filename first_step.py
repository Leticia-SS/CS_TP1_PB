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


def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True

        if not trocou:
            break

    return arr

inicio_bubble = time.time()
resultado_bubble = bubble_sort(lista)
fim_bubble = time.time()
total_bubble = fim_bubble - inicio_bubble

escrever_lista_em_arquivo(resultado_bubble, "bubble_sorted.txt")

print("\n=============================")
print("Bubble Sort")
print(f"Tempo de execução: {total_bubble} segundos")
print(f"Total de elementos ordenados: {len(resultado_bubble)}")













