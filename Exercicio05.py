n1: int = 0
n2: int = 0
cont: int = 0
soma: int = 0

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

for cont in range(n1,n2+1,1):
    if cont%2 != 0:
        soma = soma + cont

print('Soma dos impares:', soma)