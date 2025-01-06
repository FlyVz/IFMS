def mesclar_dicionarios(d1, d2):
    resultado = d1.copy()  
    
    for chave, valor in d2.items(): 
        if chave in resultado:  
            resultado[chave] += valor  
        else:
            resultado[chave] = valor 
    return resultado

dicionario1 = {'a': 10, 'b': 20, 'c': 30}
dicionario2 = {'b': 5, 'c': 10, 'd': 15}

resultado = mesclar_dicionarios(dicionario1, dicionario2)

print(resultado)
