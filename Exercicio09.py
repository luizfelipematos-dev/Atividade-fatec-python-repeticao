casa: int = 0
graos: int = 1
total: int = 0

for casa in range(1,65,1):
    total = total + graos
    graos = graos*2

print('Quantidade de graos:', total)