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


def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

inicio_selection = time.time()
resultado_selection = selection_sort(lista)
fim_selection = time.time()
total_selection = fim_selection - inicio_selection

escrever_lista_em_arquivo(resultado_selection, "selection_sorted.txt")

print("\n=============================")
print("Selection Sort")
print(f"Tempo de execução: {total_selection} segundos")
print(f"Total de elementos ordenados: {len(resultado_selection)}")


def insertion_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j <=0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave

    return arr

inicio_insertion = time.time()
resultado_insertion = insertion_sort(lista)
fim_insertion = time.time()
total_insertion = fim_insertion - inicio_insertion

escrever_lista_em_arquivo(resultado_insertion, "insertion_sorted.txt")

print("\n=============================")
print("Insertion Sort")
print(f"Tempo de execução: {total_insertion} segundos")
print(f"Total de elementos ordenados: {len(resultado_insertion)}")





