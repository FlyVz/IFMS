def fibonacci(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n] 

n = int(input("Digite um número para gerar a sequência de Fibonacci: "))

resultado = fibonacci(n)
print(f"Os {n} primeiros números da sequência de Fibonacci {resultado}")
