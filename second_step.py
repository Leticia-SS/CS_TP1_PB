import sys
import time
from collections import deque


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

posicoes = [0, 99, 999, 4999, len(lista)-1]


inicio_criacao = time.time()
hashtable = {}
for i, arquivo in enumerate(lista):
    hashtable[i] = arquivo
fim_criacao = time.time()

memoria_ht = sys.getsizeof(hashtable)
for key, value in hashtable.items():
    memoria_ht += sys.getsizeof(key) + sys.getsizeof(value)

inicio_recuperacao = time.time()
arquivos_ht = {}
for pos in posicoes:
    arquivos_ht[pos] = hashtable.get(pos)
fim_recuperacao = time.time()

print("====================")
print("Hashtable")
print(f"Tempo de criação: {fim_criacao - inicio_criacao:.6f} segundos")
print(f"Tempo de recuperação: {fim_recuperacao - inicio_recuperacao:.6f} segundos")
print(f"Memória utilizada: {memoria_ht} bytes")
print("\nArquivos recuperados:")
for pos in posicoes:
    print(f"Posição {pos + 1}: {hashtable.get(pos)}")
print("\n")

inicio_criacao = time.time()
pilha = list(lista)
fim_criacao = time.time()

memoria_pilha = sys.getsizeof(pilha)
for item in pilha:
    memoria_pilha += sys.getsizeof(item)

inicio_recuperacao = time.time()
arquivos_pilha = {}
for pos in posicoes:
    if pos < len(pilha):
        arquivos_pilha[pos] = pilha[pos]
    else:
        arquivos_pilha[pos] = None
fim_recuperacao = time.time()

print("====================")
print("Pilha")
print(f"Tempo de criação: {fim_criacao - inicio_criacao:.6f} segundos")
print(f"Tempo de recuperação: {fim_recuperacao - inicio_recuperacao:.6f} segundos")
print(f"Memória utilizada: {memoria_pilha} bytes")
print("\nArquivos recuperados:")
for pos in posicoes:
    print(f"Posição {pos + 1}: {pilha[pos]}")
print("\n")


inicio_criacao = time.time()
fila = deque(lista)
fim_criacao = time.time()

memoria_fila = sys.getsizeof(fila)
for item in fila:
    memoria_fila += sys.getsizeof(item)

inicio_recuperacao = time.time()
lista_fila = list(fila)
arquivos_fila = {}
for pos in posicoes:
    if pos < len(lista_fila):
        arquivos_fila[pos] = lista_fila[pos]
    else:
        arquivos_fila[pos] = None
fim_recuperacao = time.time()


print("====================")
print("Fila")
print(f"Tempo de criação: {fim_criacao - inicio_criacao:.6f} segundos")
print(f"Tempo de recuperação: {fim_recuperacao - inicio_recuperacao:.6f} segundos")
print(f"Memória utilizada: {memoria_fila} bytes")
print("\nArquivos recuperados:")
for pos in posicoes:
    if pos < len(lista_fila):
        print(f"Posição {pos + 1}: {lista_fila[pos]}")
    else:
        print(f"Posição {pos + 1}: Não encontrado")
print("\n")








