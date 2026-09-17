cont: int = 0
res: float = 0

for cont in range(1,16,1):
    if cont%2 == 0:
        res = res - (cont/(cont**2))
    else:
        res = res + (cont/(cont**2))

print('Resultado:', res)