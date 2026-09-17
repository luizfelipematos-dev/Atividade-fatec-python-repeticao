cont: int = 0
denominador: int = 1
res: float = 0

for cont in range(1,51,1):
    res = res + (cont/denominador)
    denominador = denominador+2

print('Resultado:', res)