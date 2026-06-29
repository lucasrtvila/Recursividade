def somaRecursiva (lista, tamanho) :
    if tamanho == 0:
        return 0
    
    return lista[tamanho-1] + somaRecursiva(lista, tamanho-1)

lista = []

while True:
    i = 1
    lista.append(int(input(f"Digite o {i}o número da lista (-1 para parar): ")))
    i+=1

    if lista[-1] <= -1:
        lista.pop()
        break
    
tamanho = len(lista)
listaSomada = somaRecursiva(lista, tamanho)

print(f"A soma de todos os elementos da lista é igual a {listaSomada}")