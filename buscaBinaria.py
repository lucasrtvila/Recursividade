def buscaBinaria(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == alvo:
        return meio
    elif alvo > lista[meio]:
        return buscaBinaria(lista, alvo, meio +1, fim)
    else:
        return buscaBinaria(lista, alvo, inicio, meio -1)


lista = []
alvo = 0
while True: 
    lista.append(int(input("Digite um número aleatório (0 para parar): ")))

    if lista[-1] == 0:
        lista.pop()
        break

lista = list(sorted(lista))
fim = len(lista)-1
alvo = int(input("Digite o número a ser encontrado: "))

print(lista)
posicaoAlvo = buscaBinaria(lista,alvo, 0, fim)
if posicaoAlvo >=0:
    print(f"O número {alvo} está na {posicaoAlvo+1}a posição na lista.")
else:
    print(f"O número {alvo} não está na lista.")