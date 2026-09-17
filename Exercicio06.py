numero: int = 0
cont: int = 0
fat: int = 1
res: float = 1

numero = int(input('Digite um numero: '))

for cont in range(1,numero+1,1):
    fat = fat*cont
    res = res + (1/fat)

print('Resultado:', res)