def remover_dupli(lista):
    lista_sem_duplicados = []
    for numero in lista:
        if numero not in lista_sem_duplicados:
            lista_sem_duplicados.append(numero)
    return lista_sem_duplicados

lista = list(map(int, input("Digite varios numeros inteiros separados por espaço: ").split()))

resultado = remover_dupli(lista)

print("Lista com numeros inteiros sem repetição:", resultado)
