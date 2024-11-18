matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

for l in range(0, 3):
    soma_diagonal_principal += matriz[l][l]  
    soma_diagonal_secundaria += matriz[l][2 - l]  

print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
