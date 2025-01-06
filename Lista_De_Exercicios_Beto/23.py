def soma(a,b):
    return a + b
def multi(a,b):
    return a * b
def subtracao(a,b):
    return a - b
def divisao (a,b):
    return a / b
def potencia(a,b):
    return a ** b
    
a = float(input("Digite o numero a: "))
b = float(input("Digite o numero b: "))
operacao = input("Digite a operacao desejada sem acentos: ")

if operacao.lower() == "soma":
    print(soma(a,b))
elif operacao.lower() == "subtracao" or operacao.lower() == "subtraçao":
    print(subtracao(a,b))
elif operacao.lower() == "multiplicacao" or operacao.lower() == "multiplicaçao":
    print(multi(a,b))
elif operacao.lower() == "divisao":
    print(divisao(a,b))
elif operacao.lower() == "potencia":
    print(potencia(a,b))
else:
    print("Operação invalida")
    