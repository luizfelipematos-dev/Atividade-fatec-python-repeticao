numero: int = 0
cont: int = 0
res: float = 0

numero = int(input('Digite um numero: '))

for cont in range(1,numero+1,1):
    res = res + (1/cont)

print('Resultado:', res)