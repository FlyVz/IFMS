def remover_dupli(lista):
    semDuplicacao = []
    for numero in lista:
        if numero not in semDuplicacao:
            semDuplicacao.append(numero)
    return semDuplicacao

lista = list(map(int, input("Digite varios numeros inteiros separados por espaço: ").split()))

resultado = remover_dupli(lista)

print("Lista com numeros inteiros sem repetição:", resultado)
