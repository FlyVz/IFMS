def palindromo(palavra):
    if palavra == palavra[::-1]:
        return "É palindromo"
    else:
        return "Não é palindromo"
print(palindromo("ana"))