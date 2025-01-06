def contador(frase):
    vogais = "aeiouAEIOU"
    num_vogais = 0
    num_consoantes = 0

    for caractere in frase:
        if caractere.isalpha():  
            if caractere in vogais:
                num_vogais += 1
            else:
                  num_consoantes += 1

    return num_vogais, num_consoantes

frase = input("Digite uma frase: ")

vogais, consoantes = contador(frase)

print(f"Número de vogais: {vogais}")
print(f"Número de consoantes: {consoantes}")
