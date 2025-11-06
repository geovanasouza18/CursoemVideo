s = 0
for impar in range(1,501):
    if impar % 3 == 0:
        s += impar
print(f'O somatório dos números ímpares múltiplos de 3 é {s}')
