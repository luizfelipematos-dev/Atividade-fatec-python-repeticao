numero: int = 0
cont: int = 0
res: int = 0

numero = int(input('Digite um numero: '))

for cont in range(0,11,1):
    res = cont*numero
    print(res)