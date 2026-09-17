dado1: int = 0
dado2: int = 0

for dado1 in range(1,7,1):
    for dado2 in range(1,7,1):
        if dado1+dado2 == 7:
            print(dado1,dado2)