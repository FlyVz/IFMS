def contar_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"
    
    contador_vogais = 0
    contador_consoantes = 0

    for caractere in frase:
        if caractere.isalpha():
            if caractere in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1
    
    return contador_vogais, contador_consoantes

frase = input("Digite uma frase: ")

vogais, consoantes = contar_vogais_consoantes(frase)

print(f"Número de vogais: {vogais}")
print(f"Número de consoantes: {consoantes}")
