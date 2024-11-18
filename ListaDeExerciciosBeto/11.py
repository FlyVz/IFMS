def quantidade():
    palavraUnica = set(frase.lower().split())
    return palavraUnica.__len__()

frase = input("Digite uma frase:")
print(f"Tem {quantidade()} palavras unicas na frase")