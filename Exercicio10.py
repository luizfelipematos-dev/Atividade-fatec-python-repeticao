n1: int = 0
n2: int = 0
numero: int = 0
cont: int = 0
div: int = 0

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

for numero in range(n1,n2+1,1):
    div = 0

    for cont in range(1,numero+1,1):
        if numero%cont == 0:
            div = div+1

    if div == 2:
        print(numero)