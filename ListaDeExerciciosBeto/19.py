def contar_caracteres(frase):
    contador = {}

    for caractere in frase:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador

frase = input("Digite uma frase: ")

resultado = contar_caracteres(frase)

print("Contagem de caracteres:", resultado)
