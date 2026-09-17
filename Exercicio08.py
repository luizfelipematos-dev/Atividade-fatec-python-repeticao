numero: int = 0
cont: int = 0
maior: int = 0
menor: int = 0

for cont in range(0,100,1):
    numero = int(input('Digite um numero positivo: '))

    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print('Maior:', maior)
print('Menor:', menor)