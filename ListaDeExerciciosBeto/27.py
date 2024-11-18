from collections import Counter

texto = input("Digite uma frase: ")

palavras = texto.lower().split()

contador = Counter(palavras)
for palavra, frequencia in contador.most_common(5):
    print(f"{palavra}: {frequencia}")

