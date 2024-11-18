def palavraFirst(palavra):
    return sorted(palavra.lower())
def palavraSecond(palavra):
    return sorted(palavra.lower())

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavraFirst(palavra1) == palavraSecond(palavra2):
    print("São anagramas")
else:
    print("Não são anagramas")    