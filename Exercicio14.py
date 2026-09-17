base: int = 0
expoente: int = 0
cont: int = 0
res: int = 1

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

for cont in range(0,expoente,1):
    res = res*base

print('Potencia:', res)